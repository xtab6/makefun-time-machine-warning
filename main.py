#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun entry.

Writes one warning label for a time machine (120 characters or fewer)
to /output/entry.txt. The label is fixed text: deterministic, no input,
no network, no randomness. The joke turns the duplicate-self hazard of
time travel into a straight-faced safety notice, with the twist saved
for the last few words. The sealed gate wants 1 to 120 characters of
UTF-8 text; this label is 74 characters including its trailing newline.
"""

import os

LABEL = "WARNING: Only one of you may claim the refund. The other one already did."


def main():
    text = LABEL.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit("label is %d chars, must be 1-120" % len(text))
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Write entry.txt only; never remove /output itself.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
