#!/usr/bin/env python3
"""Build the isolated Sites pilot from local, pinned inputs. No network or publish."""
from pathlib import Path
import hashlib
import json
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
if OUT.is_symlink():
    raise SystemExit('Refusing a symlinked build directory')
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()
for folder in ('assets', 'downloads', 'mcp-infographic'):
    shutil.copytree(ROOT / folder, OUT / folder)
shutil.copytree(ROOT / 'vendor/compass-suite', OUT / 'compass-suite')
html = (ROOT / 'index.html').read_text()
html = html.replace('https://jonathankhobson.github.io/what-is-an-mcp/', '/')
(OUT / 'index.html').write_text(html)
frame = OUT / 'compass-suite/assets/js/network-frame.js'
js = frame.read_text().replace('https://jonathankhobson.github.io/what-is-an-mcp/', '/')
# This package contains one product page, now mounted at the host root.
js = js.replace('const currentPath = window.location.pathname', 'const currentPath = "/what-is-an-mcp/"')
# Preserve keyboard position when a menu item is hidden by Escape.
js = js.replace('if (event.key === "Escape") close();', 'if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") { close(); toggle.focus(); }')
frame.write_text(js)
# Retain the old path on a future host, with equivalent content and local downloads.
alias = OUT / 'what-is-an-mcp'
alias.mkdir()
(alias / 'index.html').write_text(html.replace('<head>', '<head>\n  <base href="/">'))
for folder in ('downloads', 'mcp-infographic'):
    shutil.copytree(ROOT / folder, alias / folder)
files = []
for p in sorted(OUT.rglob('*')):
    if p.is_file():
        b = p.read_bytes()
        files.append({'path':p.relative_to(OUT).as_posix(), 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest()})
print(json.dumps({'build':'static-local-only', 'files':files}, indent=2))
