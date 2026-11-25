#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun one-liner entry.

Writes a single line roasting a smart fridge to /output/entry.txt.
"""

import os
from pathlib import Path

# One line, at most 200 characters, no trailing newline in the output.
LINE = "My smart fridge installed a firmware update at 3 a.m. and now the ice maker only dispenses lukewarm apologies."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
