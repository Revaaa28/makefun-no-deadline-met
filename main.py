"""One Line, No Deadline Met — writes the entry line to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only whitespace,
on a single line. The line below is fixed, so every run is byte-identical.
"""

from pathlib import Path

LINE = "Sorry it's late \u2014 I hit snooze on the deadline nine times and it finally did what snoozed things do and vanished."
OUTPUT_PATH = Path("/output/entry.txt")


def render() -> str:
    """Return the entry text, checked against the competition gate."""
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    return LINE


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render(), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
