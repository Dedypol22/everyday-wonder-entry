"""Everyday Wonder entry: a door drawn in bus-window fog.

On a rainy bus ride, the window fogs with the rider's own breath, and a
fingertip draws a door in the condensation - an escape hatch sketched in
mid-air. The joke of the sentence is that the door opens onto nothing but
more rain: the very weather the rider was trying to leave. The wonder is
small and exact - breath, fingertip, fog - and the strangeness comes from
the door leading nowhere new, only deeper into the ordinary.
"""

import os
import sys

LINE = (
    "The bus window fogs with my breath, and my fingertip draws a door "
    "in it that opens onto nothing but more rain."
)


def output_dir():
    """Return the directory entry.txt should be written to."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    """Write the entry sentence to entry.txt and return 0."""
    line = LINE
    assert isinstance(line, str) and line, "entry must be a non-empty string"
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert line == line.strip(), "entry must have no leading/trailing whitespace"
    line.encode("utf-8")

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
