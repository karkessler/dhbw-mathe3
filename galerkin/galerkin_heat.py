"""Eigenständiges Lernmodell zur eindimensionalen Wärmeleitung.

Das Modul verwendet lineare finite Elemente (Galerkin-Verfahren im Raum)
und Crank--Nicolson (Trapezregel) in der Zeit. Es wurde für das Web-Lernmodul
neu entworfen und übernimmt keinen Quelltext des historischen FORTRAN-Programms.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class HeatSolution:
    """Zeit- und Ortsgitter sowie die zugehörigen Knotenwerte."""

    x: np.ndarray
    times: np.ndarray
    values: np.ndarray


def initial_condition(x: np.ndarray) -> np.ndarray:
    """Glatte Anfangsbedingung, deren exakte Lösung bekannt ist."""

    return np.sin(np.pi * x) + 0.25 * np.sin(3.0 * np.pi * x)


def exact_solution(x: np.ndarray, t: float, diffusivity: float = 1.0) -> np.ndarray:
    """Exakte Lösung für die im Lernmodul verwendete Anfangsbedingung."""

    first = np.exp(-diffusivity * np.pi**2 * t) * np.sin(np.pi * x)
    third = 0.25 * np.exp(-diffusivity * (3.0 * np.pi) ** 2 * t) * np.sin(3.0 * np.pi * x)
    return first + third


def assemble_matrices(elements: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Erzeuge Gitter, Massenmatrix und Steifigkeitsmatrix für P1-Elemente.

    Die zurückgegebenen Matrizen enthalten nur die inneren Freiheitsgrade;
    an beiden Endpunkten gelten homogene Dirichlet-Randbedingungen.
    """

    if elements < 2:
        raise ValueError("elements muss mindestens 2 sein")

    x = np.linspace(0.0, 1.0, elements + 1)
    h = 1.0 / elements
    unknowns = elements - 1

    mass = np.diag(np.full(unknowns, 2.0 * h / 3.0))
    stiffness = np.diag(np.full(unknowns, 2.0 / h))
    if unknowns > 1:
        mass += np.diag(np.full(unknowns - 1, h / 6.0), 1)
        mass += np.diag(np.full(unknowns - 1, h / 6.0), -1)
        stiffness += np.diag(np.full(unknowns - 1, -1.0 / h), 1)
        stiffness += np.diag(np.full(unknowns - 1, -1.0 / h), -1)

    return x, mass, stiffness


def solve_heat_equation(
    elements: int = 40,
    dt: float = 0.002,
    final_time: float = 0.2,
    diffusivity: float = 1.0,
) -> HeatSolution:
    """Löse ``u_t = diffusivity * u_xx`` mit Crank--Nicolson."""

    if dt <= 0.0 or final_time < 0.0 or diffusivity <= 0.0:
        raise ValueError("dt und diffusivity müssen positiv, final_time muss nichtnegativ sein")

    x, mass, stiffness = assemble_matrices(elements)
    steps = max(1, int(np.ceil(final_time / dt))) if final_time > 0.0 else 0
    times = np.linspace(0.0, final_time, steps + 1)
    actual_dt = times[1] - times[0] if steps else 0.0

    values = np.zeros((steps + 1, elements + 1))
    values[0] = initial_condition(x)
    values[0, (0, -1)] = 0.0
    if not steps:
        return HeatSolution(x=x, times=times, values=values)

    left = mass + 0.5 * actual_dt * diffusivity * stiffness
    right = mass - 0.5 * actual_dt * diffusivity * stiffness
    transition = np.linalg.solve(left, right)
    interior = values[0, 1:-1].copy()

    for index in range(1, steps + 1):
        interior = transition @ interior
        values[index, 1:-1] = interior

    return HeatSolution(x=x, times=times, values=values)


def l2_error(solution: HeatSolution, diffusivity: float = 1.0) -> float:
    """Berechne den diskreten L2-Fehler am letzten Zeitpunkt."""

    reference = exact_solution(solution.x, float(solution.times[-1]), diffusivity)
    difference_squared = (solution.values[-1] - reference) ** 2
    return float(np.sqrt(np.trapz(difference_squared, solution.x)))

