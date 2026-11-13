# Quellen

| Quelle | Stand | Lizenz | Was davon hier steht |
|---|---|---|---|
| Apple Human Interface Guidelines, https://developer.apple.com/design/human-interface-guidelines/ | live, je Seite als `<seite>.md` | Apple, keine Weitergabe-Lizenz | nur Seitennamen und ein eigener Satz zum Zweck (`references/hig-seiten.md`); Inhalt wird bei Bedarf geladen, nie abgelegt |
| taste-skill, https://github.com/Leonxlnx/taste-skill | `12af471`, 25.10.2026 | MIT, `LICENSES/MIT-leonxlnx-taste-skill.txt` | Regeln aus `references/app-screens.md` §7, 8, 10, 11, 13, 14, verdichtet und übersetzt (`references/arbeitsmasken.md`) |
| emilkowalski/skills, https://github.com/emilkowalski/skills | `70744e3`, 27.07.2026 | MIT, `LICENSES/MIT-emilkowalski-skills.txt` | Regeln aus `emil-design-eng` und `apple-design`, verdichtet und übersetzt (`references/bewegung.md`) |
| dimensional-drawing, https://github.com/enesozturk/dimensional-drawing | Zip des Hauptzweigs, 07.11.2026, ohne Commit-Angabe | MIT, `LICENSES/MIT-enesozturk-dimensional-drawing.txt` | Zeichenstil (Grau, Strichsprache, Ansichten, Kopf) und Zeichenwerkzeug aus `examples/dialog-sheet.html`, angepasst an Befunde statt Maße; seit 1.1.0 über Birne (`skills/birne`) |

## Bewusst nicht übernommen

- **apple-design-skill** (https://github.com/dickwu/apple-design-skill @ `ff4ebdd`): enthält 124
  HIG-Seiten im Wortlaut und eine eigene Anleitung, ohne Lizenzdatei. Weder die Seiten noch die
  Anleitung stehen hier. Die Idee, je Prüfpunkt die passende HIG-Seite zu nennen, ist umgesetzt,
  die Seiten kommen live von Apple.
- **Skripte aus taste-skill** (`scripts/`, darunter `assets.mjs`, das Bilder aus dem Netz lädt, und
  `inspect.mjs`, das einen Browser steuert): nicht übernommen. Der Skill führt nichts aus dem Netz
  aus.
- **Aus dimensional-drawing:** der Teil für Filme (`dimensional-drawing-motion`, mit Playwright, ffmpeg und npm)
  und die Tabellen mit Maßvariablen. Befunde haben keine Maße, und der Skill führt nichts aus dem Netz aus.
- **Bibliothek aus taste-skill** (`library/*.json`, Paletten, Schriften, Landingpage-Muster): für
  Arbeitsdialoge ohne Nutzen.

## Änderungen

- **13.11.2026, Apfel trägt Birne (1.1.0):** Das Plugin bringt Birne als `skills/birne` mit, Datei für Datei gleich
  mit https://github.com/rdo2hellowelt/birnenkern. Die Befundzeichnung baut auf Birnes Blatt (Rahmen mit Zonen,
  Schriftfeld unten rechts, Blocksatz); `assets/zeichnung-vorlage.html` ist entfallen, es gibt nur noch ein Blatt.
  Birne wird nur in birnenkern geändert und hier nachgezogen:
  `rsync -a --delete ../birnenkern/skills/birne/ skills/birne/`, dann `diff -r ../birnenkern/skills/birne skills/birne`.
- **08.11.2026, Kern und Profile getrennt:** Eigene Profile liegen jetzt in `~/Documents/Apfel/profile/`,
  nicht mehr im Skill; mitgeliefert sind nur `vorlage.md` und das erfundene `beispiel.md`. Skripte
  werden über `<skill>` aufgerufen, den Basisordner, den Claude Code beim Laden nennt, damit Apfel als
  Skill und als Plugin gleich läuft. Eigene Lizenz MIT (`LICENSE`).
  Musterzeichnung und Prüffälle auf ein erfundenes Projekt umgestellt (Kundenkartei).
- **08.11.2026, Profil-Werkzeug:** Profile für Projekte ohne Git und mit eigenem Hausstil erprobt.
- **08.11.2026, Erklärblatt und Ordner:** Ergebnisse und Probeläufe nach `~/Documents/Apfel/`, nicht
  mehr im Repo. Neu „apfel erklären“ (§7): `scripts/erklaeren.py` baut aus `SKILL.md` und
  `assets/erklaer-vorlage.html` ein Erklärblatt.
- **07.11.2026, Befundzeichnung:** Bericht auf Wunsch als technisches Blatt (`assets/zeichnung-vorlage.html`,
  §5). Auslöser „apfel zeichnung“.
- **07.11.2026, Profile:** Profile als zweiter Baustein, mit Steckbrief, Fundort `.apfel/profil.md` im
  geprüften Repo, Untermenü „apfel profil“ und `scripts/profil_pruefen.py`. Dazu „apfel kurz“, bei
  Zweig oder Merge Request nur die geänderte Oberfläche, Hinweise für Windows. Probeläufe in frischer
  Sitzung; danach die Regel „Befehle so, dass die Freigaben greifen“.
- **03.11.2026, erste Fassung:** Prüfpunkte in drei Baugruppen, drei Stände mit Rangfolge, Zitate aus
  den HIG nur über `curl`, `scripts/kontrast.py` und `evals/evals.json`.
