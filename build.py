#!/usr/bin/env python3
"""Wrap the artifact-authored deck into a standalone page for GitHub Pages.

The source in src/deck.artifact.html has no <!doctype>, <html>, <head> or <body>
because the Claude artifact runtime supplies them. Pages does not, so this adds
the document shell, the viewport meta the mobile layout depends on, and the small
reset the artifact wrapper would otherwise provide.
"""
import pathlib, re

SRC = pathlib.Path("src/deck.artifact.html")
OUT = pathlib.Path("index.html")

RESET = """<style>
  :root{color-scheme:light dark}
  html{-webkit-text-size-adjust:100%}
  body{margin:0}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>"""

src = SRC.read_text(encoding="utf-8")
i = src.index("</style>") + len("</style>")
head, body = src[:i], src[i:]

title = re.search(r"<title>(.*?)</title>", head).group(1)

OUT.write_text(
    "<!doctype html>\n"
    '<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Agentic AI for construction design delivery: the 100-step drawing process, an agent framework over a governed parameter graph, and a 22-week proof of concept.">\n'
    f'<meta property="og:title" content="{title}">\n'
    f"{RESET}\n"
    f"{head.strip()}\n"
    "</head>\n<body>\n"
    f"{body.strip()}\n"
    "</body>\n</html>\n",
    encoding="utf-8",
)
print(f"built {OUT} ({OUT.stat().st_size:,} bytes) from {SRC}")
