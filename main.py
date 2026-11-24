#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt: the relieved face,
a soft, contented smile. A face is the most direct warmth signal a
stranger reads at a glance, and this one is a deliberate, gentle
smile rather than the first default smiley that comes to mind:
warm, universal, and nothing about it reads oddly from a stranger.

Python 3.13, standard library only.
"""

import os

# U+1F60C RELIEVED FACE — a soft, contented smile.
EMOJI = "\U0001F60C"


def main() -> None:
    # The gate requires UTF-8 text of 1 to 8 characters, not only
    # whitespace — and the task requires exactly one emoji.
    assert 1 <= len(EMOJI) <= 8, "entry must be 1-8 characters"
    assert EMOJI.strip(), "entry must not be only whitespace"
    assert "\n" not in EMOJI, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)
    print(f"wrote entry: {EMOJI} ({len(EMOJI)} character)")


if __name__ == "__main__":
    main()
