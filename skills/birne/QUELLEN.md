# Quellen

| Was | Herkunft | Lizenz |
|---|---|---|
| Block WERKZEUG in `assets/blatt-vorlage.html` | nach „dimensional-drawing“ von Enes Ozturk, https://github.com/enesozturk/dimensional-drawing, über den Skill apfel (Befundzeichnung seit 07.11.2026) | MIT, `LICENSES/MIT-enesozturk-dimensional-drawing.txt` |
| Block BLATT, Rahmen, Schriftfeld, Legende, Blocksatz, Tusche | eigen, 13.11.2026 | MIT, `LICENSE` |
| Normen in `references/din.md` | DIN EN ISO 5457, 7200, 128, 3098, DIN 1451, nur sinngemäß | |

## Kopie in Apfel

Das Plugin apfel (https://github.com/rdo2hellowelt/apfelkern) trägt diesen Ordner als `skills/birne`, Datei für Datei
gleich. Geändert wird nur hier. Danach im Ordner apfelkern nachziehen und prüfen:

```sh
rsync -a --delete ../birnenkern/skills/birne/ skills/birne/
diff -r ../birnenkern/skills/birne skills/birne && echo gleich
```

## Änderungen

- **13.11.2026, 1.1.0.** `sprache('en')` für englische Blätter: Hinweise, Allgemeine Hinweise und Schriftfeld.
  Prüffälle in `evals/evals.json`. Ungenutztes CSS aus Apfels früherem HTML-Kopf entfernt. Interne Unterlagen heißen
  in der Tabelle Quellen „intern“. Icon für das Plugin (`.claude-plugin/icon.png`).
- **13.11.2026, veröffentlicht als birnenkern 1.0.0.** Muster auf eine erfundene Probe umgestellt (Ausleihe einer
  Stadtbibliothek), Links auf example.org. Schriftfeld ohne voreingestellte Abteilung, die Marke kommt über `abt`.
  Apfel trägt eine Kopie und zeichnet seine Befunde damit, statt eines eigenen Blatts.
- **13.11.2026, angelegt.** Stil: keine Rundungen, Kanten leicht überzeichnet, dünne Linien, Blocksatz, Rahmen mit
  Zonen, kleines Schriftfeld unten rechts statt Kopf oben, eher Maschinenbau, Architektur, Elektro als Werkplan.
  Eigenes Paket neben Apfel.
