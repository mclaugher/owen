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
  [ "$ok" -eq 1 ] && echo "PASS $f"
  [ "$ok" -eq 0 ] && fail=1
done
exit "$fail"
