# Apple Human Interface Guidelines: Seiten für Browser-Dialoge

Apple veröffentlicht jede Seite der Human Interface Guidelines auch als Markdown:

```
https://developer.apple.com/design/human-interface-guidelines/<seite>.md
```

Gemessen 02.11.2026: alle Seiten unten antworten mit 200 und `text/markdown`.

**Regeln**

- Laden nur bei Bedarf, eine Seite je Prüfpunkt. Zum Zitieren `curl -s … | grep -n -i <begriff>`;
  WebFetch fasst zusammen und taugt nur zum Überblick.
- Nichts davon ins Repo, in den Bericht oder in ein Ticket kopieren. Zitiert wird sinngemäß und
  kurz, mit dem Link auf die Seite (ohne `.md`, damit Menschen die gewohnte Ansicht sehen).
- Antwortet eine Seite nicht mehr, im Bericht vermerken und ohne sie urteilen; keine Kopie
  aus anderen Quellen nachladen.

## Seiten nach Baugruppe

Der Zweck ist eine eigene Zusammenfassung, wofür die Seite im Review taugt, kein Apple-Text.

### Motor

| Seite | Zweck im Review |
|---|---|
| `feedback` | Arten von Rückmeldung, wo sie hingehört, wann sie stört |
| `loading` | was während des Ladens sichtbar ist, Weiterarbeiten ermöglichen |
| `progress-indicators` | bestimmte gegen unbestimmte Fortschrittsanzeige |
| `motion` | Bewegung mit Zweck, kurz, abschaltbar |

### Fahrwerk

| Seite | Zweck im Review |
|---|---|
| `layout` | Raster, Gruppierung, Ausrichtung, Verhalten bei wechselnder Fensterbreite |
| `sidebars` | Tiefe der Navigation, aktiver Eintrag, ein- und ausblenden |
| `split-views` | Liste neben Detail, Breiten, Auswahl |
| `tab-views` | Reiter innerhalb einer Ansicht |
| `toolbars` | welche Aktionen in die Werkzeugleiste gehören, Gruppierung |
| `lists-and-tables` | Spalten, Sortierung, Auswahl, Bearbeiten in Zeilen |
| `outline-views` | Baumdarstellung, Auf- und Zuklappen |
| `collections` | Kachelansichten, wenn keine Tabelle passt |
| `scroll-views` | Scrollbereiche, verschachteltes Scrollen vermeiden |
| `disclosure-controls` | Weiteres aufklappen statt alles zeigen |
| `entering-data` | Auswahl statt Tippen, Prüfung während der Eingabe |
| `text-fields` | Beschriftung, Platzhalter, Feldbreite, Fehler am Feld |
| `combo-boxes` | Auswahl mit freier Eingabe |
| `pop-up-buttons` | Auswahl aus festen Werten |
| `pickers` | Datum und Wertebereiche |
| `token-fields` | Mehrfachwerte in einem Feld |
| `toggles` | Schalter gegen Kontrollkästchen |
| `segmented-controls` | wenige gleichrangige Optionen |
| `buttons` | Rangfolge, Beschriftung, Standardknopf |
| `menus` | Beschriftung und Reihenfolge von Menüeinträgen |
| `context-menus` | Aktionen per Rechtsklick, nur als Abkürzung |
| `searching` | Suche und Filter, wo sie stehen, was sie zeigen |
| `focus-and-selection` | sichtbarer Fokus, Auswahl, Tastaturbedienung |
| `keyboards` | Tastenkürzel, Standardkürzel nicht umbelegen |
| `pointing-devices` | Hover, Zeiger, Trefferflächen mit der Maus |
| `color` | eine Farbe, eine Bedeutung; Kontrast; Hell und Dunkel |
| `typography` | Schriftgrößen, Hierarchie, Mindestgrößen |
| `accessibility` | Kontrast, Größe der Bedienelemente, nicht nur über Farbe |
| `writing` | Beschriftungen, die sagen, was passiert; einheitliche Schreibweise |
| `labels` | Beschriftungen an Feldern und Werten |
| `icons` | einheitliche Symbolsprache, Beschriftung für Screenreader |
| `charting-data`, `charts` | nur wenn der Dialog Diagramme zeigt |
| `printing` | nur wenn der Dialog druckt oder exportiert |

### Bremse

| Seite | Zweck im Review |
|---|---|
| `undo-and-redo` | Rückgängig statt Rückfrage, wo es geht |
| `alerts` | wann eine Rückfrage gerechtfertigt ist, Knopfbeschriftung, Standardknopf |
| `modality` | Dialoge mit einer Aufgabe und einem klaren Ausweg |
| `sheets` | Dialoge, die an einer Ansicht hängen |
| `popovers` | kleine Zusatzinhalte, wann sie sich schließen |
| `panels` | schwebende Hilfsfenster |
| `file-management` | Hochladen, Speichern, Versionen |
| `managing-accounts` | Anmelden, Sitzung, Abmelden |
| `privacy` | nur so viele Daten wie nötig zeigen |
| `offering-help` | Hilfe am Ort statt im Handbuch |

## Nicht laden für Browser-Dialoge

Seiten zu Geräten und Systemdiensten zählen hier nicht, zum Beispiel `designing-for-ios`,
`tab-bars`, `the-menu-bar`, `liquid-glass`, `materials`, `widgets`, `live-activities`, `apple-pay`,
`gestures`, `playing-haptics`, `app-icons`, `sf-symbols`, `siri`, `game-controls`. Sie bleiben
erreichbar, gehören aber nicht ins Review.

## Übersetzungstafel Apple nach Browser

| Bei Apple | Im Browser allgemein | Zum Beispiel mit PrimeReact |
|---|---|---|
| Fenster | Browser-Tab | Browser-Tab mit dem Dialog |
| Menüleiste | gibt es nicht | gibt es nicht; Aktionen in Werkzeugleiste und Kontextmenü |
| Sidebar | `<nav>` Seitenleiste | `Sidebar`, `PanelMenu` |
| Toolbar | Werkzeugleiste im Kopf | `Toolbar` |
| Sheet, Alert | `<dialog>`, Bestätigungsdialog | PrimeReact `Dialog`, `confirmDialog` |
| Popover | Popover, Tooltip | PrimeReact `OverlayPanel`, `Tooltip` |
| Table, Outline View | `<table>`, Baumtabelle | PrimeReact `DataTable`, `TreeTable` |
| Pop-up Button, Combo Box | `<select>`, Combobox mit Vorschlägen | `Dropdown`, `AutoComplete` |
| Punkt (pt) | CSS-Pixel bei 100 % Zoom | CSS-Pixel bei 100 % Zoom |
| Größen macOS | wie rechts | Bedienelement Standard 28 × 28, mindestens 20 × 20; Text Standard 13, mindestens 10 (Seite `accessibility`, gelesen 02.11.2026) |
