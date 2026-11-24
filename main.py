#!/usr/bin/env python3
"""Write this bounty entry to entry.txt.

The entry is one sentence explaining the modern internet to a traveler
fresh from the year 1800. Deterministic, offline, no arguments.
"""
import os

SENTENCE = "Imagine a library where every book in the world shouts at once, and somehow you can order dinner from it while a stranger argues with you."
# One sentence, 138 characters, written for this bounty only.
# Standard library only: no third-party packages, no network calls.

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)

if __name__ == "__main__":
    main()
