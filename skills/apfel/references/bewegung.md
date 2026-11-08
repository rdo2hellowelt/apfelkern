# Rückmeldung und Bewegung

Verdichtet und übersetzt aus zwei Skills im Repo `emilkowalski/skills` (Emil Kowalski, MIT, Stand
der Kopie `70744e3`): `emil-design-eng` und `apple-design`. Übernommen ist nur, was in einem
Arbeitsdialog zählt. Ausgelassen sind Gesten, Federphysik, Schwung, 3D, Bildeffekte, Materialien.

## §1 Sofort antworten

- Rückmeldung beim Drücken, nicht erst beim Loslassen: `:active` mit leichter Skalierung (0.97)
  oder Farbwechsel, Übergang 100 bis 160 ms.
- Jede Wartezeit auf dem Eingabeweg prüfen: Debounce, künstliche Timer, Warten auf das Ende einer
  Animation. Was nicht nötig ist, ist ein Rückschritt.
- Während Ziehen, Schieberegler, Spaltenbreite: die Oberfläche folgt 1:1, nicht erst am Ende.

## §2 Ob überhaupt animieren

- Aktionen, die hundertmal am Tag passieren (Tastaturkürzel, Tabellenwechsel, Speichern), bekommen
  keine Animation.
- Animation braucht einen Zweck: Herkunft zeigen (Popover aus seinem Auslöser), Zustand wechseln,
  Aufmerksamkeit auf eine Meldung lenken.

## §3 Wie schnell, welche Kurve

| Element | Dauer |
|---|---|
| Rückmeldung am Knopf | 100 bis 160 ms |
| Tooltip, kleines Popover | 125 bis 200 ms |
| Dropdown, Auswahl | 150 bis 250 ms |
| Dialog, Schublade | 200 bis 300 ms |

- Nichts in einem Arbeitsdialog dauert länger als 300 ms.
- Hereinkommen mit `ease-out`, nie `ease-in` (wirkt träge).
- Popover wachsen aus ihrem Auslöser (`transform-origin`), Dialoge bleiben mittig.
- Nie aus `scale(0)`; ab 0.95 mit Deckkraft 0.
- Hinausgehen darf schneller sein als Hereinkommen.
- Tooltip: nach dem ersten ohne Verzögerung und ohne Animation.

## §4 Technik und Zugänglichkeit

- Nur `transform` und `opacity` animieren; nie `transition: all`.
- CSS-Übergänge statt Keyframes bei Elementen, die schnell hintereinander ausgelöst werden; sie
  lassen sich unterbrechen.
- Hover-Effekte nur unter `@media (hover: hover) and (pointer: fine)`.
- `prefers-reduced-motion`: Bewegung durch Überblenden ersetzen oder weglassen; Bedeutung nie nur
  über Bewegung.

## §5 Grundsätze aus `apple-design` (in eigenen Worten)

- Wegfindung: Jede Ansicht beantwortet, wo ich bin, wohin ich kann, was da ist, wie ich herauskomme.
- Nähe heißt Zusammengehörigkeit: Bedienelement neben das, was es ändert.
- Klare, spezifische Beschriftung schlägt eine vorsichtige allgemeine.
- Nachsicht: Rückgängig für Ausrutscher, Rückfrage nur bei Unumkehrbarem, sparsam, sonst klickt man
  sie weg.
- Rückmeldung in vier Arten: Status, Abschluss, Warnung, Fehler; Prüfung während der Eingabe, nicht
  erst beim Absenden.
