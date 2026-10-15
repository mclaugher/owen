# Plan: Pre-access core v0.1.0

Build and publish the pre-access core: the shared primer plus lessons A1–A3 as four self-contained HTML pages under `docs/`, ready for GitHub Pages. CURRICULUM.md holds every lesson spec; CONTEXT.md holds the terms; DECISIONS.md holds the settled design. Non-goals: the practice repo, lessons A4–A6, Tracks B and C, any org-specific content.

## Hard rules

- Write all course text in ste-style (`.claude/skills/ste-style/SKILL.md`). Address the working engineer.
- Ship each lesson as one self-contained HTML file. Make no external request. No CDN links.
- Require zero tool access in pre-access lessons. Embed all exercise material inline.
- Use tier words (frontier, mid, small) in the lesson spine. Put model names, commands, toggles, and limits only in dated callouts.
- Verify every current-tool-behavior claim against current official docs before it enters a lesson. Date the callout.
- End every lesson with a 5-question instant-feedback quiz, then the pointer.
- Build every example from publicly available material.
- Log every deviation from CURRICULUM.md or the vendored skill in DECISIONS.md.

## Tasks

### Wave 1

1. **Vendor the teach skill at v1.3.1**
   - Outcome: `vendored-skills/teach/` holds the full contents of `skills/productivity/teach/` from github.com/mattpocock/skills at release v1.3.1, plus that repo's MIT LICENSE file, plus `vendored-skills/VENDORING.md` recording the tag, the commit hash, and the retrieval date.
   - Touches: `vendored-skills/`
   - Tests: none to add; `bash scripts/check.sh` still passes.
   - Done when: `ls vendored-skills/teach/SKILL.md vendored-skills/LICENSE vendored-skills/VENDORING.md` succeeds and VENDORING.md names tag v1.3.1 and the commit hash.

2. **Lesson template, quiz widget, inliner**
   - Outcome: `assets/lesson-template.html` (clean typographic layout, print-friendly, light/dark via `prefers-color-scheme`, a `.dated-callout` style with a visible date slot, quiz section skeleton, pointer slot); `assets/quiz.js` (vanilla JS, 5 questions, instant per-answer feedback, no dependencies); `scripts/inline.py` (stdlib only) that takes a lesson HTML path and writes a copy with every local `<link>`/`<script src>` inlined; `scripts/check.sh` extended to verify each argument file has a `<title>`, a quiz block, a pointer line, no `http://` or `https://` resource references, and no local `src`/`href` references left.
   - Touches: `assets/`, `scripts/`
   - Tests: a committed fixture `scripts/fixtures/sample-lesson.html` built from the template.
   - Done when: `python3 scripts/inline.py scripts/fixtures/sample-lesson.html /tmp/out.html && bash scripts/check.sh /tmp/out.html` passes.

### Wave 2

3. **Fork teach into teach-curriculum**
   - Depends on: 1, 2
   - Outcome: `.claude/skills/teach-curriculum/SKILL.md`, forked from `vendored-skills/teach/SKILL.md`, with these changes and no others: read `personas/<persona>.md` in place of the live interview; generate exactly one lesson per invocation, next in CURRICULUM.md order; apply the CURRICULUM.md "Standards for every lesson" section; write the lesson with the template and widget from `assets/`; run `scripts/inline.py` as the final step, writing the single-file result to `docs/lessons/`; write a learning record to `learning-records/` with one "still shaky on X" item; pre-access lessons require zero tool access. Also write `personas/track-a-new-user.md`: a working engineer, competent in git and one mainstream language, new to agentic coding tools, skeptical of hype, short on time.
   - Touches: `.claude/skills/teach-curriculum/`, `personas/`
   - Tests: none to add; record the full diff-from-vendored summary in DECISIONS.md.
   - Done when: `ls .claude/skills/teach-curriculum/SKILL.md personas/track-a-new-user.md` succeeds and DECISIONS.md has the fork-diff entry.

### Wave 3

4. **Generate the shared primer**
   - Depends on: 3
   - Outcome: `docs/lessons/0000-where-tokens-actually-go.html` per the CURRICULUM.md lesson 0000 spec, generated with teach-curriculum, plus its learning record.
   - Touches: `docs/lessons/`, `learning-records/`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0000-where-tokens-actually-go.html` passes.

### Wave 4

5. **Generate A1 — Mental model**
   - Depends on: 4
   - Outcome: `docs/lessons/0001-the-mental-model.html` per the CURRICULUM.md lesson 0001 spec, opening with a spaced callback to the primer record's shaky item, plus its learning record.
   - Touches: `docs/lessons/`, `learning-records/`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0001-the-mental-model.html` passes.

### Wave 5

6. **Generate A2 — Scoping, plan-before-code, modes**
   - Depends on: 5
   - Outcome: `docs/lessons/0002-scoping-and-modes.html` per the CURRICULUM.md lesson 0002 spec, with mode specifics verified against current official docs and confined to dated callouts, plus its learning record.
   - Touches: `docs/lessons/`, `learning-records/`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0002-scoping-and-modes.html` passes.

### Wave 6

7. **Generate A3 — Reviewing agent output, and security**
   - Depends on: 6
   - Outcome: `docs/lessons/0003-reviewing-agent-output.html` per the CURRICULUM.md lesson 0003 spec: named full security section, embedded flawed diff with at least one security-class planted flaw, two of five quiz questions on security, plus its learning record.
   - Touches: `docs/lessons/`, `learning-records/`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0003-reviewing-agent-output.html` passes.

### Wave 7

8. **Site index, QA pass, changelog**
   - Depends on: 7
   - Outcome: `docs/index.html` (self-contained; links the four lessons; states what the full curriculum will add; same visual language as the template); a QA report at `review/QA-v0.1.0.md` covering: every lesson opens from `file://` with no console error, every quiz scores correctly, every version-sensitive fact sits in a dated callout, every lesson ends with quiz then pointer, estimated completion time per lesson is 20 minutes or less and one hour or less for the core; `CHANGELOG.md` entry for v0.1.0.
   - Touches: `docs/`, `review/`, `CHANGELOG.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/index.html docs/lessons/*.html` passes and `review/QA-v0.1.0.md` exists with every checklist item marked.
