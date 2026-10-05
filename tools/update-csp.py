#!/usr/bin/env python3
"""Herberekent de SHA-256-hash van het inline script in index.html en zet die in de
Content-Security-Policy. Draai dit na elke wijziging in het script:

    python3 tools/update-csp.py          # bijwerken
    python3 tools/update-csp.py --check  # alleen controleren (bijv. in CI)
"""
import base64, hashlib, pathlib, re, sys

path = pathlib.Path(__file__).resolve().parent.parent / "index.html"
html = path.read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
if len(scripts) != 1:
    sys.exit(f"Verwacht precies 1 inline <script>, gevonden: {len(scripts)}")
digest = "sha256-" + base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
current = re.search(r"script-src '(sha256-[A-Za-z0-9+/=]+)'", html)
if not current:
    sys.exit("Geen script-src met sha256 gevonden in de CSP")
if "--check" in sys.argv:
    if current.group(1) != digest:
        sys.exit(f"CSP-hash klopt niet.\n  in bestand: {current.group(1)}\n  berekend:   {digest}\nDraai: python3 tools/update-csp.py")
    print("CSP-hash klopt:", digest)
else:
    path.write_text(html.replace(current.group(1), digest), encoding="utf-8")
    print("CSP bijgewerkt:", digest)
