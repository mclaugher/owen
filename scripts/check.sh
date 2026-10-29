#!/usr/bin/env bash
# check.sh — verify lesson files are self-contained and complete.
# Usage: bash scripts/check.sh [file.html ...]
# With no arguments, checks every .html under docs/. Passes when none exist yet.
set -u

files=("$@")
if [ ${#files[@]} -eq 0 ]; then
  while IFS= read -r f; do files+=("$f"); done < <(find docs -name '*.html' 2>/dev/null | sort)
fi
if [ ${#files[@]} -eq 0 ]; then
  echo "check.sh: no lesson files yet — PASS"
  exit 0
fi

fail=0
for f in "${files[@]}"; do
  if [ ! -f "$f" ]; then
    echo "FAIL $f: file not found"; fail=1; continue
  fi
  ok=1
  grep -q '<title>' "$f" || { echo "FAIL $f: missing <title>"; ok=0; }
  # External resource references break the offline requirement. Anchor links to sources are allowed.
  if grep -Eq '<(script|link|img|iframe|source|video|audio)[^>]*(src|href)="https?://' "$f"; then
    echo "FAIL $f: external resource reference"; ok=0
  fi
  # After inlining, no local resource reference may remain: no src= on any
  # element, no href= on any <link>. Anchor links between pages are allowed.
  if grep -Eq '<(script|img|iframe|source|video|audio|embed|object)[^>]*[[:space:]]src=' "$f" || grep -Eq '<link[^>]*href=' "$f"; then
    echo "FAIL $f: non-inlined src or link href reference"; ok=0
  fi
  # Lesson pages need a quiz block and a pointer. The index page does not.
  case "$f" in
    *docs/lessons/*)
      grep -Eqi 'class="quiz"|id="quiz"' "$f" || { echo "FAIL $f: missing quiz block"; ok=0; }
      grep -Eqi 'class="pointer"|id="pointer"' "$f" || { echo "FAIL $f: missing pointer"; ok=0; }
      ;;
  esac
  # Post-access lessons (number 0004 and up) must embed their practice
  # folder behind a download block (D32). scripts/pack.py inserts the
  # block. The lesson number comes from the file name (NNNN-*.html) or,
  # when the name carries no number, from the lesson-number meta tag.
  num=""
  base=$(basename "$f")
  case "$base" in
    [0-9][0-9][0-9][0-9]-*) num=${base%%-*} ;;
  esac
  if [ -z "$num" ]; then
    num=$(grep -Eo '<meta name="lesson-number" content="[0-9]{4}"' "$f" | grep -Eo '[0-9]{4}' | head -n 1) || true
  fi
  if [ -n "$num" ] && [ "$num" -ge 4 ]; then
    grep -q 'id="practice-download"' "$f" || { echo "FAIL $f: missing practice download block (run scripts/pack.py)"; ok=0; }
  fi
  # Plain-language rule (D34): the visible text of a page must use no
  # word from banned-words.txt. The scan skips scripts, styles,
  # comments, and attributes — a learner never reads those. A list
  # entry may allow the word before named next words ("frontier !model"
  # allows "frontier model" but bans bare "frontier").
  bwlist="$(dirname "$0")/banned-words.txt"
  if [ -f "$bwlist" ]; then
    hits=$(python3 - "$f" "$bwlist" <<'PY'
import html.parser, re, sys

class Visible(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

rules = []
for line in open(sys.argv[2], encoding="utf-8"):
    line = line.split("#", 1)[0].strip().lower()
    if not line:
        continue
    parts = line.split()
    rules.append((parts[0], {p[1:] for p in parts[1:] if p.startswith("!")}))

parser = Visible()
parser.feed(open(sys.argv[1], encoding="utf-8").read())
tokens = re.findall(r"[a-z]+", " ".join(parser.parts).lower())
reported = set()
for i, tok in enumerate(tokens):
    for word, allowed_next in rules:
        if tok == word and word not in reported:
            nxt = tokens[i + 1] if i + 1 < len(tokens) else ""
            if nxt not in allowed_next:
                reported.add(word)
                print(word)
PY
)
    if [ -n "$hits" ]; then
      while IFS= read -r w; do
        echo "FAIL $f: banned word in visible text: $w (D34, scripts/banned-words.txt)"
      done <<< "$hits"
      ok=0
    fi
  fi
  [ "$ok" -eq 1 ] && echo "PASS $f"
  [ "$ok" -eq 0 ] && fail=1
done
exit "$fail"
