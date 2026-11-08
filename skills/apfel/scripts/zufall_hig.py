#!/usr/bin/env python3
"""Eine zufällige Seite aus references/hig-seiten.md, für den Weg „Auf gut Glück“.

    python3 zufall_hig.py      (unter Windows: py zufall_hig.py oder python zufall_hig.py)

Gibt den Seitennamen, die Adresse für Menschen und die Markdown-Adresse zum Laden aus. Nur Standardbibliothek.
"""
import pathlib
import random
import re

LISTE = pathlib.Path(__file__).resolve().parent.parent / "references" / "hig-seiten.md"
BASIS = "https://developer.apple.com/design/human-interface-guidelines/"

text = LISTE.read_text(encoding="utf-8")
teil = text.split("## Seiten nach Baugruppe", 1)[-1]
seiten = sorted(set(re.findall(r"^\| `([a-z-]+)`", teil, flags=re.M)))
seite = random.choice(seiten)
print(seite)
print(BASIS + seite)
print(BASIS + seite + ".md")
