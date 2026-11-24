#!/usr/bin/env python3
"""Absurd invention pitch, v2: the whale-song headphones.

Writes one sentence to /output/entry.txt: headphones that translate your
neighbour's drill into whale song, turning DIY Sunday into a nature
documentary. The laugh comes from the invention itself (a live translator
for power tools), the fix is silly yet weirdly plausible (reframing the
noise instead of blocking it), and the sentence names the annoyance, the
invention and its mechanism in one clean line.
"""

import os

PITCH = "Headphones that translate your neighbour's drill into whale song, turning DIY Sunday into a nature documentary."


def main():
    assert 1 <= len(PITCH) <= 220, "entry must be 1-220 characters"
    assert PITCH.count(".") == 1 and PITCH.endswith("."), "entry must be exactly one sentence"
    data = PITCH.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
