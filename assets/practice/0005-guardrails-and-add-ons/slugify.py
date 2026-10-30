"""Turn a post title into a URL slug."""

import sys


def slugify(title):
    """Return the slug form of a title: lowercase, hyphen-separated."""
    out = []
    for ch in title.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -_":
            out.append("-")
    return "".join(out)


if __name__ == "__main__":
    print(slugify(" ".join(sys.argv[1:])))
