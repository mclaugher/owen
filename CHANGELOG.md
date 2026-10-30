# Changelog

All notable changes to the course live here.

## v0.2.0 — 2026-10-30

Second release: the applied phase of Track A. Four more self-contained HTML pages under `docs/`, each with its practice folder packed inside the page behind an offline download button. Track A is complete: eight lessons.

### Added

- Lesson A4: `0004-first-win-and-your-setup` — the first real session on a planted bug, then the instructions file and three permission setups.
- Lesson A5: `0005-guardrails-and-add-ons` — a worked guardrail that fires and clears, then judging add-ons one at a time.
- Lesson A6: `0006-small-sessions` — one task per session, the plan in a file, commits as save points; one task across two sessions.
- Lesson A7: `0007-when-things-go-wrong` — warning signs, the restart rule, the two cost views; the course finale uses every habit.
- Practice-folder tooling: `scripts/pack.py` embeds a folder in a lesson page with `.seed` name restoring; `scripts/check.sh` requires the download block on lessons 0004+.
- Plain-language gate: `scripts/banned-words.txt` (D34) and a visible-text scan in `scripts/check.sh`.
- QA report for this release at `review/QA-applied-phase.md`.

### Changed

- `docs/index.html` lists all eight lessons in two sections, adds the suggested-experience box (D35), and points at Track B as what comes next.
- Lesson 0001 opens with the suggested-experience echo line (D35).
- Lesson 0003 reworded one sentence to clear the banned-word scan (D37).
- The teach-curriculum fork's build steps cover post-access lessons (D38).

## v0.1.0 — 2026-10-16

First release: the pre-access core. Four self-contained HTML pages under `docs/`, ready for GitHub Pages, requiring zero tool access.

### Added

- Shared primer: `0000-where-tokens-actually-go` — the context-window mental model.
- Lesson A1: `0001-the-mental-model` — small tasks, the two dials, four first wins.
- Lesson A2: `0002-scoping-and-modes` — plan-before-code, the mode ladder, the verification rule.
- Lesson A3: `0003-reviewing-agent-output` — review habits, tests as guardrails, the security section with a flawed-diff exercise.
- Site index at `docs/index.html` linking the four lessons and naming what the full curriculum adds.
- Build tooling: lesson template, quiz widget, inliner (`scripts/inline.py`), and self-containment checks (`scripts/check.sh`).
- Generation tooling: the teach skill vendored at v1.3.1, the `teach-curriculum` fork, the Track A persona, and per-lesson learning records.
- QA report for this release at `review/QA-v0.1.0.md`.
