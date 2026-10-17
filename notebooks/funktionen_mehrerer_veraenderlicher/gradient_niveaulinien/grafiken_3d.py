"""3D-Grafiken zur Präsentation "Gradient und Niveaulinien".

Erzeugt
  abb_flaeche.svg/.png : Fläche z = x² + 4y² mit Schnittkurven in Höhe c
                         und deren Projektion (Höhenlinien) in die xy-Ebene
  abb_weg3d.svg/.png   : Weg des Gradientenverfahrens (eta = 0.2, Start (4, 1))
                         auf der Fläche und sein Schatten in der xy-Ebene
Aufruf: python grafiken_3d.py
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# Calibri-ähnliche Schrift verwenden, falls vorhanden (sonst Standardschrift)
_namen = {f.name for f in fm.fontManager.ttflist}
_schrift = next((n for n in ('Calibri', 'Carlito') if n in _namen), 'DejaVu Sans')
plt.rcParams.update({'font.family': _schrift, 'font.size': 10, 'mathtext.fontset': 'stix',
                     'svg.fonttype': 'path', 'axes.unicode_minus': True})
RED, DARK, GRAY, SURF = '#E2001A', '#5C6970', '#9DA4AA', '#DEEAF6'
CM = 1 / 2.54

def surface(ax, rmax, alpha=0.35):
    r = np.linspace(0, rmax, 30); t = np.linspace(0, 2 * np.pi, 73)
    R, T = np.meshgrid(r, t)
    X, Y = R * np.cos(T), R / 2 * np.sin(T); Z = X ** 2 + 4 * Y ** 2
    ax.plot_surface(X, Y, Z, color=SURF, alpha=alpha, linewidth=0, shade=False, zorder=0)
    ax.plot_wireframe(X, Y, Z, rstride=6, cstride=3, color=GRAY, linewidth=0.35, alpha=0.7)

def clean(ax, zmax):
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_visible(False); a.line.set_color(DARK); a.line.set_linewidth(0.6)
    ax.grid(False)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.set_xlabel('$x$', labelpad=-14); ax.set_ylabel('$y$', labelpad=-14); ax.set_zlabel('$z$', labelpad=-16)

def save(fig, name):
    fig.savefig(name + '.svg', transparent=True)
    fig.savefig(name + '.png', dpi=300, transparent=False, facecolor='white')
    plt.close(fig)

# ---------- Fläche mit Höhenlinien (Abb. 1 der Präsentation) Fläche mit Höhenlinien und Projektion ----------
fig = plt.figure(figsize=(7.6 * CM, 6.4 * CM))
ax = fig.add_axes([-0.08, -0.08, 1.16, 1.16], projection='3d')
surface(ax, 4.0)
t = np.linspace(0, 2 * np.pi, 200)
for c in (1, 4, 9, 16):
    a = np.sqrt(c); x, y = a * np.cos(t), a / 2 * np.sin(t)
    ax.plot(x, y, np.full_like(t, c), color=RED, lw=1.4, zorder=5)
    ax.plot(x, y, np.zeros_like(t), color=DARK, lw=0.9, zorder=4)
    for tt in (np.pi * 0.15, np.pi * 1.15):
        ax.plot([a * np.cos(tt)] * 2, [a / 2 * np.sin(tt)] * 2, [0, c], color=DARK, lw=0.5, ls=(0, (2, 2)))
    if c > 1: ax.text(-a - 0.35, 0, c, f'$c={c}$', color=RED, fontsize=8, ha='right', va='center')
ax.set_xlim(-4, 4); ax.set_ylim(-2.6, 2.6); ax.set_zlim(0, 16)
ax.set_box_aspect((8, 5.2, 6.5), zoom=0.98)
ax.view_init(elev=24, azim=-58)
ax.set_xlim(-5.2, 4)
clean(ax, 16)
save(fig, 'abb_flaeche')

# ---------- Gradientenweg auf der Fläche ----------
# ---------- (Abb. 7 der Präsentation) Gradientenweg auf der Fläche ----------
p = [(4.0, 1.0)]
for k in range(5): p.append((0.6 * p[-1][0], -0.6 * p[-1][1]))
p = np.array(p); fz = p[:, 0] ** 2 + 4 * p[:, 1] ** 2
fig = plt.figure(figsize=(10.0 * CM, 6.2 * CM))
ax = fig.add_axes([-0.06, -0.12, 1.12, 1.24], projection='3d')
surface(ax, np.sqrt(20), alpha=0.25)
for c in fz[:4]:
    a = np.sqrt(c); ax.plot(a * np.cos(t), a / 2 * np.sin(t), np.zeros_like(t), color=GRAY, lw=0.7)
ax.plot(p[:, 0], p[:, 1], np.zeros(len(p)), color=DARK, lw=1.0, ls=(0, (3, 2)), marker='o', ms=2.5)
for (x, y), z in zip(p, fz):
    ax.plot([x, x], [y, y], [0, z], color=DARK, lw=0.5, ls=(0, (1, 2)))
ax.plot(p[:, 0], p[:, 1], fz, color=RED, lw=1.6, marker='o', ms=3.5, zorder=10)
for k, dz in ((0, 0.8), (1, 0.0), (2, 0.0)):
    ax.text(p[k, 0] - 0.35, p[k, 1], fz[k] + dz, f'$x^{{({k})}}$', color=RED, fontsize=9, ha='right', va='center')
ax.set_xlim(-4.5, 4.5); ax.set_ylim(-2.3, 2.3); ax.set_zlim(0, 20)
ax.set_box_aspect((9, 4.6, 5), zoom=1.08)
ax.view_init(elev=22, azim=-62)
clean(ax, 20)
save(fig, 'abb_weg3d')
print('Grafiken gespeichert: abb_flaeche.*, abb_weg3d.*')
