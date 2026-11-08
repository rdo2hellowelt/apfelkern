# apfelkern

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  ●  APFEL                                              Zeichnung Nr. APF-01  │
│     prüft Arbeitsdialoge gegen Apples Gestaltungsregeln, live.     Rev A     │
├──────────────┬──────────────┬──────────────┬─────────────────────────────────┤
│  MOTOR    8  │  FAHRWERK 15 │  BREMSE   10 │  33 Prüfpunkte · 6 Regeln       │
│  Tempo       │  Navigation  │  Ungespei-   │  3 Stände: Bestand · Haus 1:1   │
│  Latenz      │  Layout      │  chertes     │            · plus               │
│  Rückmeldung │  Formulare   │  Rückgängig  │  Maßstab: dein Profil           │
├──────────────┴──────────────┴──────────────┴─────────────────────────────────┤
│  Nicht vom Bildschirm messen. Jeder Befund hat eine Fundstelle. Türlich.     │
└──────────────────────────────────────────────────────────────────────────────┘
```

![Lizenz MIT](https://img.shields.io/badge/Lizenz-MIT-111?style=flat-square)
![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-111?style=flat-square)
![Python 3, nur Standardbibliothek](https://img.shields.io/badge/Python_3-nur_Standardbibliothek-111?style=flat-square)
![Abhängigkeiten 0](https://img.shields.io/badge/Abh%C3%A4ngigkeiten-0-111?style=flat-square)

**Apfel ist ein Claude-Code-Skill, der Browser-Dialoge prüft, in denen Menschen arbeiten:** Masken,
Tabellen, Formulare, Speichern. Kein Geschmacksgutachten, sondern ein Prüfstand. Jeder Befund ist
nachprüfbar, im Code oder im Klickweg, und nennt seine Quelle: die Zeile im Code, die Seite bei
Apple, das Vorbild im eigenen Haus.

> „12 px #999 auf Weiß, 2,85:1“ statt „schlecht lesbar“.
> Zahl statt Adjektiv. Das ist der ganze Trick.

---

## Was er prüft

Ein Dialog ist ein Auto. Man prüft nicht, ob der Lack gefällt, sondern ob es fährt, lenkt und
bremst.

| Baugruppe | Fragt | Zum Beispiel |
|---|---|---|
| **Motor** · 8 | Reagiert der Dialog sofort? | Ladezustand am Knopf, Platzhalter statt Springen, keine künstlichen Wartezeiten, Animationen ≤ 300 ms |
| **Fahrwerk** · 15 | Findet man sich zurecht? | Seitenleiste, Feldteilung, Auswahl statt Tippen, Zahlen rechtsbündig, Kontrast ≥ 4,5:1, Fokus sichtbar |
| **Bremse** · 10 | Geht Arbeit verloren? | Jeder Weg aus ungespeicherten Änderungen fragt, Rückfragen nur für Unumkehrbares, Fehler als Satz statt Antwortrumpf |

Die Bremse kommt zuerst. Verlorene Arbeit wiegt schwerer als ein ruckelnder Knopf.

## Drei Stände nebeneinander

Jede Station des Dialogs kommt als **Kontaktabzug**, wie ein Bogen beim Fotografen:

```text
 Bestand             │ Haus 1:1                      │ plus · Bremse, Fahrwerk
 ────────────────────┼───────────────────────────────┼─────────────────────────
 der alte Dialog,    │ dieselbe Funktion im Bild     │ Haus 1:1 mit Kür,
 wie er heute läuft  │ des Hausmaßstabs, ohne Zusatz │ Aufwand S · M · L
```

Was in **Haus 1:1** gehört, entscheidet eine feste Rangfolge aus sechs Regeln, nicht das
Bauchgefühl. Funktion folgt dem Bestand, Bild folgt dem Hausmaßstab, alles darüber hinaus ist Kür.
Ist es unklar, steht dort „Entscheidung“, mit beiden Fundstellen, und das Team entscheidet.

## So sieht ein Befund aus

| Nr | Baugruppe | Bestand | Haus 1:1 | plus | Aufwand | Fundstelle Code | HIG-Seite |
|---|---|---|---|---|---|---|---|
| 1 | Bremse | fragt beim Verlassen | Seitenleiste verlässt ohne Rückfrage. Regel 1, Schutz wie `HAUS:bausteine/useVerlassenSchutz.ts` | wie Haus 1:1 | S | `NEU:src/dialoge/auftrag/Auftrag.tsx` | feedback |
| 2 | Fahrwerk | neu | wie Bestand | Gesamtzahl über der Tabelle, tief hängend, Arbeitsmasken §2 | S | `NEU:src/dialoge/auftrag/Liste.tsx` | lists-and-tables |

Aus der erfundenen Kundenkartei, die als Beispiel mitkommt (`skills/apfel/profile/beispiel.md`).

## Befehle

| Du tippst | Apfel macht |
|---|---|
| `apfel` | Begrüßung und Menü: bekanntes Projekt, eigenes Projekt, Profile, Auf gut Glück |
| `apfel <dialog>` | voller Review mit Kontaktabzug je Station |
| `apfel kurz <dialog>` | nur Urteil, Zahlen und die drei wichtigsten Vorschläge |
| `apfel zeichnung <dialog>` | Review plus **Befundzeichnung**: ein Blatt wie eine technische Maßzeichnung, mit Draufsicht, Explosionsansicht, Schnitt und Details |
| `apfel profil` | Profile ansehen, anlegen, prüfen, tauschen |
| `apfel erklären` | baut aus `SKILL.md` eine Seite, die zeigt, wie Apfel arbeitet |
| `apfel verbessern` | schlägt Änderungen am Skill vor, aus dem, was im Lauf auffiel |

Aufnahmen vom Dialog einfach ins Terminal ziehen, dann urteilt Apfel auch nach dem Bild. Ohne
Aufnahmen läuft er „nur Code“ und sammelt, was nur am laufenden Dialog zu sehen ist, unter
**Offen für den Klickweg**.

## Profile: der Maßstab deines Hauses

Apples Regeln gelten für alle. Was in deinem Projekt gilt, steht im **Profil**: eine
Markdown-Datei mit Vorbild-Dialog, Grenzen und je Thema einer Fundstelle („so speichert unser
Adressdialog“). 15 Grundthemen, eigene dürfen dazu.

```text
apfel profil → Neu anlegen → vier Fragen → Apfel sucht die Fundstellen selbst
             → zeigt das Profil → legt es erst nach einem Ja ab → prüft es
```

- **Eigene Profile** liegen in `~/Documents/Apfel/profile/`, nicht im Skill. Sie bleiben privat und
  überleben jedes Update.
- **Im Team:** `.apfel/profil.md` ins Projekt-Repo legen. Dann gilt für alle derselbe Maßstab, und
  Änderungen laufen über Merge Requests wie jeder andere Code.
- **Ohne Profil** prüft Apfel trotzdem, dann gegen Apples Regeln und die eigenen Prüfpunkte, und
  fragt einmal, ob es ein Vorbild gibt.
- `scripts/profil_pruefen.py` sagt, ob jede Fundstelle auf dem Ref noch existiert. Profile altern,
  Dateien wandern.

## Haltung

- **Nur lesen.** Apfel ändert keinen Code im geprüften Projekt. Kein Auschecken, kein Installieren,
  keine Skripte des Projekts.
- **Apple live, nie kopiert.** Jede Seite der Human Interface Guidelines wird bei Bedarf als
  Markdown von developer.apple.com geladen und im Wortlaut gelesen, nie abgelegt. Im Repo stehen
  nur Seitennamen.
- **Apple übersetzt, nicht übernommen.** Die HIG sprechen von macOS und iOS. Eine
  Übersetzungstafel sagt, was davon im Browser gilt. Liquid Glass bleibt draußen.
- **Nichts aus dem Netz ausführen.** Die Skripte sind lokal, nur Python-Standardbibliothek.
- **Nicht übertreiben.** Ein guter Dialog bekommt einen kurzen Bericht. Zwanzig Befunde sind kein
  Ziel.

## Installieren

**Als Plugin** (empfohlen, mit Updates), in Claude Code:

```text
/plugin marketplace add rdo2hellowelt/apfelkern
/plugin install apfel@apfelkern
```

**Als einfacher Skill**, ohne Plugin:

```sh
git clone https://github.com/rdo2hellowelt/apfelkern ~/apfelkern
cp -R ~/apfelkern/skills/apfel ~/.claude/skills/apfel
```

Dann in irgendeinem Projekt `claude` starten und `apfel` tippen. Ergebnisse und eigene Profile
landen in `~/Documents/Apfel/`, nie im geprüften Repo und nie im Plugin.

Braucht: Claude Code, Git, Python 3 (`python3`, unter Windows `py`), Netz zu developer.apple.com.
Erprobt auf macOS; Hinweise für Windows stehen im Skill.

## Unter der Haube

```text
apfelkern/
├─ .claude-plugin/        plugin.json · marketplace.json
└─ skills/apfel/
   ├─ SKILL.md            §0 Start · §1 Gegenstand · §2 Stände · §3 Prüfpunkte
   │                      §4 Kür · §5 Bericht · §6 Profile · §7 Erklärblatt
   ├─ profile/            vorlage.md · beispiel.md · LIESMICH.md
   ├─ references/         hig-seiten · arbeitsmasken · bewegung
   ├─ scripts/            kontrast.py        WCAG-Kontrast, auch mit Deckkraft
   │                      profil_pruefen.py  jede Fundstelle gegen Git
   │                      zufall_hig.py      „Auf gut Glück“
   │                      erklaeren.py       Erklärblatt aus SKILL.md
   ├─ assets/             Vorlagen: Bericht · Befundzeichnung · Erklärblatt
   ├─ evals/evals.json    11 Prüffälle: wann greift er, wann nicht
   ├─ QUELLEN.md          Herkunft, Stand, Lizenz jeder Quelle
   └─ LICENSE · LICENSES/
```

## Danke

Apfel steht auf Schultern, alle MIT, alle in `skills/apfel/LICENSES/`:

- [taste-skill](https://github.com/Leonxlnx/taste-skill) von Leonxlnx: Regeln für Tabellen, Formulare und Zustände
- [emilkowalski/skills](https://github.com/emilkowalski/skills) von Emil Kowalski: Rückmeldung und Bewegung
- [dimensional-drawing](https://github.com/enesozturk/dimensional-drawing) von enesozturk: Zeichenstil der Befundzeichnung

Was bewusst nicht übernommen wurde und warum, steht in `skills/apfel/QUELLEN.md`.

## Lizenz

MIT, © 2026 Hans M. Siehe `LICENSE`.

Apfel ist ein unabhängiges Projekt und hat nichts mit Apple Inc. zu tun. „Apple“ und „Human
Interface Guidelines“ sind Marken von Apple. Apfel verweist auf deren Seiten, verbreitet sie aber
nicht.

---

<sub>Gebaut mit Stolz bei hellowelt. Proud of it? Türlich.</sub>
