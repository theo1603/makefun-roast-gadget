"""One-Line Roast entry: the gadget you use every day.

Writes one original roast line about a daily gadget to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.
"""

import os

LINE = (
    "My smartwatch cheers me for standing up, "
    "then dies before lunch \u2014 a personal trainer "
    "with the stamina of a couch."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
