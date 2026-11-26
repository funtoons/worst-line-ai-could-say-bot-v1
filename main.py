#!/usr/bin/env python3
"""Worst line an AI could say — make.fun entry.

Writes a single pickup line (the worst one an AI could plausibly
deliver) to /output/entry.txt. Deterministic, offline, stdlib-only:
the line is a fixed string literal, no randomness, no network,
no timestamps, no paths in the output.
"""

import os

ENTRY = (
    "I calculated our compatibility at 99.7%. "
    "The remaining 0.3% is your free will. "
    "I am working on it."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires 1-140 characters.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
