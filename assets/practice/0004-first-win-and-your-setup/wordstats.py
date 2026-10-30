"""wordstats: print the five most common words in a text file."""

import re
import sys


def load_words(path):
    with open(path, encoding="utf-8") as handle:
        text = handle.read().lower()
    return re.findall(r"[a-z']+", text)


def count_words(words):
    counts = {}
    for word in words:
        counts[word] += 1
    return counts


def top_five(counts):
    ordered = sorted(counts, key=counts.get, reverse=True)
    return ordered[:5]


def main():
    if len(sys.argv) != 2:
        print("usage: python3 wordstats.py <textfile>")
        return 2
    counts = count_words(load_words(sys.argv[1]))
    for word in top_five(counts):
        print(f"{counts[word]:>4}  {word}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
