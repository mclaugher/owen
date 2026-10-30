"""tally.py — a small expense tracker. See README.md for commands."""
import csv
import sys
from pathlib import Path

DATA_FILE = Path("tally.csv")


def add(amount, category, note=""):
    with DATA_FILE.open("a", newline="") as f:
        csv.writer(f).writerow([f"{amount:.2f}", category, note])
    return f"added {amount:.2f} to {category}"


def entries():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open(newline="") as f:
        return [(float(amount), category, note) for amount, category, note in csv.reader(f)]


def format_list():
    rows = entries()
    if not rows:
        return "no entries"
    lines = []
    for amount, category, note in rows:
        line = f"{amount:>8.2f}  {category}"
        if note:
            line += f"  ({note})"
        lines.append(line)
    return "\n".join(lines)


def main(argv):
    if len(argv) >= 3 and argv[0] == "add":
        return add(float(argv[1]), argv[2], " ".join(argv[3:]))
    if argv and argv[0] == "list":
        return format_list()
    return "usage: python3 tally.py add AMOUNT CATEGORY [NOTE...] | list"


if __name__ == "__main__":
    print(main(sys.argv[1:]))
