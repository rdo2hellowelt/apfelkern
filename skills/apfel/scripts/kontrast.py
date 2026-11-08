#!/usr/bin/env python3
"""Kontrast nach WCAG 2.x messen, nicht schätzen.

    python3 kontrast.py <vordergrund> <hintergrund> [--alpha 0.6]

Farben als #rgb oder #rrggbb. --alpha legt den Vordergrund mit dieser Deckkraft
über den Hintergrund (für rgba-Text, gesperrte Felder mit opacity).
Ausgabe: Verhältnis und Urteil für Text (4.5:1), große Schrift und Bedienelemente (3:1).
Nur Standardbibliothek, liest nichts aus dem Netz.
"""
import argparse
import sys


def hex_rgb(s: str) -> tuple[float, float, float]:
    h = s.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        sys.exit(f"Farbe nicht lesbar: {s}")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminanz(rgb) -> float:
    def kanal(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (kanal(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def mischen(fg, bg, alpha):
    return tuple(alpha * f + (1 - alpha) * b for f, b in zip(fg, bg))


def verhaeltnis(fg, bg) -> float:
    a, b = sorted((luminanz(fg), luminanz(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("vordergrund")
    p.add_argument("hintergrund")
    p.add_argument("--alpha", type=float, default=1.0)
    a = p.parse_args()
    fg, bg = hex_rgb(a.vordergrund), hex_rgb(a.hintergrund)
    if a.alpha < 1:
        fg = mischen(fg, bg, a.alpha)
    v = verhaeltnis(fg, bg)
    ok = lambda grenze: "erfüllt" if v >= grenze else "Befund"
    print(f"{a.vordergrund} auf {a.hintergrund}"
          + (f" (Deckkraft {a.alpha})" if a.alpha < 1 else "")
          + f": {v:.2f}:1")
    print(f"  Text 4.5:1                 {ok(4.5)}")
    print(f"  große Schrift, Elemente 3:1 {ok(3.0)}")


if __name__ == "__main__":
    main()
