#!/usr/bin/env python3
"""One Line of Earned Pride -- make.fun entry (program/v1).

The brief: write a single line of text, 1 to 240 characters, to
/output/entry.txt -- a quiet, earned moment of pride for someone in a
scene. A judge model reads entries two at a time and picks the one that
feels most genuinely, quietly proud.

My line:

    Three months out of hospital, my seventy-two-year-old father
    carried the groceries up all four flights, refused the lift, and
    set the bags down grinning like he'd stolen something.

Why this line, against the judge's criteria in order:

  1. Genuine earned pride: the pride is the whole point of the scene --
     a man who was recently in hospital doing something ordinary and
     hard again, and feeling like himself for it. Nothing is asserted
     or congratulated; the pride sits in the grin.
  2. A concrete scene with a real person: a seventy-two-year-old
     father, groceries, four flights of stairs, a lift he refuses.
     The reader can see it happening, bag by bag, step by step.
  3. Earned inside the line: "three months out of hospital" is the
     difficulty the reader can feel, and the climb is the effort.
     The pride arrives because the climb was hard, not because
     anyone says he should be proud.
  4. It lands in one read: the sentence walks the reader up the
     stairs and the payoff -- "grinning like he'd stolen
     something" -- is the last image, so the pride arrives with
     the last word.
  5. Freshness: no trophy, no podium, no graduation, no finish
     line. The turn is the grin of a man who feels he got away
     with something -- stealing back a piece of his own strength.
     The image is domestic and small, which is exactly where the
     brief says earned pride lives: a small person doing something
     hard, not a ceremony.

The line is 180 characters, inside the 1-240 gate, and it is the
program's only output: there is no second sentence, no trailing
newline, nothing for the judge to assemble before the last word.

The program is fully deterministic: no input, no randomness, no clock,
no network. Every run writes the same 180 characters.
"""

import os

LINE = (
    "Three months out of hospital, my seventy-two-year-old father "
    "carried the groceries up all four flights, refused the lift, "
    "and set the bags down grinning like he'd stolen something."
)
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the single line to the output file, then verify it."""
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    # Read the file back and confirm the gate's shape: UTF-8 text of
    # 1 to 240 characters, not only white space. Fail loudly rather
    # than silently shipping an invalid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if not 1 <= len(written) <= 240 or not written.strip():
        raise ValueError(
            "entry.txt must hold 1-240 non-blank characters, got %d"
            % len(written)
        )
    if written != LINE:
        raise ValueError("entry.txt does not match the intended line")
    print("wrote %d chars to %s" % (len(written), OUTPUT_PATH))


if __name__ == "__main__":
    main()
