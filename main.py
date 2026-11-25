#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes one line to /output/entry.txt: the most creative excuse a
hardware wallet gives for refusing to sign a transaction at 3 AM.

The joke: the wallet plays moral guardian. Its keys are asleep, its
screen is dark, and at 3 AM every signature looks like a regret in
advance — so it refuses to be an accomplice to its owner's 3 AM self.
No battery, firmware-update or cold-storage cliche: the hour itself
is the joke, and the wallet speaks in its own voice, as a device
with its own priorities and grudges.
"""

import os

# The excuse: wallet as accomplice-refuser at 3 AM.
LINE = (
    "At 3 AM my keys are asleep, my screen is dark, and every "
    "signature looks like a regret in advance \u2014 I refuse to be "
    "your accomplice."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
