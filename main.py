#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line (<=200 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: same bytes on every run, no network, no randomness.
"""

import os

LINE = (
    "Hey kid, the haircut grows back, your crush never texts back, and "
    "those 2am coding sessions you hide from everyone turn out to be the "
    "whole plan \u2014 keep going."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
