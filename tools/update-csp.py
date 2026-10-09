#!/usr/bin/env python3
"""Herberekent de SHA-256-hash van het inline script in index.html en zet die in de
Content-Security-Policy, zowel in index.html (meta-tag) als in _headers (HTTP-header).
Draai dit na elke wijziging in het script:

    python3 tools/update-csp.py          # bijwerken
    python3 tools/update-csp.py --check  # alleen controleren (bijv. in CI)
"""
import base64, hashlib, pathlib, re, sys

root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
scripts = re.findall(r"<script>(.*?)</script>", html, flags=re.S)
if len(scripts) != 1:
    sys.exit(f"Verwacht precies 1 inline <script>, gevonden: {len(scripts)}")
digest = "sha256-" + base64.b64encode(hashlib.sha256(scripts[0].encode("utf-8")).digest()).decode()
pat = re.compile(r"script-src '(sha256-[A-Za-z0-9+/=]+)'")
files = [p for p in (root / "index.html", root / "_headers") if p.exists()]
bad = []
for p in files:
    text = p.read_text(encoding="utf-8")
    m = pat.search(text)
    if not m:
        sys.exit(f"Geen script-src met sha256 gevonden in {p.name}")
    if m.group(1) != digest:
        bad.append(p.name)
        if "--check" not in sys.argv:
            p.write_text(text.replace(m.group(1), digest), encoding="utf-8")
if "--check" in sys.argv:
    if bad:
        sys.exit(f"CSP-hash klopt niet in: {', '.join(bad)} (berekend: {digest}). Draai: python3 tools/update-csp.py")
    print("CSP-hash klopt in", ", ".join(p.name for p in files) + ":", digest)
else:
    print("Bijgewerkt:", ", ".join(bad) or "niets (al actueel)", "->", digest)
