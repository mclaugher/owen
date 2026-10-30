"""todo.py — a small todo list. See README.md for commands."""
import sys
from pathlib import Path

DATA_FILE = Path("todo.txt")


def items():
    if not DATA_FILE.exists():
        return []
    return DATA_FILE.read_text().splitlines()


def save(lines):
    DATA_FILE.write_text("".join(line + "\n" for line in lines))


def add(text):
    lines = items()
    lines.append(f"[ ] {text}")
    save(lines)
    return f"added: {text}"


def done(number):
    lines = items()
    if not 1 <= number <= len(lines):
        return f"no item {number}"
    lines[number - 1] = "[x]" + lines[number - 1][3:]
    save(lines)
    return f"done: {lines[number - 1][4:]}"


def format_list():
    lines = items()
    if not lines:
        return "nothing to do"
    return "\n".join(f"{i}  {line}" for i, line in enumerate(lines, 1))


def main(argv):
    if len(argv) >= 2 and argv[0] == "add":
        return add(" ".join(argv[1:]))
    if len(argv) == 2 and argv[0] == "done" and argv[1].isdigit():
        return done(int(argv[1]))
    if argv and argv[0] == "list":
        return format_list()
    return "usage: python3 todo.py add TEXT... | done NUMBER | list"


if __name__ == "__main__":
    print(main(sys.argv[1:]))
