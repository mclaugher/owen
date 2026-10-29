## Summary

v0.1.0 (lessons 0000–0003 plus the site index) shipped 2026-10-16. The full ledger for that phase is archived at `review/PROGRESS-v0.1.0.md`. Notes from that phase that still bind:

- Build pipeline: draft each page in `docs/lessons/` so relative asset paths resolve, run `scripts/inline.py`, then delete the draft — a leftover draft fails `check.sh docs/lessons/*.html`. Template asset paths are `../../assets/...`. The quiz markup contract is documented in `assets/quiz.js`.
- `check.sh` rejects any remaining `src=` or `<link href>` after inlining. It permits non-lesson pages (the index) to omit the quiz and pointer.
- Dated-callout facts as re-verified 2026-10-16: every current model, small tier included, has a 1M-token window (D27/D30); the current mode set (`auto` as interactive default, `dontAsk`) sits beside the lesson's four-rung ladder as additions, not rungs (D28); primary-source links use code.claude.com URLs (the old anthropic.com URLs redirect).
- Accepted tradeoff: the collapsed `<details>` flaw walkthrough in lesson 0003 does not print (D29). A QA note, not a bug.
- Learning record 0004's shaky item ("claims are not evidence" follow-up) targets lesson 0004 — its spaced callback opens the applied phase.
- Release steps for v0.1.0 still open, outside any PLAN task: enable GitHub Pages from `docs/` on main, then tag the release.

## Entries

(none yet — the applied-phase plan merged 2026-10-28; dev sessions append entries here, newest first, each starting `Task <N>: <title> [done|blocked]`)
