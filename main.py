"""Write one joke about working beside an AI coding agent."""

from pathlib import Path

JOKE = "My AI coding agent fixed the bug live on stage by deleting the feature, the tests, and my will to present."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
