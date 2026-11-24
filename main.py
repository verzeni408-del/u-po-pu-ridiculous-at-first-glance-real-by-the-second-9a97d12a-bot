"""Wi-Fi SSID rental pitch: the bakery downstairs pays rent on 32 chars."""

from pathlib import Path

ENTRY_TEXT = (
    "We rent your Wi-Fi name to the bakery downstairs, so every neighbor "
    "hunting for signal sees their menu and you collect rent on 32 characters."
)

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
