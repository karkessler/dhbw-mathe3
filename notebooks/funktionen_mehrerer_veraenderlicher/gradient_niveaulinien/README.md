# Gradient und Niveaulinien – Python-Code

Begleitcode zur Präsentation „Gradient, Niveaulinien und Gradientenverfahren“.
Die Präsentation selbst liegt als PDF bei: [`gradient_niveaulinien_praesentation.pdf`](gradient_niveaulinien_praesentation.pdf).

| Datei | Inhalt |
| --- | --- |
| [`gradientenverfahren.py`](gradientenverfahren.py) | Das Gradientenverfahren aus dem Vortrag für $f(x, y) = x^2 + 4y^2$ mit Startwert $(4, 1)$ und $\eta = 0{,}2$; gibt die ersten Iterierten und die Anzahl der Iterationen aus. |
| [`aufgabe_6_4_loesung.py`](aufgabe_6_4_loesung.py) | Musterlösung zu Aufgabe 6.4: Divergenzerkennung, Iterationszahlen für verschiedene Schrittweiten und Wege im Höhenlinienbild. |
| [`grafiken_3d.py`](grafiken_3d.py) | Erzeugt die beiden 3D-Grafiken der Präsentation (Fläche mit Höhenlinien, Weg des Verfahrens auf der Fläche) als SVG und PNG. |

Ausführen (benötigt NumPy und Matplotlib, siehe `requirements.txt` im Hauptverzeichnis):

```bash
python gradientenverfahren.py
python aufgabe_6_4_loesung.py
python grafiken_3d.py
```
