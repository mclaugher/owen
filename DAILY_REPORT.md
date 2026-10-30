# Daily report — 2026-10-30

## Merged since the last report (2026-10-29)

| PR | Merged | Title | Plan task |
|----|--------|-------|-----------|
| #12 | 2026-10-29 | feat: practice-folder packer and download-block check | task 1 |
| #13 | 2026-10-29 | feat: banned-word list and plain-language check | task 2 |
| #14 | 2026-10-29 | docs: teach-curriculum fork covers post-access lessons | task 3 |

Waves 1 and 2 of the applied-phase plan are complete. Every merge maps to a plan task; no scope creep and no reverts. Task 3's branch (PR #14) resolved a DECISIONS.md numbering collision when it merged main after #13 landed (task 3's entry became D38) — bookkeeping only.

## Open PRs awaiting human merge

None besides this housekeeping PR.

## Blocked tasks

None. Task 4 (generate lesson 0004 — first win, then make it yours) is next: its dependencies (tasks 2 and 3) both merged, so the dev loop can start the first lesson of the applied phase.

## Guideline additions from the review loop

This PR's own review rounds added two lines to REVIEW_GUIDELINES.md:

1. A report or ledger claim that git history contradicts (wrong PR, commit, or date) is a rejection; verify attributions against `git log` (f9af3fb).
2. A report claim that the PR's own final diff contradicts is a rejection; a fix or guideline commit on a report PR must update the report it invalidates (4ad38a5).

## Look at first

1. **v0.1.0 release steps are still open (second reminder).** No GitHub Pages site (API returns 404) and no tags. The human steps remain: enable Pages from `docs/` on main, then tag v0.1.0.
2. **Lesson generation starts next.** Task 4 is the first task that produces learner-facing text under the new banned-word check and the updated teach-curriculum skill. Worth a closer human read of that PR than the tooling PRs got.
