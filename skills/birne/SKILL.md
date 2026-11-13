---
name: birne
description: |-
  Birne zeichnet. Sie macht aus einem Stoff (Aufbau mit Wegen, Ablauf mit Zeitpunkten, Probe, Befund,
  Projektstand) ein technisches Blatt nach DIN, Tusche auf Weiß: Rahmen mit Zonen und Mittenmarken
  (DIN EN ISO 5457), kleines Schriftfeld unten rechts (DIN EN ISO 7200), Linienarten statt Farbe
  (DIN EN ISO 128), Beschriftung in DIN 1451, eckig, Kanten leicht überzeichnet, Texte im Blocksatz.
  Bausteine: Draufsicht, Schnitt, Detail, Explosionsansicht, Zeitachse, Tabellen. Apfel zeichnet
  seine Befunde auf demselben Blatt. Nicht für Farbdiagramme, Dashboards, Folien oder Seiten zum Lesen.
  MUST BE USED when user says: "birne", "Birne", "werkzeichnung", "tusche", "tuschezeichnung",
  "cad-stil", "technisches blatt", "din-zeichnung", "zeichne das als blatt".
---

# Birne

Ein Blatt zeigt, wie etwas aufgebaut ist und welchen Weg es nimmt, so wie eine Maschinenbau-, Architektur- oder
Elektrozeichnung. Die Striche tragen die Bedeutung, nicht die Farbe.

Apfel prüft, Birne zeichnet. Das Plugin apfel trägt eine Kopie von Birne in sich und zeichnet seine Befunde damit.
Geändert wird nur in birnenkern, dann die Kopie nachziehen (`QUELLEN.md`).

## Wann, wann nicht

- **Ja:** ein Zusammenhang soll auf ein Blatt. Aufbau mit Wegen, Ablauf mit Zeitpunkten, Befunde an ihrer Stelle,
  Stand eines Vorhabens mit Wartepunkten.
- **Nein:** Zahlenreihen als Diagramm, Folien, Fließtext zum Lesen. Dafür gibt es andere Werkzeuge.

## Ablauf

1. **Stoff sammeln.** Jede Zahl, jede Uhrzeit, jeder Stand hat eine Fundstelle (Protokoll, Ticket, Commit). Was nicht
   belegt ist, kommt nicht aufs Blatt.
2. **Anordnen.** Erst auf Papier oder im Kopf: Was ist die Hauptansicht, welcher Weg braucht einen Schnitt, welche
   Stelle ein Detail, gibt es eine Zeitachse. Ein Blatt, nicht mehr.
3. **Bauen.** `assets/blatt-vorlage.html` nach `birne-<thema>-<JJJJ-MM-TT>.html` kopieren, im Arbeitsordner oder wo der
   Auftrag es sagt. `<title>` setzen (ein Name aus zwei bis vier Wörtern), das
   `aria-label` am `svg` anpassen, den Block ZEICHNUNG neu schreiben. Die Blöcke WERKZEUG und BLATT bleiben, wie sie
   sind. Das Beispiel in der Vorlage, eine erfundene Probe Ende zu Ende (Ausleihe einer Stadtbibliothek), ist
   das Muster.
4. **Einmal ansehen.** Das Blatt rendern (Browser oder Headless-Chrome mit Bildschirmfoto), Überlappungen und
   Überläufe suchen, einmal nachbessern. Keine Schleife.
5. **Ausliefern.** Datei öffnen (Mac `open <datei>`, Windows `start <datei>`, PowerShell `Invoke-Item <datei>`). Wo
   Artifacts zur Verfügung stehen und das Blatt gezeigt werden soll, als privates Artifact veröffentlichen.

## Das Blatt

Raster 1700 × 1060, Zeichenfläche im Rahmen von 20 bis 1680 und 20 bis 1040. Die Reihenfolge im Block ZEICHNUNG:

```js
starten(function(){
 begin('sh1'); rahmen();                       // Blattrand, Zonen 1–8 und A–F, Mittenmarken
 sprache('en');                                // nur für ein englisches Blatt, sonst weglassen
 hinweise('(Untertitel)', ['Ziel: …', 'Steht: …', 'Offen: …']);   // oben links, Blocksatz
 /* Hauptansicht in der Mitte, Details links, Zeitachse und Schnitte unten, Tabellen rechts */
 legende(1330, y, 340, [['voll','durch'],['offen','offen'],['schraffiert','Störung'],['K','Schritt']], 'Text …');
 schriftfeld({abt, quelle, art, status, titel, zusatz, nr, massstab, refLabel, ref, aend, datum});
 tusche();                                     // als Letztes: eckig, Kanten überzeichnen
});
```

- **Schriftfeld** belegt x 1320 bis 1680, y 962 bis 1040. Darüber nichts zeichnen. Die Legende braucht rund 120 darüber;
  ist der Platz rechts voll, die Linienarten als zwei Zeilen in die Hinweise oben links schreiben.
- **Sprache:** Deutsch ohne Aufruf. `sprache('en')` gleich nach `rahmen()` stellt die festen Wörter um: Hinweise,
  Allgemeine Hinweise, alle Felder im Schriftfeld. Die eigenen Texte schreibt der Block ZEICHNUNG in derselben Sprache.
- **Hinweise oben links:** was das Blatt zeigt, was steht, was offen ist. Erst was geht, dann der Vorbehalt.
- **Hauptansicht** (Draufsicht) mit Schnittlinie A–A, wenn ein Weg zählt; der Schnitt steht unten mit denselben
  Buchstaben an den Enden.
- **Details** vergrößern eine Stelle, je Detail ein Titel mit `title(x, y, 'Detail A · …', 'Untertitel')`.
- **Zeitachse** mit fester Skala (eine Stunde gleich viele Einheiten), Störungen schraffiert, Ereignisse mit Kennung.
- **Tabellen** rechts: Schritte oder Vorschläge, Befunde mit Ticket-Links, Kennwerte, Quellen.
- **Kennungen** (`nk`) sind in Zeichnung und Tabellen dieselben.

## Linien und Flächen

| Klasse | Strich | Bedeutung |
|---|---|---|
| `obj`, `obj1` | voll, Körperkante | steht, ist durch, Bauteil |
| `hug` | voll, grau gefüllt | Bedienteil, Knopf, Feld, fester Block |
| `slot` | gestrichelt | Platzhalter, Bereich ohne Inhalt |
| `vor` | Strich-Punkt | offen, Vorschlag, Soll |
| `hat()` | schraffiert | gesperrt, Störung, fehlt, überschrieben |
| `cut` | breit | Weg im Schnitt, Sperre, Zeitachse |
| `cl` | dünn Strich-Punkt | Schnittlinie, Mittellinie |
| `dl` mit Pfeil | dünn | Fluss, Maßlinie |

Linien bleiben dünn. Nur Grau, bewusst nur hell.

## Schrift und Text

- Schrift-Stapel: DIN 1451 Mittelschrift (wo installiert), DIN Alternate, Bahnschrift, Barlow Semi Condensed als
  Ersatz aus Google Fonts. Großbuchstaben über die Klassen.
- Texte über mehr als eine Zeile mit `absatz()` im Blocksatz; einzelne Zeilen mit `tx()`. Kurze Hauptsätze, keine
  Gedankenstriche.
- `starten()` wartet auf die Schrift, sonst misst der Blocksatz mit der Ersatzschrift.

## Inhalt

- Keine Namen, keine Kürzel von Personen, keine Hostnamen und keine internen Pfade. Rollen statt Personen (Betrieb,
  Prüfung). Die Marke steht im Schriftfeld unter „Verantw. Abt.“ (Feld `abt`).
- Jede Zahl mit Fundstelle, die Tabelle Quellen nennt sie. Interne Unterlagen stehen dort als „intern“.
- Keine Lücken markieren, nach denen keiner fragt. Keine Selbstkorrektur auf dem Blatt: es trägt den Stand.
- Keine erfundenen Maße. Proportionen schematisch, Zahlen nur, wenn sie belegt sind.

## Werkzeug

**WERKZEUG** (nach dimensional-drawing, MIT): `begin(id)`, `mk(tag, attr, parent)`, `tx(x, y, text, klasse, attr)`,
`rr(x, y, w, h, r, klasse)`, `hat(x, y, w, h)`, `ar(x1, y1, x2, y2, klasse)`, `dimH(x1, x2, y, e1, e2, text, opt)`,
`dimV(…)`, `callout(…)`, `nb(x, y, n)`, `slotLabel(x, y, w, h, text, ausrichtung, klasse)`, `title(x, y, titel,
untertitel)`, `detailRef(…)`, `xbox(x, y, w, h)`, `notes(liste)`, `table(x, y, titel, kopf, zeilen, breiten, ausrichtung)`.

**BLATT** (Birne): `nk(x, y, kennung)` Kästchen, das mitwächst · `zwei(x, y, w, h, a, b)` zwei Zeilen im Kasten ·
`absatz(x, y, w, text, klasse, zeilenabstand)` Blocksatz, gibt das y darunter zurück · `rahmen()` ·
`hinweise(untertitel, absätze, breite)` · `legende(x, y, w, arten, text)` mit den Arten `voll`, `offen`,
`platzhalter`, `schraffiert`, `grau` oder einer Kennung · `schriftfeld(felder)` · `sprache(code)` mit `de` oder `en` ·
`tusche()` · `starten(fn)`.

Eine Gruppe verschieben, ohne jede Zahl anzufassen: `{const keep=sv; sv=mk('g',{transform:'translate(0,-36)'}); … sv=keep;}`.
`tusche()` überzeichnet auch dort richtig.

## Dateien

| Datei | Inhalt |
|---|---|
| `assets/blatt-vorlage.html` | Blatt mit WERKZEUG, BLATT und als Muster die erfundene Probe Ende zu Ende |
| `references/din.md` | Die Normen kurz: Blatt, Schriftfeld, Linienarten, Schrift |
| `evals/evals.json` | Prüffälle: wann Birne greift, wann nicht |
| `QUELLEN.md` | Herkunft, Lizenzen, Änderungen |
| `LICENSE` | MIT, für Birne selbst |
| `LICENSES/` | MIT-Text des Zeichenwerkzeugs |

## Pflege

Prüffrist 90 Tage, **nächste Prüfung 11.02.2027**: Muster gegen das jüngste Blatt halten, Schrift-Stapel prüfen,
`references/din.md` gegen die Normen lesen.
