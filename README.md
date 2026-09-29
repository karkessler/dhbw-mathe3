# DHBW Angewandte Mathematik

Interaktive Python-/Jupyter-Notebooks als Begleitmaterial zur Vorlesung
**Angewandte Mathematik**. Die Sammlung behandelt nicht nur numerische Verfahren,
sondern auch mathematische Grundlagen und gewöhnliche Differentialgleichungen.
Die Notebooks verbinden Herleitungen und Beispiele mit symbolischen Kontrollen,
numerischen Experimenten und Visualisierungen.

## Inhalte

### Differentialgleichungen

| Notebook | Inhalt |
| --- | --- |
| [`00_mathematische_grundlagen.ipynb`](notebooks/differentialgleichungen/00_mathematische_grundlagen.ipynb) | Wiederholt partielle Integration und Taylorpolynome und führt über Eigenwerte, Eigenvektoren und Diagonalisierung zur linearen Dynamik. |
| [`01_dgl_variablentrennung_richtungsfelder.ipynb`](notebooks/differentialgleichungen/01_dgl_variablentrennung_richtungsfelder.ipynb) | Behandelt Anfangswertprobleme am Abkühlungsgesetz, Richtungsfelder, das Euler-Verfahren sowie Variablentrennung und homogene Differentialgleichungen. |
| [`02_lineare_dgl_resonanz_euler.ipynb`](notebooks/differentialgleichungen/02_lineare_dgl_resonanz_euler.ipynb) | Erklärt lineare Differentialgleichungen erster und zweiter Ordnung, charakteristische Polynome, komplexe Nullstellen, Resonanz und Euler-Differentialgleichungen. |
| [`03_dgl_systeme_phasenportrait.ipynb`](notebooks/differentialgleichungen/03_dgl_systeme_phasenportrait.ipynb) | Formt höhere Differentialgleichungen in Systeme erster Ordnung um und untersucht Fundamentalmatrix, Phasenportraits, Stabilität und inhomogene Systeme. |

### Numerik und Optimierung

| Notebook | Inhalt |
| --- | --- |
| [`numerische_integration.ipynb`](notebooks/numerik/numerische_integration.ipynb) | Vergleicht Trapez- und Simpson-Regel an einem Integral mit bekanntem Wert und macht ihre Konvergenzordnungen sichtbar. |
| [`dgl_numerisch.ipynb`](notebooks/numerik/dgl_numerisch.ipynb) | Vergleicht das explizite Euler-Verfahren mit Runge-Kutta 4 für ein Anfangswertproblem; Genauigkeit, Schrittweite und Stabilität stehen im Mittelpunkt. |
| [`schwingungsdifferentialgleichung.ipynb`](notebooks/numerik/schwingungsdifferentialgleichung.ipynb) | Modelliert ein Feder-Masse-System analytisch und mit Runge-Kutta 4 und stellt ungedämpfte und gedämpfte Schwingungen gegenüber. |
| [`nullstellenverfahren.ipynb`](notebooks/numerik/nullstellenverfahren.ipynb) | Stellt Bisektion und Newton-Verfahren gegenüber und veranschaulicht lineare beziehungsweise quadratische Konvergenz. |
| [`gradient_descent_1d.ipynb`](notebooks/numerik/gradient_descent_1d.ipynb) | Rechnet den Gradientenabstieg für eine eindimensionale quadratische Funktion Schritt für Schritt nach und visualisiert Iterationen, Tangenten und Schrittweiten. |
| [`gradient_descent_rosenbrock.ipynb`](notebooks/numerik/gradient_descent_rosenbrock.ipynb) | Überträgt den Gradientenabstieg auf die Rosenbrock-Funktion und zeigt den Einfluss der Lernrate sowie die Grenzen des Verfahrens. |

## Voraussetzungen und Ausführung

Benötigt werden Python 3 sowie die in [`requirements.txt`](requirements.txt)
aufgeführten Pakete: NumPy, Matplotlib, SymPy und ipywidgets.

```bash
python -m pip install -r requirements.txt
jupyter notebook notebooks/
```

Die Zellen eines Notebooks sollten in ihrer Reihenfolge ausgeführt werden. Viele
Beispiele prüfen Rechenschritte direkt im Notebook oder machen Eigenschaften der
Verfahren anhand von Plots sichtbar. Jedes Notebook lässt sich außerdem über den
jeweiligen **Open in Colab**-Link ohne lokale Installation starten.

## Weiterführendes Material

Das Gradientenabstiegsverfahren wird auch im Kontext des Trainings neuronaler
Netze behandelt:

Keßler, K. (2025).<br>
*LLM für den Hausgebrauch – Notebooks und Materialien.*<br>
GitHub: https://github.com/karkessler/llm-hausgebrauch<br>
Web: https://tutor.kkessler.de/llm
