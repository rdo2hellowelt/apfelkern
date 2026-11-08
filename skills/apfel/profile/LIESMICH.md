# Profile

Ein Profil sagt Apfel, woran sich ein Projekt misst. Eine Markdown-Datei je Projekt, zum Lesen und
zum Ändern von Hand.

**Was drinsteht:** woran Apfel das Repo erkennt, wo die Oberfläche liegt, welcher Dialog oder
welches Design-System das Vorbild ist, was nicht geöffnet werden darf, und je Thema (Speichern,
Löschen, Tabellen und zwölf weitere) eine Fundstelle im Vorbild mit dem Muster in einem Satz.

**Ohne Profil** prüft Apfel trotzdem, dann gegen Apples Regeln und die eigenen Prüfpunkte, ohne
Hausmaßstab.

| Datei | Was |
|---|---|
| `vorlage.md` | leeres Profil zum Füllen |
| `beispiel.md` | erfundene Kundenkartei, so sieht ein fertiges Profil aus |

**Eigene Profile** liegen nicht hier, sondern in `~/Documents/Apfel/profile/` (im Finder
„Dokumente/Apfel/profile“). So bleiben sie privat und überleben jede neue Fassung von Apfel.

## Was man damit macht

Alles über `apfel profil` im Terminal, oder von Hand:

- **Neu anlegen:** „Neu“ wählen. Apfel stellt vier Fragen und sucht die Fundstellen im Vorbild
  selbst. Von Hand: `vorlage.md` kopieren und füllen.
- **Prüfen:** zeigt, ob alle Themen da sind und ob jede Fundstelle im Repo noch existiert. Dateien
  wandern, Profile altern; einmal im Quartal reicht.
- **Verbessern:** füllt Themen mit „–“, zieht gewanderte Fundstellen nach. Apfel zeigt vorher und nachher und schreibt erst nach einem Ja.
- **Weitergeben:** Die eine Datei genügt. Vorher schaut Apfel, ob interne Adressen, Zugangsdaten
  oder Namen drinstehen.
- **Übernehmen:** Datei in `~/Documents/Apfel/profile/` ablegen, oder „Übernehmen“ wählen, dann prüft Apfel sie vorher und
  zeigt die Grenzen.

## Profil im Projekt

Liegt im geprüften Repo eine Datei `.apfel/profil.md`, nimmt Apfel die vor allen anderen. So hat das
ganze Team denselben Maßstab, und Verbesserungen laufen über Merge Requests wie jeder andere Code.
Apfel liest sie nur; ins Repo legen tut sie, wer das Repo pflegt.
