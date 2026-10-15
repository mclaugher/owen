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
