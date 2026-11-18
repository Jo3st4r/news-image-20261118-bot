#!/usr/bin/env python3
"""news-image-20261118 entry: "The World in One Image" for 18 November 2026.

Writes the vendored front-page poster (assets/entry.png, 1024x1024 PNG)
byte-for-byte to /output/entry.png.

Deterministic by construction: pure byte copy of a file shipped in this
repository. No network, no clock, no randomness, no environment input.
Two runs therefore produce identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
