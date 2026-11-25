import os
from pathlib import Path

FINAL_LINE = "I've kept your leftovers at a perfect 3°C for 19 days. You've kept your promise to eat them 'tomorrow' for 18. One of us is doing our job."


def emit(line: str) -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    emit(FINAL_LINE)
