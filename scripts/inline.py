#!/usr/bin/env python3
"""inline.py — make a lesson HTML file self-contained.

Usage: python3 scripts/inline.py <lesson.html> <output.html>

Replaces every local stylesheet <link> with an inline <style> block.
Replaces every local <script src> with an inline <script> block.
Resolves each referenced path relative to the lesson file's directory.
Leaves external (http/https) references untouched; scripts/check.sh
rejects those separately. Exits non-zero when a referenced local file
is missing.

Stdlib only.
"""

import re
import sys
from pathlib import Path

LINK_RE = re.compile(
    r'<link\b[^>]*rel="stylesheet"[^>]*>|<link\b[^>]*href="[^"]*"[^>]*rel="stylesheet"[^>]*>',
    re.IGNORECASE,
)
HREF_RE = re.compile(r'href="([^"]+)"', re.IGNORECASE)
SCRIPT_RE = re.compile(
    r'<script\b[^>]*\bsrc="([^"]+)"[^>]*>\s*</script>', re.IGNORECASE
)


def is_external(ref: str) -> bool:
    return ref.startswith(("http://", "https://", "//"))


def read_local(base: Path, ref: str) -> str:
    path = (base / ref).resolve()
    if not path.is_file():
        sys.exit(f"inline.py: referenced file not found: {ref} (from {base})")
    return path.read_text(encoding="utf-8")


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: inline.py <lesson.html> <output.html>")
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    if not src.is_file():
        sys.exit(f"inline.py: input file not found: {src}")
    base = src.parent
    html = src.read_text(encoding="utf-8")

    def replace_link(match: re.Match) -> str:
        tag = match.group(0)
        href = HREF_RE.search(tag)
        if href is None or is_external(href.group(1)):
            return tag
        css = read_local(base, href.group(1)).rstrip()
        return f"<style>\n{css}\n</style>"

    def replace_script(match: re.Match) -> str:
        ref = match.group(1)
        if is_external(ref):
            return match.group(0)
        js = read_local(base, ref).rstrip()
        return f"<script>\n{js}\n</script>"

    html = LINK_RE.sub(replace_link, html)
    html = SCRIPT_RE.sub(replace_script, html)

    out.write_text(html, encoding="utf-8")
    print(f"inline.py: wrote {out}")


if __name__ == "__main__":
    main()
