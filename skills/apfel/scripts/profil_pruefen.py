#!/usr/bin/env python3
"""Ein Apfel-Profil prüfen: Aufbau und, mit Repo, jede Fundstelle.

    python3 profil_pruefen.py <profil.md>
    python3 profil_pruefen.py <profil.md> --repo <pfad zum repo> --ref <ref>

Unter Windows heißt der Aufruf meist `py` oder `python` statt `python3`.

Ohne --repo: Steckbrief vollständig, alle Grundthemen der Vorlage da, wie viele belegt.
Mit --repo: jede Fundstelle (Pfad in Backticks in der Spalte „Fundstelle“) per `git cat-file -e`
auf dem Ref, erst relativ zum „Ordner des Maßstabs“, dann ab Repo-Wurzel. Der Arbeitsbaum bleibt,
wie er ist; gelesen wird nur aus der Git-Datenbank.
Nur Standardbibliothek, nichts aus dem Netz. Rückgabe 0, wenn alles passt, sonst 1.
"""
import argparse
import datetime
import pathlib
import re
import subprocess
import sys

FELDER = ("Gilt, wenn", "Stände", "Hausmaßstab", "Ordner des Maßstabs", "Stand")
OHNE_PLATZHALTER = ("Gilt, wenn", "Hausmaßstab", "Ordner des Maßstabs", "Stand")
# Nur falls keine Vorlage zu finden ist; maßgeblich ist profile/vorlage.md.
ERSATZ_THEMEN = [
    "Laden am Knopf", "Platzhalter beim Laden", "Navigation", "Kopf", "Feldlayout",
    "Auswahlfelder", "Tabellen", "Texte", "Ungespeichertes", "Speichern, Verwerfen",
    "Validierung", "Löschen", "Meldungen", "Fehler", "Bearbeiten und Rechte",
]


def lies(text):
    """Steckbrief (Tabelle mit Kopf „Feld“) und Themen (Tabellen mit Kopf „Thema“)."""
    steckbrief, themen, kopf = {}, [], None
    for zeile in text.splitlines():
        z = zeile.strip()
        if not (z.startswith("|") and z.endswith("|") and len(z) > 1):
            kopf = None
            continue
        zellen = [c.strip() for c in z[1:-1].split("|")]
        if all(re.fullmatch(r":?-{3,}:?", c) for c in zellen):
            continue
        if kopf is None:
            kopf = zellen[0]
            continue
        if kopf == "Feld" and len(zellen) >= 2:
            steckbrief[zellen[0]] = zellen[1]
        elif kopf == "Thema" and len(zellen) >= 2:
            themen.append((zellen[0], zellen[1]))
    return steckbrief, themen


def pfade(zelle):
    """Pfade in Backticks: mit Schrägstrich oder Dateiendung, ohne Klammern und Leerzeichen."""
    treffer = []
    for t in re.findall(r"`([^`]+)`", zelle):
        if re.fullmatch(r"[\w.\-/]+", t) and ("/" in t or re.search(r"\.[A-Za-z]{1,5}$", t)):
            treffer.append(t.rstrip("/"))
    return treffer


def finde_vorlage(profil):
    skill = pathlib.Path(__file__).resolve().parent.parent
    kandidaten = [profil.parent / "vorlage.md", skill / "profile" / "vorlage.md"]
    if len(skill.parents) >= 3:
        kandidaten.append(skill.parents[2] / "profile" / "vorlage.md")
    for k in kandidaten:
        if k.is_file() and k.resolve() != profil.resolve():
            return k
    return None


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("profil")
    p.add_argument("--repo", help="Repo mit dem Hausmaßstab")
    p.add_argument("--ref", help="Ref des Maßstabs, z. B. origin/release/2026-12 (sonst HEAD)")
    a = p.parse_args()

    profil = pathlib.Path(a.profil)
    if not profil.is_file():
        sys.exit(f"Profil nicht gefunden: {profil}")
    if profil.name == "vorlage.md":
        print("Das ist die Vorlage, kein Profil. Kopieren, füllen, dann diese Datei prüfen.")
        return 0
    text = profil.read_text(encoding="utf-8")
    titel = next((z[2:].strip() for z in text.splitlines() if z.startswith("# ")), profil.name)
    steckbrief, themen = lies(text)
    befunde = 0

    print(f"{titel}  ({profil})")

    fehlt = [f for f in FELDER if f not in steckbrief]
    offen = [f for f in OHNE_PLATZHALTER
             if f in steckbrief and re.search(r"<[^<>]+>|PLATZHALTER", steckbrief[f])]
    if fehlt or offen:
        befunde += len(fehlt) + len(offen)
        if fehlt:
            print("Steckbrief: fehlt " + ", ".join(fehlt))
        if offen:
            print("Steckbrief: noch Platzhalter in " + ", ".join(offen))
    else:
        print("Steckbrief: vollständig")

    vorlage = finde_vorlage(profil)
    kern = [t for t, _ in lies(vorlage.read_text(encoding="utf-8"))[1]] if vorlage else ERSATZ_THEMEN
    namen = [t for t, _ in themen]
    fehlende = [t for t in kern if t not in namen]
    eigene = [t for t in namen if t not in kern]
    leer = [t for t, f in themen if t in kern and f in ("–", "-", "")]
    belegt = len([t for t in kern if t in namen and t not in leer])
    zeile = f"Grundthemen: {belegt} von {len(kern)} belegt"
    if leer:
        zeile += f", ohne Muster im Vorbild: {', '.join(leer)}"
    if eigene:
        zeile += f"; {len(eigene)} eigene dazu"
    print(zeile)
    if fehlende:
        befunde += len(fehlende)
        print("Grundthemen fehlen ganz (Name wie in der Vorlage?): " + ", ".join(fehlende))
    if not vorlage:
        print("  (keine vorlage.md gefunden, Themen aus der eingebauten Liste)")

    if a.repo:
        ref = a.ref or "HEAD"
        rc, commit = git(a.repo, "rev-parse", "--short=10", f"{ref}^{{commit}}")
        if rc != 0:
            sys.exit(f"Ref nicht lesbar in {a.repo}: {ref}")
        _, datum = git(a.repo, "log", "-1", "--format=%cd", "--date=format:%d.%m.%Y", ref)
        ordner = next(iter(pfade(steckbrief.get("Ordner des Maßstabs", ""))), "")
        geprueft, weg = 0, []
        for thema, zelle in themen:
            for pfad in pfade(zelle):
                geprueft += 1
                orte = [f"{ordner}/{pfad}", pfad] if ordner else [pfad]
                if not any(git(a.repo, "cat-file", "-e", f"{ref}:{o}")[0] == 0 for o in orte):
                    weg.append((thema, pfad))
        print(f"Fundstellen auf {ref} @ {commit} ({datum}): {geprueft} geprüft, "
              f"{geprueft - len(weg)} da, {len(weg)} {'fehlt' if len(weg) == 1 else 'fehlen'}")
        for thema, pfad in weg:
            print(f"  fehlt  {thema}: {pfad}")
        if not a.ref:
            print("  (HEAD genommen; besser den Ref aus „Ref des Maßstabs“ angeben)")
        befunde += len(weg)
        heute = datetime.date.today().strftime("%d.%m.%Y")
        if not weg:
            print(f"Vorschlag für „Stand“: {heute}, alle {geprueft} Fundstellen da auf "
                  f"`{ref}` @ `{commit}` ({datum})")

    if befunde == 0:
        print("Ergebnis: passt")
    else:
        print(f"Ergebnis: {befunde} {'Stelle' if befunde == 1 else 'Stellen'} nachsehen")
    return 0 if befunde == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
