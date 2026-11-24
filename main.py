#!/usr/bin/env python3
"""make.fun entry: u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes the pickup line held in entry.txt, byte-for-byte, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ENTRY = os.path.join(HERE, "entry.txt")


def check_gate(data: bytes) -> None:
    """Mirror the sealed gate: UTF-8 text of 1 to 200 characters,
    not only white space."""
    text = data.decode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1 to 200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> int:
    with open(ENTRY, "rb") as fh:
        check_gate(fh.read())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    shutil.copyfile(ENTRY, dest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
