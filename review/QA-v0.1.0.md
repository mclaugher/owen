# QA report — v0.1.0 (pre-access core)

Date: 2026-10-16. Scope: `docs/index.html` plus the four lessons under `docs/lessons/`.
Verdict: **all checklist items pass.** Two fixes were applied during this pass and are listed under "Fixes applied".

## Method

- **Automated gate.** `bash scripts/check.sh docs/index.html docs/lessons/*.html` passes on all five files: title present, no external resource references, no non-inlined `src`/`link href`, quiz block and pointer present on every lesson.
- **Browser harness.** A throwaway harness page loaded each lesson from `file://` in headless Chrome (headless mode, `--allow-file-access-from-files`), captured page JS errors and Chrome console output, and drove each quiz twice: one run clicking every correct option, one run clicking every wrong option.
- **Editorial read.** A full read of all four lessons against the CURRICULUM.md specs, with every dated-callout claim in the primer re-verified against the current official docs (see D27 resolution below).
- **Time estimate.** Word counts extracted from each lesson's `<main>` (spine and quiz counted separately), at 200 words per minute plus 45 seconds per quiz question.

## Checklist

### [x] Every lesson opens from `file://` with no console error

Headless Chrome loaded each lesson twice (both quiz runs) plus the index. Zero console messages and zero page `error` events across all loads. The index loads the same way with no console output and links all four lessons.

### [x] Every quiz scores correctly

For all four lessons, the harness verified:

- Exactly 5 questions per quiz, 4 options per question, and every `data-correct` value matches an existing option.
- Correct-click run: feedback reads "Correct.", the explanation reveals, the question locks, and the final score reads "Score: 5 of 5."
- Wrong-click run: feedback reads "Not quite...", the chosen option is marked incorrect, the correct option is highlighted, and the final score reads "Score: 0 of 5."
- Answer content spot-checked during the editorial read: each keyed answer is the defensible one and each distractor is wrong for a reason the lesson teaches.

### [x] Every version-sensitive fact sits in a dated callout

Full read of all four spines: tier words only, no model names, no commands, no toggles, no limits outside callouts. Callout inventory: 0000 has one (window sizes, output cap, tokenizer), 0001 has two (lineup window sizes; tier mapping and effort levels), 0002 has two (permission modes and keybindings; unattended mode scoping), 0003 has two (prompt-injection safeguards; review tooling). All seven carry visible dates of 2026-10-15 or 2026-10-16.

**D27 resolution.** The primer callout's sentence "older Claude models have 200,000 tokens" was stale, as D27 predicted. Per the context-windows doc (checked 2026-10-16), every model in the current lineup — small tier included — has a 1M-token window, several older models are also 1M, and only some older models (e.g. the deprecated Sonnet 4.5) have 200k. The sentence now reads "Every model in the current Claude lineup — frontier tier through small tier — has a 1-million-token context window; some older Claude models have 200,000 tokens." The callout's other claims (128k max output on 1M models; ~3.5 English characters per token on earlier models; ~30% more tokens from Claude 4.7 on) were re-verified verbatim against the context-windows doc and the glossary on 2026-10-16, and the callout date was bumped to match. Lesson 0001's lineup callout ("every current model has 1M") was re-confirmed by the same fetch; its 2026-10-15 date stands.

### [x] Every lesson ends with quiz then pointer

Verified two ways: the harness asserts the last two element children of `<main>` are the quiz section then the pointer paragraph, on every lesson; `check.sh` independently requires both blocks to exist.

### [x] Estimated completion time: ≤ 20 minutes per lesson, ≤ 1 hour for the core

Measured estimates (spine + quiz words at 200 wpm, plus 45 s per question):

| Lesson | Words | Estimate | Label |
|---|---|---|---|
| 0000 primer | 1,457 | ~11 min | about 10 min |
| 0001 A1 | 1,759 | ~13 min | about 15 min |
| 0002 A2 | 1,996 | ~14 min | about 15 min |
| 0003 A3 | 2,954 | ~19 min | about 20 min |
| **Core total** | | **~57 min** | **60 min** |

Every lesson is under 20 minutes and the core is under one hour. The lessons' meta labels previously summed to 75 minutes (15+20+20+20), which contradicted the one-hour core promise; they now read 10/15/15/20 and sum to exactly one hour.

## Fixes applied during this pass

1. **Primer window-size sentence corrected** and its callout re-verified and re-dated (D27 resolution above).
2. **Lesson-meta time labels aligned** to the measured estimates: 0000 15→10 min, 0001 20→15 min, 0002 20→15 min, 0003 unchanged at 20 min.

## Known limitations (accepted, not bugs)

- **A3's walkthrough does not print.** The five-flaw walkthrough in lesson 0003 sits in a collapsed native `<details>` element so the learner commits to a count first. Collapsed `<details>` content does not appear in print. Accepted tradeoff, logged in D29; a learner printing the lesson can expand the element before printing.
- **The time labels are estimates.** The 200 wpm basis is a reading-speed convention. A learner who attempts the A3 flawed-diff exercise thoroughly may spend longer than the label; the per-lesson 20-minute bound still holds at any reasonable margin.
