# Arbeitsmasken: Tabellen, Formulare, Zustände

Verdichtet und übersetzt aus `references/app-screens.md` von taste-skill (Leonxlnx, MIT, Stand
`12af471`), Abschnitte 7, 8, 10, 11, 13, 14. Die Vorlage beruht auf einer Studie von 23
Desktop-Masken; wo sie darüber hinausgeht, nennt sie es selbst Hausregel. Ausgelassen sind
Landingpage-Teile, Diagramm-Feinheiten, Telefon, Paletten und alle Skripte.

**Rang:** Diese Regeln sind Kür. Wo der Hausmaßstab des Projekts es anders macht (etwa mit den
Voreinstellungen einer Bibliothek wie PrimeReact), gilt der Hausmaßstab, und der
Unterschied ist höchstens ein Kür-Vorschlag für beide. Ohne Hausmaßstab sind diese Regeln der
Maßstab.

## §1 Geltung

Masken, in denen gearbeitet wird: Listen mit Filtern, Detailseite eines Objekts, Einstellungen,
Verwaltung. Nicht: Seiten, die einmal gelesen werden.

## §2 Tabellen und Listen

- **Zahlen rechtsbündig**, in Ziffern gleicher Breite (`font-variant-numeric: tabular-nums`) oder
  Monospace. Linksbündige Zahlenspalten und springende Ziffern sind ein Befund.
- **Feste Nachkommastellen je Größe:** Geld 2, Prozent 1 oder 2, Anzahl 0. Tausendertrenner
  durchgehend. Kein Leerzeichen-Mischmasch beim Währungszeichen.
- **Datum** in einer Form je Tabelle; zum Vergleichen sortierbar und rechtsbündig.
- **Kennungen** (IDs) in Monospace, bei Bedarf gekürzt, mit Kopierknopf.
- **Fehlender Wert** ist ein grauer Strich, **echte Null** wird gedruckt.
- **Spaltenkopf** klein, grau, normale Schreibung; keine Großbuchstaben mit Sperrung, kein
  Farbband. Zahlenköpfe bündig über ihren Werten. Sortiersymbol nur an der aktiven Spalte.
- **Keine Zebrastreifen**; Zeilentrenner 1 px und kaum dunkler als die Fläche, oder nur Abstand.
  Ist das im Hausmaßstab uneinheitlich (Streifen in manchen Tabellen, in anderen nicht), daraus
  keinen Vorschlag machen, solange das Team nicht entschieden hat.
- **Kennspalte** (Name, Bezeichnung) bekommt die meiste Breite und wird nie abgeschnitten;
  Kürzen im Text vor Kürzen im Layout. Abschneiden einzeilig mit Auslassungszeichen, nie im Wort.
- **Ein Statuszeichen je Zeile**; Statusetiketten als blasse Fläche mit dunkler Schrift desselben
  Farbtons, nie gequetscht (`white-space: nowrap; flex: none`).
- **Zeilenaktionen:** keine, oder eine an fester Stelle rechts. Kontrollkästchen nur, wenn es
  Sammelaktionen gibt.
- **Geänderte Zelle** in einer bearbeitbaren Tabelle trägt eine Markierung.
- **Volle Liste:** Gesamtzahl über der Tabelle, Kopf bleibt beim Scrollen stehen, am Ende Blättern
  oder Nachladen mit Bereich („1 bis 50 von 1.284“).
- **Zahlen im Filter** werden aus der aktuellen Ansicht gerechnet und bei jedem Wechsel neu.

## §3 Formulare und Einstellungen

- **Beschriftung über dem Feld**, kein Platzhalter als Beschriftung, keine schwebenden Labels.
  Hat der Hausmaßstab eine andere Feldteilung (etwa Beschriftung links vom Feld), gilt er, und
  dieser Punkt wird kein Befund.
- **Eine Feldhöhe je Kontext**; Knöpfe einer Reihe gleich hoch.
- **Ein gefüllter Hauptknopf je Ansicht**, Nebenknöpfe umrandet oder als Text.
- **Gesperrte Felder bleiben lesbar** und sagen, warum sie gesperrt sind. 30 % Deckkraft oder
  1.4:1 Kontrast sind ein Befund.
- **Ein Speichermodell je Ansicht:** alles speichert sich selbst mit stiller Bestätigung, oder ein
  Speichern je Bereich. Nie gemischt.
- **Zerstörende Aktionen** zuletzt, eigener Abschnitt, als Text- oder Randknopf in Warnfarbe, Folge
  in Worten, Rückfrage nennt das Objekt.
- **Zeigen, was eine Einstellung bewirkt**, wo es geht: eine kleine Vorschau neben dem Schalter.

## §4 Dichte

- Dichte ist drei Größen zusammen: Zeilenhöhe, Innenabstand, Schriftgröße. Nicht die Schrift
  verkleinern und den Abstand lassen.
- Gesetzter Leerraum wirkt ruhig, übrig gebliebener wirkt unfertig: leere Spalten über alle Zeilen,
  gestreckte Karten, halbleere Kopfleisten sind Befunde.
- Für den Datenstand bauen, den das Konto heute hat, nicht nur für den vollen.

## §5 Farbe und Status

- Rot ist ein Signal, keine Textur: höchstens eine rote Markierung je Objekt.
- Vorzeichen stehen im Text, nicht nur in der Farbe.
- Akzentfarbe auf Daten und höchstens einem Bedienelement, nicht auf jeder Leiste und jedem Knopf.
- Keine Verläufe, kein Glas, kein Glühen auf Flächen, Knöpfen, Karten.
- Rahmen oder Schatten, nie beides; Schatten nur an Schwebendem (Menü, Popover, Dialog).

## §6 Leer, Laden, Fehler

- **Laden:** endgültiges Layout, jeder Wert als flache graue Fläche in echter Größe, Beschriftungen
  sofort sichtbar, kein Schimmer-Verlauf, kein Springen, wenn die Daten kommen.
- **Aktualisieren:** alte Werte bleiben stehen, ein Zeitstempel zeigt die Frische.
- **Fehler:** im Block, der fehlschlug, nicht als Seitenbanner. Ein Satz, was fehlschlug und wann
  die Daten zuletzt stimmten, dazu „Erneut versuchen“.
- **Leerer Bereich:** Rahmen und Überschrift bleiben, ein Satz über die ganze Breite
  (`grid-column: 1 / -1`), bei Bedarf ein Link zum Anlegen.
- **Erster Aufruf ohne Daten:** Rahmen und Titel bleiben, die erste Aktion steht dort, wo später die
  Daten stehen.

## §7 Erkennungszeichen generierter Masken (Kür)

Wenn eine Maske „nach KI aussieht“, sind es meist diese: farbige Seitenleiste mit Akzentbalken,
Begrüßung mit Emoji, vier Kennzahlkarten mit Symbol im Farbkreis, Sparklines überall, Regenbogen-
Diagramme, Zebra-Tabelle mit Großbuchstaben-Kopf, gesättigte Statusetiketten mit weißer Schrift,
Akzentfarbe auf jedem Knopf, Blättern unter einer Fünf-Zeilen-Liste, Platzhalterdaten („Max
Mustermann“, „Acme“). Ersatz ist jeweils das Ruhigere aus §2 bis §6.
