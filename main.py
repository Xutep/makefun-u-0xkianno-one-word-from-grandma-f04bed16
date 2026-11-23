#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Utep's grandma would text about AI to
/output/entry.txt: one word and nothing else.
"""

import os

WORD = "robit"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
