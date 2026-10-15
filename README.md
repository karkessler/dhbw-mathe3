# Angewandte Mathematik

Interaktive Python-/Jupyter-Notebooks als Begleitmaterial zur Vorlesung
**Angewandte Mathematik**. Die Sammlung behandelt nicht nur numerische Verfahren,
sondern auch mathematische Grundlagen, gewöhnliche Differentialgleichungen und
Funktionen mehrerer Veränderlicher.
Die Notebooks verbinden Herleitungen und Beispiele mit symbolischen Kontrollen,
numerischen Experimenten und Visualisierungen.

## Inhalte

### Differentialgleichungen

| Notebook | Inhalt | Statische Version |
| --- | --- | --- |
| [`00_mathematische_grundlagen.ipynb`](notebooks/differentialgleichungen/00_mathematische_grundlagen.ipynb) | Wiederholt partielle Integration und Taylorpolynome und führt über Eigenwerte, Eigenvektoren und Diagonalisierung zur linearen Dynamik. | [`PDF`](notebooks/differentialgleichungen/00_mathematische_grundlagen.pdf) |
| [`01_dgl_variablentrennung_aehnlichkeitsdgl.ipynb`](notebooks/differentialgleichungen/01_dgl_variablentrennung_aehnlichkeitsdgl.ipynb) | Behandelt Anfangswertprobleme am Abkühlungsgesetz, Richtungsfelder, das Euler-Verfahren sowie Variablentrennung und Ähnlichkeitsdifferentialgleichungen. | [`PDF`](notebooks/differentialgleichungen/01_dgl_variablentrennung_richtungsfelder.pdf) |
| [`02_lineare_dgl_resonanz_euler.ipynb`](notebooks/differentialgleichungen/02_lineare_dgl_resonanz_euler.ipynb) | Erklärt lineare Differentialgleichungen erster und zweiter Ordnung, charakteristische Polynome, komplexe Nullstellen, Resonanz und Euler-Differentialgleichungen. | [`PDF`](notebooks/differentialgleichungen/02_lineare_dgl_resonanz_euler.pdf) |
| [`03_dgl_systeme_phasenportrait.ipynb`](notebooks/differentialgleichungen/03_dgl_systeme_phasenportrait.ipynb) | Behandelt lineare Systeme mit Phasenportraits, einem gekoppelten Feder-Masse-System, Normalmoden, Variation der Konstanten und inhomogenen Systemen. | [`PDF`](notebooks/differentialgleichungen/03_dgl_systeme_phasenportrait.pdf) |
| [`04_komplexe_eigenwerte_spiralpunkte.ipynb`](notebooks/differentialgleichungen/04_komplexe_eigenwerte_spiralpunkte.ipynb) | Leitet komplexe Eigenwerte her und veranschaulicht stabile und instabile Spiralpunkte sowie Zentren im Phasenportrait. | [`PDF`](notebooks/differentialgleichungen/04_komplexe_eigenwerte_spiralpunkte.pdf) |

### Funktionen mehrerer Veränderlicher

| Notebook | Inhalt | Statische Version |
| --- | --- | --- |
| [`00_werkzeuge_mehrere_veraenderliche.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/00_werkzeuge_mehrere_veraenderliche.ipynb) | Werkzeuge für Kapitel 2: Funktionen zweier Variablen mit NumPy auswerten, Fläche, Höhenlinien, Farbkarte und Schnitte, Vektoren und Normen, SymPy für Gradient, Jacobi- und Hesse-Matrix. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/00_werkzeuge_mehrere_veraenderliche.pdf) |
| [`01_darstellung_isolinien.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/01_darstellung_isolinien.ipynb) | Abschnitt 2.1: Definition und explizite/implizite Darstellung (Ebene, Kugel), Isoparameterlinien und eingefärbte Höhenlinien, Höhenlinienbilder lesen. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/01_darstellung_isolinien.pdf) |
| [`02_konvergenz_grenzwerte_stetigkeit.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/02_konvergenz_grenzwerte_stetigkeit.ipynb) | Abschnitte 2.2 und 2.3: Konvergenz im ℝⁿ, Grenzwerte und ε-δ-Stetigkeit, unstetige Funktionen und Annäherung auf verschiedenen Wegen, vektorwertige Funktionen, innere Punkte und Randpunkte. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/02_konvergenz_grenzwerte_stetigkeit.pdf) |
| [`03_partielle_ableitungen_gradient_jacobi.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/03_partielle_ableitungen_gradient_jacobi.ipynb) | Abschnitt 2.4: Partielle Ableitungen und Schnittkurven, Gradientenfeld und Höhenlinien, Satz von Schwarz mit Gegenbeispiel, Jacobi-Matrix als lineare Näherung und Kettenregel. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/03_partielle_ableitungen_gradient_jacobi.pdf) |
| [`04_richtungsableitung.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/04_richtungsableitung.ipynb) | Abschnitt 2.5: Richtungsableitung und Satz 2.5.2 (mit Gegenbeispiel ohne C¹), maximale Steigung in Gradientenrichtung, Richtungsableitung über dem Winkel und Gradientenabstieg. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/04_richtungsableitung.pdf) |
| [`05_tangentialebene_totales_differential.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/05_tangentialebene_totales_differential.ipynb) | Abschnitt 2.6: Tangentialebene als lineare Näherung, totales Differential und Fehler der Näherung, Anwendung auf die Fehlerfortpflanzung bei Messwerten. | [`PDF`](notebooks/funktionen_mehrerer_veraenderlicher/05_tangentialebene_totales_differential.pdf) |

### Numerik und Optimierung

| Notebook | Inhalt | Statische Version |
| --- | --- | --- |
| [`00_nullstellenverfahren.ipynb`](notebooks/numerik/00_nullstellenverfahren.ipynb) | Stellt Bisektion und Newton-Verfahren gegenüber und veranschaulicht lineare beziehungsweise quadratische Konvergenz. | [`PDF`](notebooks/numerik/00_nullstellenverfahren.pdf) |
| [`01_numerische_integration.ipynb`](notebooks/numerik/01_numerische_integration.ipynb) | Vergleicht Trapez- und Simpson-Regel an einem Integral mit bekanntem Wert und macht ihre Konvergenzordnungen sichtbar. | [`PDF`](notebooks/numerik/01_numerische_integration.pdf) |
| [`02_dgl_numerisch.ipynb`](notebooks/numerik/02_dgl_numerisch.ipynb) | Vergleicht das explizite Euler-Verfahren mit Runge-Kutta 4 für ein Anfangswertproblem; Genauigkeit, Schrittweite und Stabilität stehen im Mittelpunkt. | [`PDF`](notebooks/numerik/02_dgl_numerisch.pdf) |
| [`03_schwingungsdifferentialgleichung.ipynb`](notebooks/numerik/03_schwingungsdifferentialgleichung.ipynb) | Modelliert ein Feder-Masse-System analytisch und mit Runge-Kutta 4 und stellt ungedämpfte und gedämpfte Schwingungen gegenüber. | [`PDF`](notebooks/numerik/03_schwingungsdifferentialgleichung.pdf) |
| [`04_gradient_descent_1d.ipynb`](notebooks/numerik/04_gradient_descent_1d.ipynb) | Rechnet den Gradientenabstieg für eine eindimensionale quadratische Funktion Schritt für Schritt nach und visualisiert Iterationen, Tangenten und Schrittweiten. | [`PDF`](notebooks/numerik/04_gradient_descent_1d.pdf) |
| [`05_gradient_descent_rosenbrock.ipynb`](notebooks/numerik/05_gradient_descent_rosenbrock.ipynb) | Überträgt den Gradientenabstieg auf die Rosenbrock-Funktion und zeigt den Einfluss der Lernrate sowie die Grenzen des Verfahrens. | [`PDF`](notebooks/numerik/05_gradient_descent_rosenbrock.pdf) |

## Voraussetzungen und Ausführung

Benötigt werden Python 3 sowie die in [`requirements.txt`](requirements.txt)
aufgeführten Pakete: NumPy, Matplotlib, SymPy, ipywidgets und SciPy.

```bash
python -m pip install -r requirements.txt
jupyter notebook notebooks/
```

Die Zellen eines Notebooks sollten in ihrer Reihenfolge ausgeführt werden. Viele
Beispiele prüfen Rechenschritte direkt im Notebook oder machen Eigenschaften der
Verfahren anhand von Plots sichtbar. Jedes Notebook lässt sich außerdem über den
jeweiligen **Open in Colab**-Link ohne lokale Installation starten.

## Statische Versionen (PDF)

Zu jedem Notebook liegt eine exportierte PDF-Version ohne Python-Code vor. Sie enthält
die formatierten Formeln, Ausgaben und Grafiken und kann direkt auf GitHub oder in
einem PDF-Betrachter geöffnet werden.

Mit dem Skript `python generate_pdfs.py` können die PDF-Dateien bei Bedarf jederzeit
automatisch neu generiert werden.

## Weiterführendes Material

Das Gradientenabstiegsverfahren wird auch im Kontext des Trainings neuronaler
Netze behandelt:

Keßler, K. (2025).<br>
*LLM für den Hausgebrauch – Notebooks und Materialien.*<br>
GitHub: https://github.com/karkessler/llm-hausgebrauch<br>
Web: https://tutor.kkessler.de/llm
