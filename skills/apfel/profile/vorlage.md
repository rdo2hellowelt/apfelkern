# Profil <Projekt>

_Vorlage. Kopieren nach `profile/<projekt>.md` oder ins Projekt-Repo als `.apfel/profil.md`, dann
füllen. Schneller geht es mit `apfel profil` und „Neu“: Apfel stellt vier Fragen und sucht die
Fundstellen selbst. Spitze Klammern ersetzen; „–“ heißt, das Vorbild hat dafür kein Muster, der
Prüfpunkt zählt dann als Kür._

| Feld | Wert |
|---|---|
| Gilt, wenn | <woran man das Repo erkennt, z. B. Remote enthält `<name>` oder es gibt `<ordner>`> |
| Stände | Bestand · Haus 1:1 · plus |
| Hausmaßstab | <Vorbild-Dialog oder Design-System> oder „keiner“ |
| Ordner des Maßstabs | `<pfad im Repo>`, die Fundstellen unten sind relativ dazu |
| Ref des Maßstabs | <Zweig, oder eine Regel wie „jüngster Release-Zweig“> |
| Oberfläche | `<Ordner der geprüften Dialoge>` |
| Stand | <TT.MM.JJJJ>, Fundstellen geprüft auf `<ref>` @ `<commit>` |

## Codebasen

- **Geprüfter Dialog (NEU):** Zweig des Auftrags.
- **Hausmaßstab (HAUS):** Ordner und Ref wie oben. Ohne Vorbild „keiner“, dann sind alle Prüfpunkte Kür.
- **Bestand (ALT):** <alter Dialog, Pfad> oder „neu“.
- **Code lesen** nur, ohne den Arbeitsbaum zu ändern: `git show <ref>:<pfad>`, `git grep <muster> <ref>`.
- **Fundstellen-Präfixe:** `NEU:`, `HAUS:`, `ALT:`.

## Grenzen

- <was nicht geöffnet, gestartet oder beschrieben werden darf, z. B. Seiten, die schon beim Öffnen schreiben>

## Hausmaßstab: Fundstellen je Thema

Je Thema eine Fundstelle im Vorbild und das Muster in einem Satz. Die Themennamen bleiben, wie sie
sind, Apfel verweist mit `Haus:<Thema>` darauf. Eigene Themen dürfen dazukommen.

### Motor

| Thema | Fundstelle | Muster |
|---|---|---|
| Laden am Knopf | – | – |
| Platzhalter beim Laden | – | – |

### Fahrwerk

| Thema | Fundstelle | Muster |
|---|---|---|
| Navigation | – | – |
| Kopf | – | – |
| Feldlayout | – | – |
| Auswahlfelder | – | – |
| Tabellen | – | – |
| Texte | – | – |

### Bremse

| Thema | Fundstelle | Muster |
|---|---|---|
| Ungespeichertes | – | – |
| Speichern, Verwerfen | – | – |
| Validierung | – | – |
| Löschen | – | – |
| Meldungen | – | – |
| Fehler | – | – |
| Bearbeiten und Rechte | – | – |

## Beispielzeilen für den Bericht

Frei. Zwei Zeilen im Format aus `SKILL.md` §5 helfen Apfel, den Ton des Projekts zu treffen.
