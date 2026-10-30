# Review guidelines

The review loop reads this file before every review and appends lessons here.

- New behavior needs tests. A weakened or deleted test is a rejection.
- Scope beyond the stated task is a rejection.
- Course text not in ste-style is a rejection. Check `.claude/skills/ste-style/SKILL.md`.
- A lesson with an external resource reference is a rejection. `bash scripts/check.sh <file>` must pass.
- A pre-access lesson that requires tool access is a rejection.
- A model name, command, toggle, or limit in the lesson spine is a rejection. These belong in dated callouts. The spine uses tier words.
- An undated callout, or a tool-behavior claim with no verification date, is a rejection.
- A lesson without the 5-question quiz and the closing pointer is a rejection.
- Org-specific content anywhere in the repo is a rejection.
- Example material that is not publicly available is a rejection.
- A deviation from CURRICULUM.md or the vendored skill with no DECISIONS.md entry is a rejection.
- A dated-callout claim that the cited page contradicts for any current model is a rejection. Check each tier-level claim against the sizes-by-model table.
- A post-access lesson page (0004 and later) without the packed practice-folder download block is a rejection (D32).
- A file a tool reads by name (CLAUDE.md, settings files) sitting live under `assets/practice/` is a rejection. Sources carry the `.seed` suffix.
- A lesson whose text contains a word from `scripts/banned-words.txt` is a rejection. An industry term used before the lesson defines it is a rejection (D34).
- An exercise that does not name its practice files is a rejection.
- A published expected token range, or any learner-versus-anyone comparison, in a Track A lesson is a rejection (D33).
- A PR for a lesson task whose body does not record the solved exercise is a rejection.
- A report or ledger claim that git history contradicts (wrong PR, commit, or date) is a rejection. Verify attributions against `git log`.
- A report claim that the PR's own final diff contradicts is a rejection. A fix or guideline commit on a report PR must update the report it invalidates.
- A tool-behavior claim is verified against the docs page that governs that behavior, not only the page the callout cites. Default permission mode comes from permission-modes, not the quickstart.
