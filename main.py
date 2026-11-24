"""The One-Line Exit entry.

Writes ENTRY to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), no trailing
newline.

Verified: entry is 125 chars / 125 bytes, one line; entry.txt sha256
5adda496278c6acf2c96c49d0a6e236c69de9504940de2dcf61231888ed4b25b,
byte-identical across 3 fresh runs + 1 clean-env run.
"""

import os

ENTRY = "Please accept my resignation as the office fire warden: I set the building on fire twice, and the second time was on purpose."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
