"""Entry for make.fun competition: u-suga-the-robot-apology-dd96bb59.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE_A = "I am sorry: I fed the cat at 6:00 exactly as scheduled, "
LINE_ONE_B = "and again at 6:04, because she asked with her face and "
LINE_ONE_C = "I had no rule for faces."

LINE_TWO_A = "I have learned that a request repeated is not a new request, "
LINE_TWO_B = "so from now on I will check my own log before I check her bowl."

ENTRY = LINE_ONE_A + LINE_ONE_B + LINE_ONE_C + "\n" + LINE_TWO_A + LINE_TWO_B


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
