import numpy as np

def gradientenverfahren(grad, x0, eta, eps=1e-6, maxit=1000):
    """Minimiert f mit x(k+1) = x(k) - eta * grad f(x(k))."""
    x = np.array(x0, dtype=float)
    weg = [x.copy()]                  # Iterierte speichern
    for k in range(maxit):
        g = grad(x)                   # Gradient in x(k)
        if np.linalg.norm(g) < eps:   # Abbruch: |g| < eps
            break
        x = x - eta * g               # Schritt gegen grad f
        weg.append(x.copy())
    return x, np.array(weg)

f    = lambda x: x[0]**2 + 4*x[1]**2
grad = lambda x: np.array([2*x[0], 8*x[1]])

x, weg = gradientenverfahren(grad, [4.0, 1.0], eta=0.2)
for k, p in enumerate(weg[:4]):
    print(f"k={k}: x=({p[0]:7.4f}, {p[1]:7.4f})  f={f(p):8.4f}")
print(f"{len(weg)-1} Iterationen, x=({x[0]:.1e}, {x[1]:.1e})")
