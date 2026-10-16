# Daily report — 2026-10-16

## Merged since yesterday

All six PRs merged on 2026-10-15. Tasks 1–6 of PLAN.md are done.

| PR | Task | Title |
|----|------|-------|
| #1 | 1 | chore: vendor teach skill v1.3.1 |
| #2 | 2 | feat: lesson template, quiz widget, inliner |
| #3 | 3 | feat: fork teach into teach-curriculum |
| #4 | 4 | feat: generate shared primer lesson 0000 |
| #5 | 5 | feat: generate A1 mental-model lesson 0001 |
| #6 | 6 | feat: generate A2 scoping-and-modes lesson 0002 |

## Open PRs awaiting human merge

None, besides this housekeeping PR.

## Blocked tasks

None. Tasks 7 (A3 — reviewing agent output, security) and 8 (site index, QA pass, changelog) remain. Both are unblocked; task 7 is next.

## Guideline additions from the review loop

One, from the PR #4 review (commit eb180c6): "A dated-callout claim that the cited page contradicts for any current model is a rejection. Check each tier-level claim against the sizes-by-model table." The same review also produced a content fix (a6fefe6) that corrected the primer's 200k-window claim before merge.

## Look at first

1. **D27 QA flag.** The models-overview page now shows a 1M window for every current model. The primer callout's sentence "older Claude models have 200,000 tokens" may read as too broad. Task 8 QA must re-verify it. The flag is logged in DECISIONS.md (D27) and in the task 5 PROGRESS entry.
2. **Mode-system drift risk.** D28 notes the current Claude Code mode set (`auto` as the interactive default, `dontAsk`) no longer maps one-to-one onto the lesson's four-rung ladder. The A2 callouts handle it today; task 8 QA should re-check the docs pages before tagging v0.1.0.
3. **No release tag yet.** The plan targets a tagged v0.1.0 after task 8. Two tasks stand between here and the tag.
