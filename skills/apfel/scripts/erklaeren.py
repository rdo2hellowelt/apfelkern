#!/usr/bin/env python3
"""Erklärblatt für Apfel bauen (SKILL.md §7).

Liest SKILL.md (Prüfpunkte, Rangfolge, Pflege), den Profilordner, die Probeläufe und die jüngste
Befundzeichnung im Apfel-Ordner, füllt assets/erklaer-vorlage.html und schreibt
apfel-erklaert-<JJJJ-MM-TT>.html in den Apfel-Ordner. Nur Standardbibliothek, liest git.

  python3 erklaeren.py [--artefakt] [--ziel <ordner>] [--aus <datei>]
"""
import argparse, base64, datetime, glob, html, json, os, re, subprocess, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORDNER = os.path.expanduser("~/Documents/Apfel")
GRUPPEN = ("Motor", "Fahrwerk", "Bremse")


def inline(t):
    """Markdown-Zeile in HTML: **fett**, `code`, sonst escapen."""
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"`([^`]+)`", r'<span class="mono">\1</span>', t)


def pruefpunkte(md):
    punkte, gruppen = [], {}
    for g in GRUPPEN:
        m = re.search(rf"^#### {g}: ([^\n]+)\n(.*?)(?=^#{{2,4}} )", md, re.M | re.S)
        if not m:
            sys.exit(f"Abschnitt '#### {g}: …' nicht gefunden. Skript an SKILL.md anpassen.")
        gruppen[g] = m.group(1).strip()
        for zeile in m.group(2).splitlines():
            z = [c.strip() for c in zeile.strip().strip("|").split("|")]
            if len(z) != 4 or z[1] not in ("H", "K"):
                continue
            text = re.sub(r"`([^`]+)`", r"\1", z[0])
            quelle = re.sub(r"`([^`]+)`", r"\1", z[3]).replace(", HIG:", " · HIG:")
            punkte.append([g, text, z[1], z[2], quelle])
    if not punkte:
        sys.exit("Keine Prüfpunkte gelesen.")
    return punkte, gruppen


def rangfolge(md):
    m = re.search(r"\*\*Rangfolge für Haus 1:1\*\*.*?\n\n(.*?)\n\n", md, re.S)
    if not m:
        sys.exit("Liste nach 'Rangfolge für Haus 1:1' nicht gefunden.")
    regeln = [" ".join(x.split()) for x in re.split(r"\n(?=\d+\. )", m.group(1).strip())]
    li = []
    for r in regeln:
        r = re.sub(r"^\d+\.\s*", "", r)
        if "gehört nicht in Haus 1:1" in r or "geht nach plus" in r:
            ziel, cls = "plus", " p"
        elif "bleibt so" in r:
            ziel, cls = "bleibt", ""
        else:
            ziel, cls = "Haus 1:1", ""
        li.append(f'<li><span>{inline(r)}<span class="to{cls}">{ziel}</span></span></li>')
    return "\n      ".join(li), len(regeln)


def profile():
    """Eigene Profile aus dem Profilordner (<Apfel-Ordner>/profile), sonst das mitgelieferte Beispiel."""
    out = []
    eigene = sorted(glob.glob(os.path.join(ORDNER, "profile", "*.md")))
    for p in eigene or [os.path.join(SKILL, "profile", "beispiel.md")]:
        name = os.path.basename(p)
        if name in ("vorlage.md", "LIESMICH.md", "INTERN.md") or not os.path.exists(p):
            continue
        t = open(p, encoding="utf-8").read()
        titel = re.search(r"^# Profil (.+)$", t, re.M)
        mass = re.search(r"^\| Hausmaßstab \| (.+?) \|", t, re.M)
        stand = re.search(r"^\| Stand \| (.+?) \|", t, re.M)
        fund = re.search(r"alle (\d+) Fundstellen", stand.group(1) if stand else "")
        out.append({"datei": name, "titel": titel.group(1) if titel else name[:-3],
                    "mass": mass.group(1) if mass else "–",
                    "fund": f"{fund.group(1)} Fundstellen" if fund else "Fundstellen je Thema"})
    return out


def laeufe():
    karten, minuten, usd = [], [], []
    for f in sorted(glob.glob(os.path.join(ORDNER, "probelaeufe", "*", "probelauf-bericht.md"))):
        t = open(f, encoding="utf-8").read()
        for m in re.finditer(r"^\| (\d+) \| ([^|]+?) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| ([\d.]+) \|$", t, re.M):
            nr, was, rf, sv, runden, sek, kosten = m.groups()
            mi, us = int(sek) / 60, float(kosten)
            minuten.append(mi); usd.append(us)
            karten.append((int(nr), f'''<div class="run"><h3>Fall {nr} · {html.escape(was)}</h3>
          <div><span class="cap">Min</span><b>{mi:.1f}</b></div><div><span class="cap">USD</span><b>{us:.2f}</b></div><div><span class="cap">Runden</span><b>{runden}</b></div><div><span class="cap">Rückfr.</span><b>{rf}</b></div>
          <p>{sv} Schreibversuche außerhalb der Freigabe.</p></div>'''.replace(f"<b>{mi:.1f}</b>", f"<b>{mi:.1f}</b>".replace(".", ",")).replace(f"<b>{us:.2f}</b>", f"<b>{us:.2f}</b>".replace(".", ","))))
    karten.sort()
    if not karten:
        return '<p style="font-size:.9rem">Noch keine Probeläufe im Apfel-Ordner.</p>', "EIN LAUF · NUR CODE"
    de = lambda x: f"{x:.1f}".replace(".", ",")
    schnitt = f"EIN LAUF · NUR CODE · Ø {de(sum(minuten)/len(minuten))} MIN · Ø {sum(usd)/len(usd):.2f} USD".replace(".", ",")
    return "\n        ".join(k for _, k in karten), schnitt


def zeichnung():
    pngs = glob.glob(os.path.join(ORDNER, "**", "apfel-zeichnung-*.png"), recursive=True)
    if not pngs:
        return '<p class="cap">Noch keine Befundzeichnung im Apfel-Ordner. „apfel zeichnung &lt;dialog&gt;“ legt eine an.</p>'
    p = max(pngs, key=os.path.getmtime)
    b64 = base64.b64encode(open(p, "rb").read()).decode()
    rel = os.path.relpath(p, ORDNER)
    datum = re.search(r"(\d{4}-\d{2}-\d{2})", rel)
    d = datetime.date.fromisoformat(datum.group(1)).strftime("%d.%m.%Y") if datum else ""
    dialog = re.sub(r"^apfel-zeichnung-|-\d{4}-\d{2}-\d{2}\.png$", "", os.path.basename(p)).replace("-", " ")
    return f'''<figure>
    <div class="img"><img src="data:image/png;base64,{b64}" alt="Jüngste Befundzeichnung: {html.escape(dialog)}"></div>
    <figcaption>Jüngste Befundzeichnung im Apfel-Ordner: {html.escape(dialog)}, {d}, Datei <span class="mono">{html.escape(rel)}</span>. Auf schmalen Bildschirmen seitlich scrollen.</figcaption>
  </figure>'''


def git(*args):
    try:
        return subprocess.run(["git", "-C", SKILL, *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main():
    global ORDNER
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    a.add_argument("--artefakt", action="store_true", help="ohne <!doctype>/<html>/<head>/<body>")
    a.add_argument("--ziel", default=ORDNER, help="Apfel-Ordner (Standard ~/Documents/Apfel)")
    a.add_argument("--aus", help="Ausgabedatei statt apfel-erklaert-<datum>.html im Ziel")
    o = a.parse_args()
    ORDNER = os.path.expanduser(o.ziel)

    md = open(os.path.join(SKILL, "SKILL.md"), encoding="utf-8").read()
    vorlage = open(os.path.join(SKILL, "assets", "erklaer-vorlage.html"), encoding="utf-8").read()
    punkte, gruppen = pruefpunkte(md)
    regeln_html, n_regeln = rangfolge(md)
    pf = profile()
    pflege = re.search(r"nächste Prüfung (\d\d\.\d\d\.\d{4})", md)
    laeufe_html, schnitt = laeufe()
    commit = git("log", "-1", "--format=%h")
    stand = git("log", "-1", "--format=%cd", "--date=format:%d.%m.%Y")
    if git("status", "--porcelain"):
        commit += " + Änderungen"
    heute = datetime.date.today()
    erster = pf[0] if pf else {"datei": "kein Profil", "fund": "Hausmaßstab", "titel": "", "mass": ""}

    werte = {
        "STAND": stand or heute.strftime("%d.%m.%Y"),
        "HEUTE": heute.strftime("%d.%m.%Y"),
        "COMMIT": commit or "ohne Git",
        "ZEILEN": str(md.count("\n")),
        "N_PP": str(len(punkte)),
        "N_MOTOR": str(sum(p[0] == "Motor" for p in punkte)),
        "N_FAHRWERK": str(sum(p[0] == "Fahrwerk" for p in punkte)),
        "N_BREMSE": str(sum(p[0] == "Bremse" for p in punkte)),
        "N_REGELN": str(n_regeln),
        "PFLEGE": pflege.group(1) if pflege else "–",
        "PROFIL_DATEI": erster["datei"],
        "PROFIL_FUND": erster["fund"],
        "PROFILE_LISTE": ", ".join(f'{html.escape(p["titel"])} (Maßstab: {html.escape(p["mass"])})' for p in pf) or "noch keins, „apfel profil“ legt eins an",
        "PROFILE_KURZ": "vorlage, beispiel, LIESMICH",
        "LAUF_SCHNITT": schnitt,
        "LAEUFE": laeufe_html,
        "RANGFOLGE": regeln_html,
        "PRUEFPUNKTE_JSON": json.dumps(punkte, ensure_ascii=False).replace("</", "<\\/"),
        "GRUPPEN_JSON": json.dumps(gruppen, ensure_ascii=False),
        "ZEICHNUNG": zeichnung(),
    }
    seite = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: werte[m.group(1)], vorlage)
    offen = re.findall(r"\{\{[A-Z_]+\}\}", seite)
    if offen:
        sys.exit(f"Platzhalter ohne Wert: {offen}")
    if not o.artefakt:
        seite = ('<!doctype html>\n<html lang="de">\n<head>\n<meta charset="utf-8">\n'
                 '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                 + seite + "\n</html>\n")
    ziel = os.path.expanduser(o.aus) if o.aus else os.path.join(ORDNER, f"apfel-erklaert-{heute.isoformat()}.html")
    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    open(ziel, "w", encoding="utf-8").write(seite)
    print(ziel)
    print(f"{len(punkte)} Prüfpunkte ({werte['N_MOTOR']}/{werte['N_FAHRWERK']}/{werte['N_BREMSE']}), "
          f"{n_regeln} Regeln, {len(pf)} Profil(e), Skill {werte['COMMIT']}")


if __name__ == "__main__":
    main()
