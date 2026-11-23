#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Utep's grandma would text about AI to
/output/entry.txt: one word and nothing else.
"""

import os

WORD = "robit"

# The bounty takes one word and nothing else: guard the rule in code so a
# future edit cannot silently break it (a space, a newline, or a second word
# would be judged as a different entry).
assert WORD and WORD == WORD.strip(), "word must not start or end with whitespace"
assert not any(ch.isspace() for ch in WORD), "entry must be a single word"
assert WORD.isalpha(), "entry must be a single alphabetic word"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)
    # Read it back: the file must hold exactly the word, nothing else.
    with open("/output/entry.txt", encoding="utf-8") as handle:
        assert handle.read() == WORD, "entry.txt must contain only the word"


if __name__ == "__main__":
    main()
