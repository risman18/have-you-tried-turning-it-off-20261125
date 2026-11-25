#!/usr/bin/env python3
"""Write one funny tech-support line to /output/entry.txt.

Original line, written for the make.fun bounty
"Have You Tried Turning It Off?".
"""

LINE = (
    "Great news, I found your problem \u2014 it's the Wi-Fi. "
    "Bad news, I just lost it again. "
    "Have you tried turning the router off, then on, "
    "then quietly thanking it?"
)


def main() -> None:
    # Gate: entry must be 1-199 chars of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 199, f"entry is {len(LINE)} chars"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
