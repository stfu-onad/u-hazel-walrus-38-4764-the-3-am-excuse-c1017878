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

OUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# The excuse, built in three beats so each image lands on its own:
# the sleeping keys, the dark screen, the refusal itself. The wallet
# is not broken or out of power — it is awake enough to judge, and
# it chooses not to be an accomplice to its owner's 3 AM self.
LINE_PARTS = (
    "At 3 AM my keys are asleep, my screen is dark, and every ",
    "signature looks like a regret in advance \u2014 I refuse to be ",
    "your accomplice.",
)


def compose_line() -> str:
    """Join the beats into the single entry line."""
    return "".join(LINE_PARTS).strip()


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"line is {len(text)} chars, gate allows 1-{MAX_CHARS}"
    )
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def write_entry(text: str, out_path: str = OUT_PATH) -> None:
    """Write the validated line plus a trailing newline."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


def main() -> None:
    text = compose_line()
    validate(text)
    write_entry(text)

    print(f"wrote {len(text)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
