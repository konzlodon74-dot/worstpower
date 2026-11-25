#!/usr/bin/env python3
"""Worst superpower one-liner entry.

Writes a single useless-superpower joke to /output/entry.txt
with no trailing newline, after checking the 1-140 character gate.
"""
import os

LINE = "My superpower is reading my own mind - but only the thoughts I had five seconds ago."

def main():
    assert 1 <= len(LINE) <= 140, "line length out of gate"
    assert "\n" not in LINE and "\r" not in LINE, "line must be single line"
    assert LINE.strip(), "line must be non-blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))

if __name__ == "__main__":
    main()
