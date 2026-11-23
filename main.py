#!/usr/bin/env python3
"""Sleeve notes for the Frog Trio.

Writes one album title and a short back-cover blurb for a jazz trio
made entirely of frogs to /output/entry.txt (or to the path given as
argv[1] for local testing). Stdlib only; no network, no clock.
"""

import os
import sys

ENTRY = """Night Water

The trio holds the late set at the boathouse on Miller's Pond, and by the second tune the room is theirs. Milo's tenor comes in low, unhurried, a dry tone that sits just behind the beat; Ada walks the bass through the reeds, and Pip keeps time on brushes so soft you hear the water against pilings between songs. One night, no overdubs, the three of them in a circle."""


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    text = ENTRY.strip() + "\n"
    if not (1 <= len(text.rstrip("\n")) <= 400):
        raise SystemExit("entry length out of gate range")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
