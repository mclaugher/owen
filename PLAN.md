# Plan: Track A applied phase (lessons 4–7)

Build and publish lessons 0004–0007 as four self-contained HTML pages under `docs/`, each with its practice folder packed inside the page. `CURRICULUM.md` holds every lesson spec. `CONTEXT.md` holds the terms. DECISIONS.md entries D31–D36 hold the settled design from the 2026-10-28 design session. Non-goals: Tracks B and C, the transcript bundle, version tags, any org-specific content.

## Hard rules

- Write all course text in ste-style (`.claude/skills/ste-style/SKILL.md`). Address the working engineer.
- Ship each lesson as one self-contained HTML file. Make no external request. No CDN links.
- Pack each lesson's practice folder inside its own page behind a download button (D32). Use copy-paste blocks as the fallback for one or two tiny files.
- Author practice-folder sources under `assets/practice/<lesson>/`. Give any file a tool reads by name (CLAUDE.md, settings files) a `.seed` suffix. The packer restores the real name. Why: a build session must never ingest a deliberately bad CLAUDE.md.
- Solve every exercise end to end before you call its lesson done. Record the solve in the PR body.
- Define every industry term in ordinary words on first use (D34). Use no word from `scripts/banned-words.txt` in lesson text.
- Use tier words (frontier, mid, small) in the lesson spine. Put model names, commands, toggles, and limits only in dated callouts.
- Verify every current-tool-behavior claim against current official docs before it enters a lesson. Date the callout.
- End every lesson with a 5-question instant-feedback quiz, then the pointer.
- Build every example from publicly available material.
- Publish no expected token range and no learner comparison anywhere in Track A (D33).
- Log every deviation from CURRICULUM.md or the vendored skill in DECISIONS.md.

## Tasks

### Wave 1

1. **Practice-folder packer**
   - Outcome: `scripts/pack.py` (stdlib only) takes a source folder, a lesson HTML path, and an output path. It embeds the folder in the page and wires a download button that works offline from `file://`. It restores `.seed` names at pack time: a source file `CLAUDE.md.seed` downloads as `CLAUDE.md`. `scripts/check.sh` gains one check: every lesson page numbered 0004 or higher must contain the download block.
   - Touches: `scripts/pack.py`, `scripts/check.sh`, `scripts/fixtures/`
   - Tests: a committed fixture practice folder and a committed post-access fixture lesson. Packing the fixture passes `check.sh`. A post-access fixture page without the download block fails `check.sh`.
   - Done when: `python3 scripts/pack.py scripts/fixtures/practice-sample scripts/fixtures/post-access-lesson.html /tmp/packed.html && bash scripts/check.sh /tmp/packed.html` passes, and the unpacked fixture fails.

### Wave 2

2. **Banned-word list and plain-language check**
   - Depends on: 1
   - Outcome: `scripts/banned-words.txt` seeded per D34: orchestration, provenance, capstone, persona, "frontier" as a bare noun, and peers the session judges insider-only. `scripts/check.sh` rejects a lesson whose visible text contains a listed word.
   - Touches: `scripts/banned-words.txt`, `scripts/check.sh`, `scripts/fixtures/`
   - Tests: a fixture lesson containing a banned word fails `check.sh`. The four shipped lessons pass.
   - Done when: `bash scripts/check.sh docs/index.html docs/lessons/*.html` passes and the banned-word fixture fails.

3. **Update teach-curriculum for post-access lessons**
   - Depends on: 1
   - Outcome: the fork's build steps cover post-access lessons: author the practice folder under `assets/practice/<lesson>/` with `.seed` suffixes, run `scripts/pack.py`, name each practice file in the exercise text, and solve the exercise end to end before done. Record the diff in DECISIONS.md.
   - Touches: `.claude/skills/teach-curriculum/SKILL.md`, `DECISIONS.md`
   - Tests: none to add.
   - Done when: the fork SKILL.md states the post-access build steps and DECISIONS.md has the diff entry.

### Wave 3

4. **Generate lesson 0004 — First win, then make it yours**
   - Depends on: 2, 3
   - Outcome: `docs/lessons/0004-first-win-and-your-setup.html` per its CURRICULUM.md spec, opening with the spaced callback to record 0004, plus its learning record. Its practice folder: a small Python program with one planted bug that crashes with a clear error message, and a deliberately bloated `CLAUDE.md.seed`.
   - Touches: `docs/lessons/`, `assets/practice/0004-first-win-and-your-setup/`, `learning-records/`, `DECISIONS.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0004-first-win-and-your-setup.html` passes and the PR body records the solved exercise.

### Wave 4

5. **Generate lesson 0005 — Guardrails and add-ons**
   - Depends on: 4
   - Outcome: `docs/lessons/0005-guardrails-and-add-ons.html` per its CURRICULUM.md spec, full weight per D36: both halves teach and both halves practice. Its practice folder: a small program with one failing test as the guardrail target.
   - Touches: `docs/lessons/`, `assets/practice/0005-guardrails-and-add-ons/`, `learning-records/`, `DECISIONS.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0005-guardrails-and-add-ons.html` passes and the PR body records the solved exercise, including the guardrail firing and then clearing.

### Wave 5

6. **Generate lesson 0006 — Small sessions**
   - Depends on: 5
   - Outcome: `docs/lessons/0006-small-sessions.html` per its CURRICULUM.md spec, plus its learning record. Its practice folder: one task sized for a plan-then-build handoff across two sessions.
   - Touches: `docs/lessons/`, `assets/practice/0006-small-sessions/`, `learning-records/`, `DECISIONS.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0006-small-sessions.html` passes and the PR body records the two-session solve with the plan file.

### Wave 6

7. **Generate lesson 0007 — When things go wrong, and what it cost**
   - Depends on: 6
   - Outcome: `docs/lessons/0007-when-things-go-wrong.html` per its CURRICULUM.md spec, plus its learning record. Its practice folder: the finale feature task. The finale uses every habit and publishes no comparison (D33).
   - Touches: `docs/lessons/`, `assets/practice/0007-when-things-go-wrong/`, `learning-records/`, `DECISIONS.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/lessons/0007-when-things-go-wrong.html` passes and the PR body records the solved finale with the three cost-view answers.

### Wave 7

8. **Index update, QA pass, changelog**
   - Depends on: 7
   - Outcome: `docs/index.html` lists all eight pages and gains the suggested-experience box (D35). A QA report at `review/QA-applied-phase.md` covers: every page loads offline with no console error, every quiz scores correctly, every exercise solved within its time box, every version-sensitive fact in a dated callout, the banned-word check clean, and the define-on-first-use spot check done. A CHANGELOG.md entry.
   - Touches: `docs/`, `review/`, `CHANGELOG.md`
   - Tests: none to add.
   - Done when: `bash scripts/check.sh docs/index.html docs/lessons/*.html` passes and `review/QA-applied-phase.md` exists with every item marked.
