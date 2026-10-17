import numpy as np
import matplotlib.pyplot as plt

def gradientenverfahren(grad, x0, eta, eps=1e-6, maxit=10000):
    """Gibt (x, Iterationen, Weg) zurück; Iterationen = None,
    falls das Verfahren divergiert oder maxit erreicht."""
    x = np.array(x0, dtype=float)
    weg = [x.copy()]
    for k in range(maxit):
        g = grad(x)
        if np.linalg.norm(g) < eps:      # konvergiert
            return x, k, np.array(weg)
        x = x - eta * g
        weg.append(x.copy())
        if np.linalg.norm(x) > 1e6:      # divergiert
            return x, None, np.array(weg)
    return x, None, np.array(weg)

grad = lambda x: np.array([2*x[0], 8*x[1]])

# b) Iterationszahlen
for eta in [0.05, 0.1, 0.2, 0.24, 0.26]:
    x, k, weg = gradientenverfahren(grad, [4, 1], eta)
    text = f"{k} Iterationen" if k is not None else "divergent"
    print(f"eta = {eta:.2f}: {text}")

# c) Wege im Höhenlinienbild
X, Y = np.meshgrid(np.linspace(-5, 5, 200), np.linspace(-3, 3, 200))
plt.contour(X, Y, X**2 + 4*Y**2, levels=15, colors="gray")
for eta, farbe in [(0.2, "red"), (0.24, "blue")]:
    x, k, weg = gradientenverfahren(grad, [4, 1], eta)
    plt.plot(weg[:, 0], weg[:, 1], "o-", color=farbe,
             label=f"eta = {eta}")
plt.axis("equal")    # gleiche Skalierung: rechte Winkel sichtbar
plt.legend()
plt.show()
