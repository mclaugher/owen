# QA report — applied phase (lessons 0004–0007 plus the index)

Date: 2026-10-30. Scope: `docs/index.html` plus the eight lessons under `docs/lessons/`. The four applied-phase lessons got the full pass; the four pre-access pages (QA'd for v0.1.0 in `review/QA-v0.1.0.md`) re-ran the automated and browser checks as a regression sweep.
Verdict: **all checklist items pass.** Two changes were applied during this pass and are listed under "Fixes applied".

## Method

- **Automated gate.** `bash scripts/check.sh docs/index.html docs/lessons/*.html` passes on all nine pages: title, no external or non-inlined resource references, quiz and pointer on every lesson, download block on every lesson 0004+, banned-word scan clean.
- **Browser harness.** Headless Chrome loaded every page from `file://` with console logging to stderr, validated against a probe page that deliberately logs and throws (both signals captured). A harness page (`--allow-file-access-from-files`) then loaded each lesson twice in iframes and drove each quiz twice: one run clicking every keyed option, one run clicking only wrong options.
- **Zip verification.** The base64 zip embedded in each lesson 0004+ was extracted and compared byte-for-byte against a fresh `scripts/pack.py` run over `assets/practice/<lesson>/` (the fixed timestamp makes packing deterministic). Each extracted folder then ran its exercise's starting command.
- **Editorial read.** A full read of the four applied lessons' visible text against their CURRICULUM.md specs: spine scan for version-sensitive facts, callout inventory, and the define-on-first-use spot check.
- **Time estimate.** The v0.1.0 house method: words in `<main>` at 200 words per minute, plus 45 seconds per quiz question.

## Checklist

### [x] Every page loads offline with no console error

Headless Chrome loaded all nine pages from `file://`. Zero `CONSOLE` lines (messages or uncaught errors) from any page. The capture method was validated first against a probe page that logs and throws — both appeared, so the clean result is a real pass, not a blind one. The quiz harness additionally loaded each lesson twice with scripting fully exercised.

### [x] Every quiz scores correctly

For all eight lessons (40 questions), the harness verified:

- Exactly 5 questions per quiz, 4 options per question, and every `data-correct` value matches an existing option.
- Correct-click run: feedback reads "Correct.", the explanation reveals, the question locks, and the final score reads "Score: 5 of 5."
- Wrong-click run: feedback reads "Not quite…", the chosen option is marked incorrect, the keyed option is highlighted, and the final score reads "Score: 0 of 5."
- Keyed answers spot-checked during the editorial read of 0004–0007: each keyed answer is the defensible one, and each distractor is wrong for a reason its lesson teaches (0004 q3's "whichever setup felt fastest" fails the mode-to-risk rule; 0007 q3's sunk-token options contradict the restart rule the lesson just derived).

### [x] Every exercise solved within its time box

Each applied lesson's exercise has a recorded end-to-end solve, run from the packed zip exactly as the learner receives it, in the PR that shipped the lesson:

| Lesson | Time box | Solve record |
|---|---|---|
| 0004 first win + setup | 10 min (first win) | PR #16 — `KeyError: 'call'` reproduced, one-line fix, README output matched exactly; CLAUDE.md trimmed 100→6 lines; balanced settings written and validated |
| 0005 guardrail + add-on | 10 min + 15 min | PR #17 — Stop hook fired on a question-only prompt (exit 2), agent fixed `slugify.py` not the test, hook cleared; add-on judged by the three questions |
| 0006 two sessions | 12 min | PR #18 — plan session wrote only PLAN.md; a cold build session carried it out; 10/10 tests OK, README example byte-for-byte |
| 0007 finale | 15 min | PR #19 — full habit chain, 9/9 tests OK, three bill answers recorded from the real cost views |

This pass re-verified each zip's starting state from the shipped pages: 0004 crashes with `KeyError: 'call'`, 0005 fails exactly one test, 0006 and 0007 pass all four tests — each exercise opens where its lesson says it does. The mechanical scope of every solve (a one-line fix; one settings paste; one plan file plus one small feature) fits its stated box; the boxes were judged against those recorded solves, not stopwatch-timed on a learner.

### [x] Every version-sensitive fact sits in a dated callout

Full read of the four applied spines: tier words and tool-generic names only — "the instructions file", "the mode that asks", "guardrail", "add-on", "helper", "the window bill", "the spend bill". Claude Code names, commands, keybindings, JSON syntax, and file locations sit only in callouts. Exercise steps name practice files (`README.md`, `wordstats.py`, `PLAN.md`, `.claude/settings.json`) as the Post-access rule requires (D40) — course material, not version-sensitive facts.

Callout inventory: 0004 has six (install and modes; the memory file; three settings examples; settings locations), 0005 has four (hooks; the guardrail block; skills; plugins and the marketplace), 0006 has two (session commands; subagents), 0007 has two (course-correction controls; cost views). All fourteen carry a visible "Verified 2026-10-30" and were verified against the current official docs during their build tasks — the same day as this pass, so no re-verification was due. The seven pre-access callouts stand at 2026-10-15/16 per the v0.1.0 QA.

### [x] Banned-word check clean

`check.sh`'s visible-text scan (D34 list plus insider-only peers) passes on all nine pages, including the rebuilt index. The scan runs inside the automated gate above.

### [x] Define-on-first-use spot check (D34)

Sampled across the four lessons, every industry term gets ordinary words at first use: *allow list / deny list* ("actions on an allow list run without a prompt, actions on a deny list never run at all", 0004); *exit code* ("the number every command hands the system when it ends, where zero means success", 0005); *slug* ("the lowercase, hyphen-separated form of a title that goes in a web address", 0005); *add-on* ("a folder of packaged instructions with a name and a one-line description", 0005); *marketplace* ("a catalog that lists plugins and where to fetch each one", 0005); *save point* ("a state you know is good, cheap to return to", 0006); *helper* ("a second, short-lived session… hands back only a summary", 0006); *the two bills* ("what fills the window right now, and what the session has spent in total", 0007).

### [x] Estimated completion time (house method)

| Lesson | Words | Read + quiz | Label |
|---|---|---|---|
| 0004 A4 | 2,555 | ~17 min | about 20 min |
| 0005 A5 | 2,762 | ~18 min | about 20 min |
| 0006 A6 | 2,026 | ~14 min | about 20 min |
| 0007 A7 | 2,111 | ~14 min | about 20 min |

Every applied lesson is under its 20-minute label by the house method. The pre-access pages re-measure within one minute of their v0.1.0 figures (lesson 0001 gained one meta line; see Fixes applied).

## Fixes applied during this pass

1. **Index rebuilt for the full track (task 8).** `docs/index.html` now lists all eight lessons in two sections (pre-access core, applied phase), carries the suggested-experience box (D35), and replaces the stale "what the full curriculum adds" bullets: the "Track A, continued" and "practice repo" bullets are gone (shipped, and superseded by in-page practice folders, D32), and the Track B bullet now catches lesson 0007's closing pointer to "the efficiency course" — a what-comes-next line, not a link, because B1 is outline-only. Version meta bumped to v0.2.0.
2. **D35 echo line added to lesson 0001.** The decision places the suggested-experience list on the index "with one echo line at the top of lesson 1"; the shipped 0001 predates D35 and had none. One `lesson-meta` line now opens its `<main>`. Quiz, structure, and checks re-verified by the harness after the edit.

## Known limitations (accepted, not bugs)

- **The time labels measure the page, not the practice.** Per the house method (and v0.1.0 precedent), "about 20 minutes" covers reading plus quiz. The hands-on boxes (10, 10+15, 12, and 15 minutes) overlap the step text but run beyond the label for a learner who does everything — lesson 0005 most of all, since both halves practice by design (D36). The applied-phase section of the index says "about 20 minutes each plus hands-on practice" for exactly this reason.
- **A3's walkthrough still does not print** (collapsed `<details>`, D29) — carried forward from the v0.1.0 QA, unchanged.
- **The solves are agent-run.** The recorded exercise solves prove the path works end to end from the shipped zips; they are not human timing data.
