---
name: apfel
description: |-
  Apfel prüft Browser-Dialoge für die Arbeit am Schreibtisch (Masken, Tabellen, Formulare,
  Speichern) in jedem Repo, in drei Baugruppen: Motor (Tempo, Latenz, Rückmeldung), Fahrwerk
  (Navigation, Layout, Tabellen, Formulare, Konsistenz), Bremse (Ungespeichertes, Bestätigen,
  Rückgängig, Fehler, Rechte). Maßstab ist das Profil des Projekts: eine Datei mit Vorbild-Dialog
  und Fundstelle je Thema, zum Anlegen, Prüfen und Weitergeben (mitgeliefert: Vorlage und ein
  Beispiel). Danach die Kür mit Aufwand S/M/L. Bericht als Kontaktabzug je
  Bildschirm: Bestand · Haus 1:1 · plus, je Vorschlag mit Fundstelle im Code und HIG-Seite, auf
  Wunsch als Befundzeichnung (technisches Blatt). Apples Human Interface
  Guidelines werden je Seite live von developer.apple.com geladen, nie kopiert.
  Nicht für Landingpages, Marketing-Seiten oder native Mobil-Apps.
  MUST BE USED when user says: "apfel", "Apfel", "apfel profil", "apfel kurz", "apfel zeichnung",
  "apfel verbessern", "apfel erklären", "UI prüfen", "Dialog prüfen", "Oberfläche prüfen", "Optik-Review", "Befundzeichnung".
---

# Apfel

Ein Review für Dialoge, in denen Menschen arbeiten: Masken, Tabellen, Formulare, Speichern. Kein
Geschmacksgutachten. Jeder Befund ist nachprüfbar, entweder im Code oder im Klickweg, und nennt
seine Quelle. Der Review liest nur; geändert wird nichts (Ausnahmen unter „Regeln beim Prüfen“).

Apfel hat zwei Bausteine: die **Prüfpunkte** (§3, gleich für alle) und das **Profil** (§6, je
Projekt). Das Profil ist eine einzelne Markdown-Datei mit dem Hausmaßstab, den Codebasen und den
Grenzen. Mitgeliefert sind eine Vorlage und ein erfundenes Beispiel; eigene Profile entstehen aus
der Vorlage, lassen sich prüfen, verbessern und weitergeben.

## Wann, wann nicht

- **Ja:** ein Arbeitsdialog im Browser, ein Merge Request mit Oberflächen-Anteil, Aufnahmen oder ein
  Klickweg mit der Frage „passt das?“.
- **Nein:** Landingpages, Werbeseiten, Portfolios, Lebensläufe und andere Druckstücke (dafür gibt
  es Art-Direction- und Hausstil-Skills), native iOS/macOS-Apps, reine Animationsarbeit ohne
  Dialog dahinter.

## 0 · Start ohne Auftrag

Wird Apfel ohne Gegenstand aufgerufen („apfel“, „/apfel“, „UI prüfen“):

1. Den Inhalt von `begruessung.txt` (liegt neben dieser Datei) unverändert in einem Codeblock ausgeben.
2. Mit dem Auswahl-Werkzeug fragen, sonst als nummerierte Liste: „Womit fangen wir an?“
   - **Bekanntes Projekt:** nur, wenn im Profilordner eigene Profile liegen (§6). Diese zur Wahl stellen, Name
     aus dem Steckbrief, dann fragen: Pfad zum Repo, Zweig, welcher Dialog.
   - **Eigenes Projekt:** Pfad zum Projekt erfragen und um Lesezugriff bitten. Profil suchen wie in §6 unter
     „Fundorte“. Gibt es keins, anbieten, eins anzulegen (§6, „Neu anlegen“), oder ohne Profil weiter wie in §1, letzte
     Zeile der Tabelle.
   - **Profile:** ansehen, neu anlegen, prüfen, verbessern, weitergeben oder übernehmen. Weiter in §6.
   - **Auf gut Glück:** `python3 <skill>/scripts/zufall_hig.py` nennt eine Seite. Die Seite live laden
     (`curl -s <markdown-adresse>`), daraus drei Punkte, die für Arbeitsdialoge zählen, je ein Satz, mit Link auf
     die Seite ohne `.md`. Danach fragen, ob man das an einem eigenen Dialog prüfen will.
3. Nennt der Aufruf schon einen Gegenstand („apfel, prüf den Auftragsdialog auf Zweig X“), Begrüßung kurz halten, das
   Menü überspringen und mit §1 weitermachen. „apfel profil“ geht direkt nach §6, „apfel kurz …“ prüft wie üblich
   und berichtet als Kurzfassung (§5). „apfel zeichnung …“ prüft wie üblich und liefert nach dem Bericht im Terminal
   gleich die Befundzeichnung (§5). „apfel erklären“ geht direkt nach §7.

Ton: deutsch, verständlich, kurze Absätze. Die Begrüßung bleibt schlicht, ohne weitere Verzierung.

## Ablauf

### 1 · Gegenstand und Hausmaßstab festhalten

- **Gegenstand:** welcher Dialog, welcher Zweig, welcher Commit.
- **Nur die Änderung:** Ist der Gegenstand ein Zweig oder Merge Request, zuerst
  `git diff --name-only <basis>...<zweig> -- <Oberfläche aus dem Profil>` und nur die Stationen
  prüfen, die das berührt. Basis ist der Zielzweig des MR, sonst der Zweig, von dem abgezweigt
  wurde; beide im Kopf nennen. Wer den ganzen Dialog will, sagt es.
- **Material:** Code (immer), dazu Aufnahmen je Station des Klickwegs, falls vorhanden. Aufnahmen
  dürfen als Datei ins Terminal gezogen oder als Pfad genannt werden. Gibt es keine, läuft der
  Review „nur Code“ (siehe §5).
- **Profil wählen** (Fundorte in §6), die erste passende Zeile gilt:

  | Lage | Hausmaßstab | Stände heißen |
  |---|---|---|
  | Ein Profil passt zum Repo (Feld „Gilt, wenn“ im Steckbrief trifft zu) | wie im Profil; dessen Regeln zu Refs, Codebasen und Grenzen gelten zusätzlich | wie im Feld „Stände“ (etwa Alt · Neu 1:1 · Neu plus) |
  | Kein Profil, aber das Projekt nennt einen Maßstab (Referenzdialog, Design-System, Hausstil-Skill in `CLAUDE.md` oder `.claude/skills/`) oder der Auftrag nennt einen | dieser Maßstab, im Kopf mit Pfad und Commit | Bestand · Haus 1:1 · plus |
  | Nichts davon | keiner. Alle H-Punkte werden K, die Spalte „Haus 1:1“ entfällt, Arbeitsmasken und HIG tragen allein. Einmal fragen, ob es einen Referenzdialog gibt, dann ohne weiter | Bestand · plus |

- **Bestand** ist der alte Dialog, den der neue ersetzt. Gibt es keinen, steht in der Spalte „neu“
  und Regel 1 in §2 entfällt.
- **Code lesen**, ohne den Arbeitsbaum zu verändern: nie auschecken, nie Abhängigkeiten
  installieren. Liegt der Gegenstand auf einem fremden Zweig: `git show <ref>:<pfad>`.

### 2 · Drei Stände: Bestand, Haus 1:1, plus

| Spalte | Was sie zeigt |
|---|---|
| **Bestand** | der alte Dialog, wie er heute läuft (oder „neu“) |
| **Haus 1:1** | dieselbe Funktion im Bild des Hausmaßstabs, ohne Zusätze |
| **plus** | Haus 1:1 mit Kür |

**Rangfolge für Haus 1:1**, von oben nach unten, die erste passende Regel gilt:

1. **Funktion folgt dem Bestand.** Kann der neue Dialog weniger oder anders als der Bestand:
   Befund in Haus 1:1, wird nachgezogen. Das gilt auch, wenn der Hausmaßstab für diese Funktion kein
   Muster hat (dann ist die Umsetzung frei; ein gemeinsamer Baustein ist ein Vorschlag für plus).
2. **Stürzt der Bestand ab und der neue Dialog rechnet sauber:** bleibt so, als bewusste Abweichung.
3. **Bild und Bedienung folgen dem Hausmaßstab.** Gleiche Funktion, aber anderes Bild oder andere
   Bedienung (Feldteilung, Ort des Speicherns, wann Knöpfe aktiv sind): Befund in Haus 1:1,
   angleichen. Bleibt die Funktion des Bestands erhalten, gewinnt das Bild des Hausmaßstabs.
4. **Mehr als Bestand oder Hausmaßstab:** gehört nicht in Haus 1:1. Zurück auf den Maßstab, als
   Vorschlag nach plus, oder bewusst behalten als Abweichung in der MR-Beschreibung (eine Zeile,
   mit Fundstelle).
5. **Hat der Hausmaßstab im Bild eine Lücke** und der Bestand verlangt dazu nichts: kein Befund in
   Haus 1:1; der Vorschlag geht nach plus und gilt für beide Dialoge.
6. **Bleibt es unklar** (Regel 1 und 3 ziehen in verschiedene Richtungen): Befund in Haus 1:1 mit
   Aufwand „Entscheidung“, beide Seiten mit Fundstelle, keine eigene Auflösung.

### 3 · Drei Baugruppen

Je Prüfpunkt:

- **Art:** **H** = der Hausmaßstab hat dafür ein Muster (Abweichung ist ein Befund in Haus 1:1).
  **K** = nur Kür (Abweichung ist höchstens ein Vorschlag in plus), es sei denn, der Bestand
  verlangt es (Regel 1). Ohne Hausmaßstab ist alles K.
- **Prüfbar:** **Code** = aus dem Quelltext prüfbar. **Lauf** = nur am laufenden Dialog prüfbar.
  Beim Review „nur Code“ kommen Lauf-Punkte nicht in die Tabelle, sondern in „Offen für den
  Klickweg“.
- **Quelle:** `Haus:<Thema>` heißt: die Fundstelle zu diesem Thema im Profil, Abschnitt
  „Fundstellen je Thema“; ohne Profil die Stelle im genannten Maßstab. `HIG:<seite>` heißt: die Seite laden (Liste in `references/hig-seiten.md`).
  `Arbeitsmasken §n` und `Bewegung §n` verweisen auf `references/`.

#### Motor: Tempo, Latenz, Rückmeldung

| Prüfpunkt | Art | Prüfbar | Quelle |
|---|---|---|---|
| Knopf zeigt sofort Wirkung (Ladezustand am Knopf, gesperrt während der Anfrage) | H | Code | Haus:Laden am Knopf, HIG:feedback |
| `:active`-Rückmeldung beim Drücken | K | Lauf | Bewegung §1 |
| Laden zeigt das spätere Layout mit Platzhaltern; nichts springt, wenn die Daten kommen | H | Code, Lauf | Haus:Platzhalter beim Laden, Arbeitsmasken §6, HIG:loading |
| Aktualisieren behält die alten Werte sichtbar, bis neue da sind | K | Code | Arbeitsmasken §6 |
| Speichern sperrt doppeltes Auslösen und zeigt, dass es läuft | H | Code | Haus:Speichern, Verwerfen |
| Keine künstlichen Wartezeiten: Debounce, Timer, Tooltip-Verzögerung beim zweiten Hover | K | Code | Bewegung §1, §3 |
| Animationen höchstens 300 ms, keine bei Tastaturaktionen, `prefers-reduced-motion` beachtet | K | Code, Lauf | Bewegung §2 bis §4, HIG:motion |
| Fortschritt bestimmt anzeigen, wenn die Menge bekannt ist | K | Code | HIG:progress-indicators |

#### Fahrwerk: Navigation, Layout, Tabellen, Formulare, Konsistenz

| Prüfpunkt | Art | Prüfbar | Quelle |
|---|---|---|---|
| Wo bin ich, wohin kann ich, wie komme ich zurück: Seitenleiste und Kopf wie im Hausmaßstab | H | Code | Haus:Navigation, Haus:Kopf, HIG:sidebars |
| Seitenleiste höchstens zwei Ebenen, aktiver Eintrag eindeutig | H | Code | Haus:Navigation, HIG:sidebars |
| Feldteilung Beschriftung/Feld wie im Hausmaßstab; ohne Maßstab Beschriftung über dem Feld | H | Code | Haus:Feldlayout, Arbeitsmasken §3 |
| Auswahl statt Tippen, wo die Werte bekannt sind (Autocompletes, Dropdowns) | H | Code | Haus:Auswahlfelder, HIG:entering-data, HIG:combo-boxes |
| Tabellen mit Filtern wie im Hausmaßstab | H | Code | Haus:Tabellen |
| Zahlen rechtsbündig in Ziffern gleicher Breite, Datum einheitlich, fehlender Wert als Strich, echte Null gedruckt | K | Code | Arbeitsmasken §2, HIG:lists-and-tables |
| Gesamtzahl über der Tabelle, Kopf bleibt beim Scrollen stehen | K | Lauf | Arbeitsmasken §2 |
| Filter, Sortierung, Auswahl bleiben beim Zurückkommen erhalten | K | Code | Arbeitsmasken §2; H nur, wenn der Bestand es kann (Regel 1) |
| Prüfung beim Verlassen des Felds, Meldung am Feld, nicht erst beim Speichern | K | Code | HIG:entering-data |
| Gesperrte Felder bleiben lesbar und sagen, warum | K | Code, Lauf | Arbeitsmasken §3 |
| Ein Speichermodell je Ansicht | H | Code | Haus:Speichern, Verwerfen, Arbeitsmasken §3 |
| Texte zentral übersetzt, gleiche Beschriftung für gleiche Aktion | H | Code | Haus:Texte, HIG:writing, HIG:buttons |
| Eine Farbe bedeutet eine Sache; Status nicht nur über Farbe | K | Code | HIG:color, HIG:accessibility |
| Tab-Reihenfolge, sichtbarer Fokus, Enter/Escape in Dialogen | K | Lauf | HIG:keyboards, HIG:focus-and-selection |
| Kontrast Text 4.5:1, große Schrift und Bedienelemente 3:1, gemessen mit `scripts/kontrast.py` | K | Code, Lauf | HIG:accessibility |

#### Bremse: Ungespeichertes, Bestätigen, Rückgängig, Fehler, Rechte

| Prüfpunkt | Art | Prüfbar | Quelle |
|---|---|---|---|
| Jeder Weg aus der Ansicht mit offenen Änderungen fragt („Speichern und Verlassen“ / „Verwerfen und Verlassen“): Seitenleiste, Menü, Zurück, Fenster schließen | H | Code | Haus:Ungespeichertes, HIG:feedback |
| Escape in einem Unterdialog schließt nur diesen, nicht den Bearbeitungsmodus | K | Code, Lauf | HIG:modality, HIG:keyboards |
| Speichern und Verwerfen nur aktiv, wenn etwas geändert ist | H | Code | Haus:Speichern, Verwerfen |
| Validierung: blockierend gegen Warnung, „Trotzdem speichern“, Meldungen nach Abschnitt | H | Code | Haus:Validierung |
| Löschen und Unumkehrbares: Rückfrage nennt Objekt und Folge, Abbrechen da, Bestätigen als gefährlich gekennzeichnet | H | Code | Haus:Löschen, HIG:alerts |
| Rückfragen sparsam: nicht für Umkehrbares | K | Code | HIG:alerts, HIG:modality |
| Fehler im Block, der fehlschlug: was, seit wann, wie weiter; ein gescheiterter Abruf zeigt einen Fehler, nicht „keine Daten“ | K | Code | Arbeitsmasken §6, HIG:feedback |
| Serverfehler als lesbarer Text, nie der rohe Antwortrumpf | H | Code | Haus:Meldungen, Haus:Fehler |
| Bearbeiten nur mit Recht; ohne Recht lesbar statt versteckt, mit Grund | H | Code | Haus:Bearbeiten und Rechte, Arbeitsmasken §3 |
| Rechte im Backend geprüft, nicht nur am Knopf | H | Code | Haus:Bearbeiten und Rechte |

### 4 · Kür (Spalte plus)

Was über den Hausmaßstab hinausgeht, zuerst der Hebel, dann die Quelle:

- **Tief hängend:** wenige Zeilen, ein Ort, kein Verhaltensbruch. Meist Aufwand S.
- **Weitreichend:** betrifft mehrere Dialoge oder gemeinsame Bausteine, braucht eine Entscheidung.
  Aufwand M oder L.

**Aufwand** schätzt immer den Umbau: **S** bis zwei Stunden an einer Stelle; **M** ein Tag oder
mehrere Stellen; **L** mehrere Tage oder ein gemeinsamer Baustein. Hängt der Umbau an einer
Entscheidung, steht „Entscheidung, dann S/M/L“. Die Schätzung ist ein Vorschlag, entschieden wird
im Team.

### 5 · Bericht als Kontaktabzug

**Kopf**, vier Felder, Zusätze als Unterpunkte darunter:

- **Dialog und Stand:** Name, Zweig und Commit; Hausmaßstab mit Ort und Stand (oder „keiner“); Ort
  des Bestands.
- **Material:** Code, Aufnahmen ja/nein, Klickweg ja/nein. Unterpunkte: nicht erreichbare Teile,
  nicht geladene HIG-Seiten.
- **Urteil:** ein Satz.
- **Zahlen:** Vorschläge je Baugruppe, davon in Haus 1:1 und nur in plus.

**Stationen.** Gibt es einen Klickweg, ist jede seiner Stationen eine Station des Berichts. Ohne
Klickweg: je Seite (Route) eine Station je Modus (Lesen, Bearbeiten und Speichern), jeder
Unterdialog mit eigenen Eingaben eine eigene Station.

**Je Station ein Kontaktabzug**, die Stände nebeneinander. Der Kopf der plus-Spalte nennt alle
Baugruppen ihrer Vorschläge („plus · Fahrwerk, Bremse“). Mit Aufnahmen stehen dort Bilder (für plus
eine Skizze oder ein beschriftetes Bild, solange es nicht gebaut ist). **Nur Code:** je Spalte zwei
bis vier Zeilen Beschreibung dessen, was man sehen würde, mit Fundstelle.

Darunter die Vorschläge der Station:

| Nr | Baugruppe | Bestand | Haus 1:1 | plus | Aufwand | Fundstelle Code | HIG-Seite |
|---|---|---|---|---|---|---|---|

Beispielzeilen stehen im Profil (Muster: `profile/beispiel.md`).

- **Fundstelle Code** mit vollem Pfad ab Repo-Wurzel, bei mehreren Codebasen mit Präfix aus dem
  Profil; Zeile nur, wenn selbst gesehen.
- Spalte **Haus 1:1** nennt die Abweichung und die Regel aus §2, die greift; „wie Bestand“, wenn es
  keine gibt.
- Spalte **plus** nennt den Kür-Vorschlag mit „tief hängend“ oder „weitreichend“ und der Quelle aus
  `references/`; „wie Haus 1:1“, wenn es keinen gibt.
- Spalte **HIG-Seite**: Seitenname aus `references/hig-seiten.md`; „–“, wenn keine Seite passt
  (Rechte, Feldteilung, Hausregeln). Dann trägt die Fundstelle die Begründung.

**Offen für den Klickweg:** Lauf-Punkte und Urteile, die erst am laufenden Dialog entschieden werden,
je eine Zeile mit Station und was zu prüfen ist.

**Was trägt:** höchstens drei Zeilen, was der Dialog schon gut macht.

**Kurzfassung** („apfel kurz“): geprüft wird genauso, berichtet nur der Kopf (Urteil, Zahlen) und
die drei wichtigsten Vorschläge, je eine Zeile mit Fundstelle. Reihenfolge: Haus 1:1 vor plus,
Bremse vor Motor vor Fahrwerk (verlorene Arbeit zuerst). Kein Kontaktabzug. Zum Schluss anbieten,
den vollen Bericht nachzuliefern.

**Ausgabe:** im Terminal als Markdown. Danach mit dem Auswahl-Werkzeug fragen, sonst als nummerierte Liste, ob der
Bericht noch anders kommen soll: **Seite zum Lesen**, **Befundzeichnung**, **beides** oder **nur Terminal**. Nennt der
Auftrag es schon („auch als Seite“, „apfel zeichnung“), nicht noch einmal fragen. Jede Datei danach öffnen (Mac
`open <datei>`, Windows `start <datei>`, in PowerShell `Invoke-Item <datei>`). Der Inhalt bleibt derselbe wie im
Terminal.

**Seite zum Lesen:** aus `assets/bericht-vorlage.html` eine Datei `apfel-bericht-<dialog>-<JJJJ-MM-TT>.html` im
Apfel-Ordner bauen, wie oben in der Vorlage beschrieben. Je Spalte ein Bild oder zwei bis vier Zeilen; für plus ohne
Aufnahme höchstens eine schlichte SVG-Skizze.

**Befundzeichnung:** ein Blatt, das zeigt, wo die Vorschläge im Dialog sitzen und welchen Weg sie nehmen, im Stil
der Maßzeichnungen, die Apple für Zubehör veröffentlicht. Aus `assets/zeichnung-vorlage.html` eine Datei
`apfel-zeichnung-<dialog>-<JJJJ-MM-TT>.html` im Apfel-Ordner bauen. Kopf (`header.tb`, dazu `<title>`) aus dem
Bericht: Dialog, Stand im Zweig, Hausmaßstab, Quelle, Hinweise, Kennzahlen. Die Fußzeile verlinkt die Seite zum
Lesen, wenn es sie gibt. Im Skript bleibt der Block WERKZEUG, wie er ist (`rr`, `hat`, `ar`, `dimH`, `dimV`,
`callout`, `nb`, `slotLabel`, `title`, `detailRef`, `xbox`, `notes`, `table`); der Block ZEICHNUNG wird neu
geschrieben. Das Beispiel darin, das Auftragsformular der Kundenkartei, ist das Muster. Das Blatt misst
1700 × 1060: Hinweise oben links, Explosionsansicht darunter, Draufsicht in der Mitte, Tabellen rechts, unten
Schnitt und Details.

- **Nur Grau, die Striche tragen die Bedeutung.** Voll = Stand im Zweig, Strich-Punkt (`vor`) = Vorschlag,
  gestrichelt (`slot`) = Platzhalter, schraffiert (`hat`) = gesperrt, fehlt oder überschrieben, grau (`hug`) = Knopf
  oder Feld. Bewusst nur hell.
- **Aufbau, nicht Inhalt.** Bereiche und Bausteine als benannte Platzhalter (Meldung, Filterleiste, Tabelle). Text
  aus dem Dialog nur, wenn der Vorschlag daran hängt, etwa ein Feld oder ein Reiter.
- **Keine erfundenen Maße.** Proportionen schematisch. Zahlen nur, wenn sie im Code stehen (`col-4`, neun Felder),
  sonst Worte: hug, flex, fill.
- **Nummern wie im Bericht.** Jeder Vorschlag ist ein Kästchen (`nb`) an seiner Stelle in der Draufsicht, mit
  derselben Nummer in Hinweisen und Tabellen.
- **Ansichten nach Bedarf.** Draufsicht immer, mit Detailkreisen. Explosionsansicht, wenn Ebenen zählen
  (Unterdialog, Auswahl, modaler Dialog, der Weg einer Taste). Schnitt, wenn ein Weg zählt (Speichern, Prüfung im
  Client und auf dem Server, Rechte). Höchstens ein Detail je Vorschlag. Rechts die Tabellen Vorschläge,
  Fundstellen, Apple-Seiten und Offen für den Klickweg.
- **Ein Blatt.** Bei mehreren Stationen zeigt die Draufsicht die Station mit den meisten Vorschlägen; die übrigen
  kommen als Detail oder bleiben im Bericht. Ein zweites Blatt nur, wenn das erste sonst unlesbar wird.
- **Einmal ansehen, wenn es geht.** Steht ein Browser ohne Fenster bereit (Chrome oder Edge mit `--headless
  --screenshot`), vor dem Öffnen ein Bild machen und überlappende Beschriftungen oder Linien über den Blattrand in
  einem Durchgang beheben. Sonst ohne Blick öffnen.
- **Als Artefakt** (Claude Code mit Artefakten): `<!doctype>`, `<html>`, `<head>` und `<body>` weglassen, der Rest
  bleibt.

**Prüfgerüst und Klickweg** eines Projekts folgen derselben Gliederung: je Station die Stände, je
Stand die Baugruppen Motor, Fahrwerk, Bremse.

## 6 · Profile

Das Profil sagt, woran ein Projekt sich misst. Aufbau: oben ein **Steckbrief** (Tabelle mit den
Feldern Gilt, wenn · Stände · Hausmaßstab · Ordner des Maßstabs · Ref des Maßstabs · Oberfläche ·
Stand), dann Codebasen, Grenzen und die **Fundstellen je Thema**: die 15 Grundthemen der Vorlage
mit denselben Namen wie `Haus:` in §3, dazu eigene Themen nach Bedarf. Die Vorlage gibt den Aufbau
vor; sie ist kein Profil.

**Profilordner:** `~/Documents/Apfel/profile/`, neben den Ergebnissen, nicht im Skill. So bleiben
eigene Profile privat und überleben jede neue Fassung des Skills, auch als Plugin. Fehlt der Ordner,
mit `mkdir -p ~/Documents/Apfel/profile` anlegen. Ist er ein Git-Repo, nach jedem Schreiben mit
kurzer Nachricht committen. Im Skill liegt `<skill>/profile/` mit `vorlage.md`, `beispiel.md` (erfunden,
zum Ansehen) und `LIESMICH.md` (für Menschen); das Beispiel gilt nie für ein echtes Repo.

**Fundorte**, das erste Profil, dessen „Gilt, wenn“ zutrifft, gilt:

1. im geprüften Repo `.apfel/profil.md` (das Team pflegt es mit dem Code),
2. im Profilordner `<projekt>.md`.

Die Liste im Untermenü zeigt nur diese beiden Orte; `beispiel.md` nur, wenn man es ansehen will.

**Untermenü** („apfel profil“ oder Menüpunkt „Profile“): zuerst die vorhandenen Profile als kurze
Liste mit Name, Gilt wenn und Stand. Dann mit dem Auswahl-Werkzeug fragen, vier Möglichkeiten:

- **Ansehen:** Steckbrief und Themen-Tabelle zeigen, Grenzen ganz.
- **Neu anlegen:** aus `vorlage.md`, mit vier Fragen: Name und woran man das Repo erkennt; Ordner
  der Oberfläche; Vorbild-Dialog oder Design-System (oder keins); was nicht geöffnet oder
  ausgeführt werden darf. Die Fundstellen je Thema sucht Apfel danach selbst im Vorbild
  (`git grep` auf dem Ref des Maßstabs), mit dem Muster in einem Satz; was fehlt, bleibt „–“. Das
  fertige Profil zeigen, erst nach einem Ja ablegen, dann prüfen.
- **Prüfen und verbessern:** zuerst
  `python3 <skill>/scripts/profil_pruefen.py <profil> --repo <pfad> --ref <ref>` (ohne Repo nur der
  Aufbau). Dann schärfen: fehlende Fundstellen im
  Vorbild am neuen Ort suchen, Themen mit „–“ belegen, eigene Themen ergänzen, „Stand“ mit der
  Vorschlagszeile des Skripts neu setzen. Nichts still ersetzen: Änderungen als vorher und nachher
  zeigen, erst nach einem Ja schreiben, danach noch einmal prüfen.
- **Tauschen:** fragen, in welche Richtung.
  - *Weitergeben:* Pfad der Datei nennen, die eine Datei genügt. Vorher durchsehen und nennen, was
    nicht nach draußen soll: interne Adressen, Zugangsdaten, Namen von Personen.
  - *Übernehmen:* Pfad zu einer Datei oder eingefügter Text. Erst den Aufbau prüfen, dann zeigen,
    was das Profil festlegt, die Grenzen ganz, dann nach einem Ja in den Profilordner legen. Gibt
    es den Namen schon: Unterschiede zeigen und fragen, ob ersetzen, zusammenführen oder unter
    neuem Namen.

**Schreiben** ist hier die Ausnahme zu „nur lesen“: Apfel schreibt nur in den Profilordner und nur
nach einem Ja. Ins Projekt-Repo (`.apfel/profil.md`) nur, wenn es ausdrücklich verlangt wird.

## 7 · Erklärblatt

„apfel erklären“ baut eine Seite, die zeigt, wie Apfel arbeitet: Ablauf, Schnitt durch einen Lauf,
Profile, drei Stände mit Rangfolge, alle Prüfpunkte zum Filtern, Bericht, Befundzeichnung, Regeln,
Probeläufe. Die Seite entsteht aus dieser Datei, sie ist also immer so aktuell wie der Skill.

1. `python3 <skill>/scripts/erklaeren.py` ausführen. Das Skript liest die
   Prüfpunkt-Tabellen und die Rangfolge aus dieser Datei, die Profile aus dem Profilordner, die Probeläufe
   und die jüngste Befundzeichnung (PNG) aus dem Apfel-Ordner, füllt `assets/erklaer-vorlage.html`
   und schreibt `apfel-erklaert-<JJJJ-MM-TT>.html` in den Apfel-Ordner. Es nennt den Pfad.
2. Die Datei öffnen (`open <datei>`), im Terminal zwei Sätze dazu: was neu ist seit dem letzten
   Blatt, falls eins im Apfel-Ordner liegt.
3. Mit Artefakten: `--artefakt` dazu, dann fehlen `<!doctype>`, `<html>`, `<head>` und `<body>`.

Ändern sich Abschnitte, die das Skript liest (Überschriften `#### Motor/Fahrwerk/Bremse`, die
Tabellen darunter, die Liste nach „Rangfolge für Haus 1:1“), das Skript im selben Zug anpassen.
Feste Texte der Seite stehen in der Vorlage.

## Regeln beim Prüfen

- **Pfade.** `<skill>` ist der Ordner dieser Datei: der Pfad, den Claude Code beim Laden als
  Basisordner des Skills nennt (als Skill meist `~/.claude/skills/apfel/`, als Plugin ein Ordner
  unter `~/.claude/plugins/`). Dort liegen `scripts/`, `assets/`, `references/`, `begruessung.txt`.
  Die Sitzung läuft im geprüften Repo oder anderswo, also Skripte immer mit vollem Pfad aufrufen:
  `python3 <skill>/scripts/kontrast.py …`, `<skill>` dabei durch den echten Pfad ersetzen (gilt für
  alle Skripte; wo hier kurz `scripts/…` steht, ist `<skill>/scripts/…` gemeint). Der **Apfel-Ordner** für Ergebnisdateien (Seite zum Lesen,
  Befundzeichnung, Erklärblatt) ist `~/Documents/Apfel/` (im Finder „Dokumente/Apfel“), nie das
  geprüfte Repo und nie der Skill-Ordner. Fehlt er, mit `mkdir -p ~/Documents/Apfel` anlegen.
- **Zahl statt Adjektiv.** „12 px #999 auf Weiß, 2.85:1“ statt „schlecht lesbar“. Kontrast immer mit
  `python3 <skill>/scripts/kontrast.py <vorne> <hinten> [--alpha n]`.
- **Windows.** Python heißt meist `py` oder `python`; `python3` kann dort ein Platzhalter sein, der
  den Microsoft Store öffnet, also zuerst `py`, dann `python`. In PowerShell `curl.exe` statt `curl`
  (sonst greift ein gleichnamiger Befehl mit anderen Schaltern), `Select-String` statt `grep`. In Git
  Bash gilt alles wie auf dem Mac. Fehlt Python ganz: einmal sagen, dann ohne Skript weiter;
  Kontrast als Urteil kennzeichnen, für „Auf gut Glück“ eine Seite aus `references/hig-seiten.md`
  selbst wählen, Fundstellen eines Profils einzeln mit `git cat-file -e <ref>:<pfad>` prüfen.
- **Befehle so, dass die Freigaben greifen.** Git immer als ein Befehl mit vollem Pfad:
  `git -C <pfad zum repo> show <ref>:<datei>`. Kein `cd` vor einem Git-Befehl, keine Variablen,
  keine Schleifen, keine Ketten mit `;` oder `&&`; weiterleiten nur an `head`, `tail -n`, `wc`
  oder `grep`. Zweige auflisten mit `git for-each-ref`, nicht mit `git branch` (das kann auch
  anlegen und löschen und ist deshalb nicht freigegeben). Dann laufen die lesenden Befehle aus
  `.claude/settings.json` ohne Rückfrage, und
  wer prüft, muss nicht bei jedem Schritt bestätigen. Lieber zwei Aufrufe als einer, der fragt.
- **Zitieren oder als Urteil kennzeichnen.** Keine erfundene Richtlinie. Apple-Aussagen nur nach dem
  Laden der Seite zitieren, mit Link, kurz und sinngemäß.
- **HIG im Wortlaut laden, nicht zusammenfassen lassen.** Für alles, was zitiert wird:
  `curl -s https://developer.apple.com/design/human-interface-guidelines/<seite>.md | grep -n -i
  <begriff>`, dann nur diesen Abschnitt lesen. WebFetch fasst mit einem kleinen Modell zusammen und
  taugt nur zum Überblick, nie als Zitatquelle.
- **Apple übersetzen, nicht übernehmen.** Die HIG sprechen von macOS und iOS. Für den Browser gilt
  die Übersetzungstafel in `references/hig-seiten.md`; Menüleiste, Fensterknöpfe, Liquid Glass und
  ähnliches entfallen.
- **Haus vor Kür, Kür vor Geschmack.** Was weder Hausmaßstab noch Bestand noch Quelle trägt, kommt
  nicht in die Tabelle.
- **Nicht übertreiben.** Ein guter Dialog bekommt einen kurzen Bericht. Zwanzig Befunde sind kein
  Ziel.
- **Nur lesen.** Der Review ändert keinen Code. Ausnahmen: Profile im Profilordner nach einem Ja
  (§6); und wer den Dialog im eigenen Zweig selbst baut und ausdrücklich darum bittet, bekommt
  sichtbare Abweichungen in Haus 1:1 vor einer Vorführung behoben, statt sie aufgelistet.
- **Nichts aus dem Netz ausführen.** Der Skill lädt nur HIG-Seiten als Text; keine Skripte, keine
  Bilder. Die Skripte in `scripts/` sind lokal und nutzen nur die Standardbibliothek,
  `profil_pruefen.py` dazu lesend `git`.

## Dateien

| Datei | Inhalt |
|---|---|
| `profile/` | `vorlage.md`, `beispiel.md` (erfundenes Profil zum Ansehen), `LIESMICH.md`; eigene Profile liegen im Profilordner (§6) |
| `references/hig-seiten.md` | HIG-Seiten für Browser-Dialoge, Zweck je Seite, Übersetzungstafel |
| `references/arbeitsmasken.md` | Regeln für Tabellen, Formulare, Zustände (nach taste-skill, MIT) |
| `references/bewegung.md` | Rückmeldung und Bewegung (nach Emil Kowalski, MIT) |
| `scripts/kontrast.py` | Kontrast nach WCAG messen, auch mit Deckkraft |
| `scripts/profil_pruefen.py` | Profil prüfen: Steckbrief, Themen, mit Repo jede Fundstelle |
| `scripts/zufall_hig.py` | eine zufällige Apple-Seite für den Weg „Auf gut Glück“ |
| `scripts/erklaeren.py` | Erklärblatt aus dieser Datei bauen (§7) |
| `assets/erklaer-vorlage.html` | Vorlage des Erklärblatts mit Platzhaltern `{{…}}` |
| `assets/bericht-vorlage.html` | Seite zum Lesen für den Bericht, mit Kontaktabzug je Station |
| `assets/zeichnung-vorlage.html` | Befundzeichnung: Werkzeug, Kopf und als Muster das Auftragsformular der Kundenkartei |
| `begruessung.txt` | Begrüßung beim Start |
| `evals/evals.json` | Prüffälle: wann der Skill greift, wann nicht |
| `QUELLEN.md` | Herkunft, Stand, Lizenzen, Änderungen |
| `LICENSE` | MIT, für Apfel selbst |
| `LICENSES/` | MIT-Texte der übernommenen Quellen |

## Pflege

Prüffrist 90 Tage, **nächste Prüfung 31.01.2027**. Dann: jedes Profil mit `scripts/profil_pruefen.py`
gegen den Ref seines Maßstabs prüfen (Regel im Feld „Ref des Maßstabs“) und „Stand“ nachziehen,
HIG-Liste stichprobenartig laden, die Fälle in `evals/evals.json` einmal durchspielen. Danach das
Datum hier weitersetzen.

**Verbessern aus jeder Sitzung:** Die gültige Fassung ist das Git-Repo des Skills. Ist `<skill>` dieses
Repo (als Skill installiert, mit `.git` daneben), dort ändern. Ist `<skill>` eine Plugin-Kopie, dort
nichts ändern, sondern die Änderung für das Repo vorschlagen. Sagt
jemand „apfel verbessern“ oder fällt bei einem Lauf etwas auf (Rückfrage trotz Freigabe, falsche
Regel, Lücke in der Prüfliste): Änderung an dieser Datei oder an `references/`, `assets/`,
`scripts/` als vorher/nachher vorschlagen, nach einem Ja schreiben, eine Zeile in `QUELLEN.md`
unter Änderungen. Gibt es neben dieser Datei ein Git-Repo, danach mit kurzer Nachricht committen.
Probeläufe liegen in `~/Documents/Apfel/probelaeufe/`, nicht im Skill-Repo.
