# DHBW Mathe 3

Begleitmaterial (Python/Jupyter) zur Vorlesung Numerische Mathematik 3.

## Notebooks

Alle Notebooks liegen in `notebooks/numerik/` und orientieren sich an der Gliederung
"4. Numerik" der Vorlesung:

- [`numerische_integration.ipynb`](notebooks/numerik/numerische_integration.ipynb) (4.1):
  Trapez- und Simpson-Regel, Konvergenzordnung im Vergleich.
- [`dgl_numerisch.ipynb`](notebooks/numerik/dgl_numerisch.ipynb) (4.2):
  Explizites Euler-Verfahren und Runge-Kutta 4, Stabilität und Konvergenzordnung.
- [`schwingungsdifferentialgleichung.ipynb`](notebooks/numerik/schwingungsdifferentialgleichung.ipynb) (4.2):
  Feder-Masse-Oszillator analytisch und mit Runge-Kutta 4; Vergleich von ungedämpfter und
  gedämpfter Schwingung.
- [`nullstellenverfahren.ipynb`](notebooks/numerik/nullstellenverfahren.ipynb) (4.3):
  Bisektion und Newton-Verfahren, lineare vs. quadratische Konvergenz.
- [`gradient_descent_1d.ipynb`](notebooks/numerik/gradient_descent_1d.ipynb) (4.4):
  Gradientenabstiegsverfahren, Skriptbeispiel $f(x)=x^2-2x+3$ von Hand nachgerechnet
  (Iterationsfolge, Tangenten-Plot, Schrittweiten-Variation langsam/Skript/oszillierend/divergent).
- [`gradient_descent_rosenbrock.ipynb`](notebooks/numerik/gradient_descent_rosenbrock.ipynb) (4.4):
  Dieselbe Methode als 2D-Erweiterung, demonstriert an der Rosenbrock-Funktion (Konvergenzverhalten,
  Einfluss der Schrittweite, Ausblick auf das Newton-Verfahren).

## Ausführen

```bash
pip install -r requirements.txt
jupyter notebook notebooks/
```

Oder direkt über den "Open in Colab"-Link im jeweiligen Notebook.

## Verwandtes Material

Das Gradientenabstiegsverfahren (4.4) wird dort auch im Kontext des Trainings neuronaler
Netze behandelt:

Keßler, K. (2025).
*LLM für den Hausgebrauch – Notebooks und Materialien.*
GitHub: https://github.com/karkessler/llm-hausgebrauch
Web: https://tutor.kkessler.de/llm
DOI: https://doi.org/10.5281/zenodo.18293327
