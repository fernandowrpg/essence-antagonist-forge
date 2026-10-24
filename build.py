#!/usr/bin/env python3
"""Build Essence Antagonist Forge into docs/ (GitHub Pages).

Usage: python3 build.py
Reads  src/index.template.html + data/exalted-essence-antagonist-library.json
Writes docs/index.html (single self-contained page) and docs/library.json
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src" / "index.template.html"
DATA = ROOT / "data" / "exalted-essence-antagonist-library.json"
OUT = ROOT / "docs"

HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
"""

def main():
    lib = json.loads(DATA.read_text(encoding="utf-8"))
    payload = json.dumps(lib, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = SRC.read_text(encoding="utf-8")
    if "__DATA__" not in tpl:
        raise SystemExit("Template is missing the __DATA__ placeholder")
    body = tpl.replace("__DATA__", payload)
    # template starts with <title>, <link> and <style>; they belong in <head>
    split = body.index("</style>") + len("</style>")
    html = HEAD + body[:split] + "\n</head>\n<body>\n" + body[split:] + "\n</body>\n</html>\n"
    OUT.mkdir(exist_ok=True)
    # newline="\n" keeps LF output when building on Windows
    (OUT / "index.html").write_text(html, encoding="utf-8", newline="\n")
    (OUT / "library.json").write_text(json.dumps(lib, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    c = lib["meta"]["counts"]
    print(f"docs/index.html  {len(html)//1024} KB  ({c['charms']} charms, {c['modes']} modes, {c['qualities']} qualities)")

if __name__ == "__main__":
    main()
