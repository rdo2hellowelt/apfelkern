# Profil Kundenkartei (Beispiel)

_Erfunden, zum Ansehen. So sieht ein ausgefülltes Profil aus: eine React-App „Kundenkartei“, deren
Adressdialog das Vorbild für alle neuen Dialoge ist. Eigene Profile gehören nach
`~/Documents/Apfel/profile/` oder ins Projekt als `.apfel/profil.md`, nicht hierher._

| Feld | Wert |
|---|---|
| Gilt, wenn | Remote enthält `kundenkartei` oder es gibt `src/dialoge/adresse/` |
| Stände | Bestand · Haus 1:1 · plus |
| Hausmaßstab | Adressdialog (`src/dialoge/adresse/`) |
| Ordner des Maßstabs | `src/`, die Fundstellen unten sind relativ dazu |
| Ref des Maßstabs | jüngster Zweig `release/*` |
| Oberfläche | `src/dialoge/` |
| Stand | 08.11.2026, Beispiel ohne echtes Repo, Fundstellen nicht geprüft |

## Codebasen

- **Geprüfter Dialog (NEU):** Zweig des Auftrags, `src/dialoge/<dialog>/`.
- **Hausmaßstab (HAUS):** `src/dialoge/adresse/` und die gemeinsamen Bausteine in `src/bausteine/`, auf dem Ref oben.
- **Bestand (ALT):** die alte Fassung unter `legacy/` (jQuery), sonst „neu“.
- **Code lesen** nur, ohne den Arbeitsbaum zu ändern: `git show <ref>:<pfad>`, `git grep <muster> <ref>`.
- **Fundstellen-Präfixe:** `NEU:`, `HAUS:`, `ALT:`.

## Grenzen

- Keinen Dev-Server starten, keine Abhängigkeiten installieren.
- `scripts/seed-db.sh` nie ausführen, es überschreibt die Testdatenbank.

## Hausmaßstab: Fundstellen je Thema

### Motor

| Thema | Fundstelle | Muster |
|---|---|---|
| Laden am Knopf | `bausteine/Knopf.tsx` | `laedt` setzt Kreisel und `disabled`, die Breite bleibt. |
| Platzhalter beim Laden | `bausteine/Skelett.tsx` | Skelett in der Form des späteren Inhalts, bis die Daten da sind. |

### Fahrwerk

| Thema | Fundstelle | Muster |
|---|---|---|
| Navigation | `bausteine/Seitenleiste.tsx` | Seitenleiste mit einer Ebene, aktiver Eintrag mit Balken und `aria-current`. |
| Kopf | `dialoge/adresse/Kopf.tsx` | Titel links, Aktionen rechts, Speichern ganz rechts. |
| Feldlayout | `bausteine/Feld.tsx` | Beschriftung über dem Feld, Hilfetext darunter, Fehler ersetzt den Hilfetext. |
| Auswahlfelder | `bausteine/Auswahl.tsx` | Ab sieben Einträgen mit Suche, sonst einfache Liste. |
| Tabellen | `bausteine/Tabelle.tsx` | Filterzeile über der Tabelle, Gesamtzahl links, Kopf bleibt stehen. |
| Texte | `texte/de.json` | Alle Texte zentral, Schlüssel nach Dialog und Zweck. |

### Bremse

| Thema | Fundstelle | Muster |
|---|---|---|
| Ungespeichertes | `bausteine/useVerlassenSchutz.ts` | Jeder Weg aus der Ansicht fragt „Speichern und verlassen“ oder „Verwerfen und verlassen“. |
| Speichern, Verwerfen | `dialoge/adresse/Fussleiste.tsx` | Beide Knöpfe nur aktiv, wenn etwas geändert ist. |
| Validierung | `dialoge/adresse/pruefung.ts` | Fehler blockieren, Warnungen erlauben „Trotzdem speichern“. |
| Löschen | `bausteine/Rueckfrage.tsx` | Rückfrage nennt Objekt und Folge, Bestätigen ist rot. |
| Meldungen | `bausteine/Meldung.tsx` | Kurze Meldung oben rechts, Fehler bleiben, bis man sie schließt. |
| Fehler | `api/fehlertext.ts` | Serverfehler als Satz mit Ausweg, nie der rohe Antwortrumpf. |
| Bearbeiten und Rechte | – | – |

## Beispielzeilen für den Bericht

| Nr | Baugruppe | Bestand | Haus 1:1 | plus | Aufwand | Fundstelle Code | HIG-Seite |
|---|---|---|---|---|---|---|---|
| 1 | Bremse | fragt beim Verlassen | Seitenleiste verlässt ohne Rückfrage. Regel 1, Schutz wie `HAUS:bausteine/useVerlassenSchutz.ts` | wie Haus 1:1 | S | `NEU:src/dialoge/auftrag/Auftrag.tsx` | feedback |
| 2 | Fahrwerk | neu | wie Bestand | Gesamtzahl über der Tabelle, tief hängend, Arbeitsmasken §2 | S | `NEU:src/dialoge/auftrag/Liste.tsx` | lists-and-tables |
