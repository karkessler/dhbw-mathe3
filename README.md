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
| [`00_mathematische_grundlagen.ipynb`](notebooks/differentialgleichungen/00_mathematische_grundlagen.ipynb) | Wiederholt partielle Integration und Taylorpolynome und führt über Eigenwerte, Eigenvektoren und Diagonalisierung zur linearen Dynamik. | [`HTML`](notebooks/differentialgleichungen/00_mathematische_grundlagen.html) |
| [`01_dgl_variablentrennung_aehnlichkeitsdgl.ipynb`](notebooks/differentialgleichungen/01_dgl_variablentrennung_aehnlichkeitsdgl.ipynb) | Behandelt Anfangswertprobleme am Abkühlungsgesetz, Richtungsfelder, das Euler-Verfahren sowie Variablentrennung und Ähnlichkeitsdifferentialgleichungen. | [`HTML`](notebooks/differentialgleichungen/01_dgl_variablentrennung_richtungsfelder.html) |
| [`02_lineare_dgl_resonanz_euler.ipynb`](notebooks/differentialgleichungen/02_lineare_dgl_resonanz_euler.ipynb) | Erklärt lineare Differentialgleichungen erster und zweiter Ordnung, charakteristische Polynome, komplexe Nullstellen, Resonanz und Euler-Differentialgleichungen. | [`HTML`](notebooks/differentialgleichungen/02_lineare_dgl_resonanz_euler.html) |
| [`03_dgl_systeme_phasenportrait.ipynb`](notebooks/differentialgleichungen/03_dgl_systeme_phasenportrait.ipynb) | Behandelt lineare Systeme mit Phasenportraits, einem gekoppelten Feder-Masse-System, Normalmoden, Variation der Konstanten und inhomogenen Systemen. | [`HTML`](notebooks/differentialgleichungen/03_dgl_systeme_phasenportrait.html) |
| [`04_komplexe_eigenwerte_spiralpunkte.ipynb`](notebooks/differentialgleichungen/04_komplexe_eigenwerte_spiralpunkte.ipynb) | Leitet komplexe Eigenwerte her und veranschaulicht stabile und instabile Spiralpunkte sowie Zentren im Phasenportrait. | [`HTML`](notebooks/differentialgleichungen/04_komplexe_eigenwerte_spiralpunkte.html) |

### Funktionen mehrerer Veränderlicher

| Notebook | Inhalt | Statische Version |
| --- | --- | --- |
| [`00_werkzeuge_mehrere_veraenderliche.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/00_werkzeuge_mehrere_veraenderliche.ipynb) | Werkzeuge für Kapitel 2: Funktionen zweier Variablen mit NumPy auswerten, Fläche, Höhenlinien, Farbkarte und Schnitte, Vektoren und Normen, SymPy für Gradient, Jacobi- und Hesse-Matrix. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/00_werkzeuge_mehrere_veraenderliche.html) |
| [`01_darstellung_isolinien.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/01_darstellung_isolinien.ipynb) | Abschnitt 2.1: Definition und explizite/implizite Darstellung (Ebene, Kugel), Isoparameterlinien und eingefärbte Höhenlinien, Höhenlinienbilder lesen. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/01_darstellung_isolinien.html) |
| [`02_konvergenz_grenzwerte_stetigkeit.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/02_konvergenz_grenzwerte_stetigkeit.ipynb) | Abschnitte 2.2 und 2.3: Konvergenz im ℝⁿ, Grenzwerte und ε-δ-Stetigkeit, unstetige Funktionen und Annäherung auf verschiedenen Wegen, vektorwertige Funktionen, innere Punkte und Randpunkte. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/02_konvergenz_grenzwerte_stetigkeit.html) |
| [`03_partielle_ableitungen_gradient_jacobi.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/03_partielle_ableitungen_gradient_jacobi.ipynb) | Abschnitt 2.4: Partielle Ableitungen und Schnittkurven, Gradientenfeld und Höhenlinien, Satz von Schwarz mit Gegenbeispiel, Jacobi-Matrix als lineare Näherung und Kettenregel. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/03_partielle_ableitungen_gradient_jacobi.html) |
| [`04_richtungsableitung.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/04_richtungsableitung.ipynb) | Abschnitt 2.5: Richtungsableitung und Satz 2.5.2 (mit Gegenbeispiel ohne C¹), maximale Steigung in Gradientenrichtung, Richtungsableitung über dem Winkel und Gradientenabstieg. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/04_richtungsableitung.html) |
| [`05_tangentialebene_totales_differential.ipynb`](notebooks/funktionen_mehrerer_veraenderlicher/05_tangentialebene_totales_differential.ipynb) | Abschnitt 2.6: Tangentialebene als lineare Näherung, totales Differential und Fehler der Näherung, Anwendung auf die Fehlerfortpflanzung bei Messwerten. | [`HTML`](notebooks/funktionen_mehrerer_veraenderlicher/05_tangentialebene_totales_differential.html) |

### Numerik und Optimierung

| Notebook | Inhalt | Statische Version |
| --- | --- | --- |
| [`00_nullstellenverfahren.ipynb`](notebooks/numerik/00_nullstellenverfahren.ipynb) | Stellt Bisektion und Newton-Verfahren gegenüber und veranschaulicht lineare beziehungsweise quadratische Konvergenz. | [`HTML`](notebooks/numerik/00_nullstellenverfahren.html) |
| [`01_numerische_integration.ipynb`](notebooks/numerik/01_numerische_integration.ipynb) | Vergleicht Trapez- und Simpson-Regel an einem Integral mit bekanntem Wert und macht ihre Konvergenzordnungen sichtbar. | [`HTML`](notebooks/numerik/01_numerische_integration.html) |
| [`02_dgl_numerisch.ipynb`](notebooks/numerik/02_dgl_numerisch.ipynb) | Vergleicht das explizite Euler-Verfahren mit Runge-Kutta 4 für ein Anfangswertproblem; Genauigkeit, Schrittweite und Stabilität stehen im Mittelpunkt. | [`HTML`](notebooks/numerik/02_dgl_numerisch.html) |
| [`03_schwingungsdifferentialgleichung.ipynb`](notebooks/numerik/03_schwingungsdifferentialgleichung.ipynb) | Modelliert ein Feder-Masse-System analytisch und mit Runge-Kutta 4 und stellt ungedämpfte und gedämpfte Schwingungen gegenüber. | [`HTML`](notebooks/numerik/03_schwingungsdifferentialgleichung.html) |
| [`04_gradient_descent_1d.ipynb`](notebooks/numerik/04_gradient_descent_1d.ipynb) | Rechnet den Gradientenabstieg für eine eindimensionale quadratische Funktion Schritt für Schritt nach und visualisiert Iterationen, Tangenten und Schrittweiten. | [`HTML`](notebooks/numerik/04_gradient_descent_1d.html) |
| [`05_gradient_descent_rosenbrock.ipynb`](notebooks/numerik/05_gradient_descent_rosenbrock.ipynb) | Überträgt den Gradientenabstieg auf die Rosenbrock-Funktion und zeigt den Einfluss der Lernrate sowie die Grenzen des Verfahrens. | [`HTML`](notebooks/numerik/05_gradient_descent_rosenbrock.html) |

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

## Statische HTML-Versionen und PDF

Zu jedem Notebook liegt eine HTML-Version ohne Python-Code vor. Sie enthält die
gespeicherten Formeln, Ausgaben und Grafiken und kann direkt im Browser geöffnet
werden. Für eine PDF-Datei die HTML-Version im Browser öffnen und über
**Drucken → Als PDF speichern** exportieren.

## Weiterführendes Material

Das Gradientenabstiegsverfahren wird auch im Kontext des Trainings neuronaler
Netze behandelt:

Keßler, K. (2025).<br>
*LLM für den Hausgebrauch – Notebooks und Materialien.*<br>
GitHub: https://github.com/karkessler/llm-hausgebrauch<br>
Web: https://tutor.kkessler.de/llm
