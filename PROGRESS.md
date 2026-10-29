## Summary

v0.1.0 (lessons 0000–0003 plus the site index) shipped 2026-10-16. The full ledger for that phase is archived at `review/PROGRESS-v0.1.0.md`. Notes from that phase that still bind:

- Build pipeline: draft each page in `docs/lessons/` so relative asset paths resolve, run `scripts/inline.py`, then delete the draft — a leftover draft fails `check.sh docs/lessons/*.html`. Template asset paths are `../../assets/...`. The quiz markup contract is documented in `assets/quiz.js`.
- `check.sh` rejects any remaining `src=` or `<link href>` after inlining. It permits non-lesson pages (the index) to omit the quiz and pointer.
- Dated-callout facts as re-verified 2026-10-16: every current model, small tier included, has a 1M-token window (D27/D30); the current mode set (`auto` as interactive default, `dontAsk`) sits beside the lesson's four-rung ladder as additions, not rungs (D28); primary-source links use code.claude.com URLs (the old anthropic.com URLs redirect).
- Accepted tradeoff: the collapsed `<details>` flaw walkthrough in lesson 0003 does not print (D29). A QA note, not a bug.
- Learning record 0004's shaky item ("claims are not evidence" follow-up) targets lesson 0004 — its spaced callback opens the applied phase.
- Release steps for v0.1.0 still open, outside any PLAN task: enable GitHub Pages from `docs/` on main, then tag the release.

## Entries

(newest first, each starting `Task <N>: <title> [done|blocked]`)

Task 3: Update teach-curriculum for post-access lessons [done]
The fork's build steps gain step 3: pack the practice folder into the draft for a post-access lesson (old steps 3–6 renumbered 4–7), and a new "Post-access rule" section after "Pre-access rule" states the full recipe — author under `assets/practice/<lesson>/`, `.seed` suffixes, the PACK:PRACTICE marker and lesson-number meta tag in the draft, the pack command, name every practice file in the exercise text, solve end to end before done, copy-paste fallback for one or two tiny files. Key decision, verified by test: pack.py reads the whole page before writing, so the draft packs in place (`pack.py <folder> <draft> <draft>`) and the inline/delete/check steps run unchanged — pack before inline.py. DECISIONS.md D38 records the diff under a new 2026-10-29 heading. Nothing else in the fork changed; lesson generation for 0004 (task 4) should now follow the skill as written.
Files touched: `.claude/skills/teach-curriculum/SKILL.md`, `DECISIONS.md`, `PROGRESS.md`.
Task 2: Banned-word list and plain-language check [done]
`scripts/banned-words.txt` seeds the D34 words (orchestration, provenance, capstone, persona, their inflections) plus peers judged insider-only (affordance, ideation, operationalize, paradigm, synergy, learnings, performant). `check.sh` now scans each page's visible text against the list — scripts, styles, comments, and attributes are skipped, so quiz JS never trips it. List syntax: one lowercase word per line, `#` comments, and `!next` exceptions; `frontier !model !models !tier !tiers` bans bare "frontier" but allows "frontier model" and "frontier-tier" (hyphens split into tokens). Gotchas for the next session: matching is exact-token, so new inflections must be listed explicitly, and `scripts/fixtures/banned-word-lesson.html` fails `check.sh` by design. Shipped lesson 0003 used "provenance" in visible text; one sentence reworded, logged as D37.
Files touched: `scripts/banned-words.txt`, `scripts/check.sh`, `scripts/fixtures/banned-word-lesson.html`, `docs/lessons/0003-reviewing-agent-output.html`, `DECISIONS.md`, `PROGRESS.md`.

Task 1: Practice-folder packer [done]
`scripts/pack.py` (stdlib only) zips a practice folder, strips a trailing `.seed` from each file name, and replaces the marker comment `<!-- PACK:PRACTICE -->` in the lesson page with a download block (`id="practice-download"`) whose button rebuilds the zip from embedded base64 — offline-safe from `file://`. Authors of lessons 0004+ must put that marker in the draft page and a `<meta name="lesson-number" content="NNNN">` tag in the head: `check.sh` requires the download block on any page whose file name starts `NNNN-` with NNNN ≥ 0004, or whose head carries that meta tag (the meta covers packed output with arbitrary file names). The zip uses a fixed timestamp, so repacking an unchanged folder changes nothing. Gotcha for the next session: run pack.py on the draft (it needs the marker), and note `scripts/fixtures/post-access-lesson.html` fails `check.sh` by design — like `sample-lesson.html`, never add fixtures to a default check run.
Files touched: `scripts/pack.py`, `scripts/check.sh`, `scripts/fixtures/post-access-lesson.html`, `scripts/fixtures/practice-sample/` (README.md, CLAUDE.md.seed, src/greet.py), `PROGRESS.md`.
