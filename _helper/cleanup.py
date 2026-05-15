"""Remove intermediate build files (.aux, .log, .tex, .out, .typ).

Called by Quarto as a pre-render script (see _quarto.yml).
Skips .pixi, .git, .quarto, and _helper directories — .quarto holds
the cached Typst package downloads (e.g. fontawesome) that must
survive between renders.
"""

import pathlib

SKIP_DIRS = {".pixi", ".git", ".quarto", "_helper"}

for p in pathlib.Path(".").rglob("*"):
    if p.suffix in {".aux", ".log", ".tex", ".out", ".typ"} and SKIP_DIRS.isdisjoint(p.parts):
        p.unlink()
