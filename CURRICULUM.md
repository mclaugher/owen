# Curriculum

Read CONTEXT.md first. Use its terms. Generate lessons in this order, one per invocation of teach-curriculum.

## Sequence

| # | File | Lesson | Status |
|---|------|--------|--------|
| 0 | `0000-where-tokens-actually-go` | Shared primer | Specified below |
| 1 | `0001-the-mental-model` | A1 — Mental model | Specified below |
| 2 | `0002-scoping-and-modes` | A2 — Scoping, plan-before-code, modes | Specified below |
| 3 | `0003-reviewing-agent-output` | A3 — Reviewing output and security | Specified below |
| 4 | `0004-first-win-and-your-setup` | A4 — First win, then make it yours | Specified below |
| 5 | `0005-guardrails-and-add-ons` | A5 — Guardrails and add-ons | Specified below |
| 6 | `0006-small-sessions` | A6 — Small sessions | Specified below |
| 7 | `0007-when-things-go-wrong` | A7 — When things go wrong, and what it cost | Specified below |
| 8 | `0008-audit-sessions` | B1 — Audit sessions (keystone) | Outline only |
| 9 | `0009-context-hygiene` | B2 — Context hygiene | Outline only |
| 10 | `0010-the-two-dials` | B3 — Right-sizing: model and thinking | Outline only |
| 11 | `0011-own-your-setup-2` | B4 — Setup ownership and sharing | Outline only |
| 12 | `0012-durable-state` | C1 — Plans and ADRs as durable state | Outline only |
| 13 | `0013-role-loops-and-routing` | C2 — Role loops and model routing | Outline only |
| 14 | `0014-parallel-sessions` | C3 — Parallel sessions | Outline only |

v0.1.0 shipped lessons 0–3 (the pre-access core). Lessons 4–7 are the applied phase of Track A (D36); they build next. Lessons 8–14 wait for their build cycle.

## Standards for every lesson

- Write the lesson in ste-style (`.claude/skills/ste-style/SKILL.md`). Address the working engineer.
- Ship one self-contained HTML file in `docs/lessons/`. Make no external request. Pass `scripts/check.sh`.
- Keep the spine durable. Put every version-sensitive fact in a dated callout. Use tier words in the spine.
- Verify every current-tool-behavior claim against current official docs before it enters the lesson. Date the callout.
- End with a 5-question instant-feedback quiz, then the pointer.
- Keep the lesson completable in 20 minutes or less.
- Read the latest learning record first. Open with one spaced callback to the prior lesson's shaky item (primer excepted).
- Build every example from publicly available material.
- Pre-access lessons (0–3) require zero tool access. Embed all exercise material inline.
- Post-access lessons (4 and later) hand the learner a practice folder packed inside the page (D32). A download button saves the folder. Use copy-paste blocks as the fallback for one or two tiny files. Re-downloading resets the exercise. The exercise names each practice file by name.
- Define every industry term in ordinary words on first use (D34). Use no word from the banned-word list at `scripts/banned-words.txt` in lesson text.

## Lesson 0000 — Where Tokens Actually Go (shared primer)

Teach the core mental model.

- One context window holds everything: every message, every file read, every tool output.
- The window fills fast. Performance degrades as the window fills.
- Context degradation is the primary failure mode of agentic coding. Every best practice is downstream of this fact.
- Include the invest-to-save worked example: one planning session versus the debugging spiral the session prevents. Present it as a worked illustration with concrete numbers. Do not assert unmeasured multiples.
- Close with the quiz and the pointer.

## Lesson 0001 — A1: Mental model

- Open with a short recap of the primer. Build on it. Do not repeat it.
- Teach small, focused tasks as the highest-leverage habit. Derive the habit from the window model.
- Introduce the two dials: which model tier, and how hard the model thinks. Name the dials; depth comes in Track B.
- Present the first-wins menu: stack-trace analysis, refactoring, test generation, codebase questions.
- Frame each menu item as an instance of one property: bounded scope, checkable outcome, small context footprint.
- Include a worked stack-trace analysis inline.
- Quiz tests the property, not the menu list. Example question shape: "which of these tasks fits the pattern, and why?"

## Lesson 0002 — A2: Scoping, plan-before-code, and the mode system

- Teach where to spend tokens on purpose. Plan mode is the flagship discipline.
- Teach the full mode picture: read-only planning, approval-per-action, auto-accepted edits, unattended operation.
- Each mode trades control for flow. Match the mode to the risk of the work, not to your patience.
- State the verification rule: more autonomy granted means more verification owed.
- Restrict unattended modes to isolated environments.
- Teach when not to use the agent. Some tasks are faster by hand.
- Include an annotated transcript inline: a well-scoped planned task.
- Put mode names, toggles, and keybindings in dated callouts.

## Lesson 0003 — A3: Reviewing agent output, and security

- Teach verification habits and tests as guardrails.
- Include an annotated transcript of confident nonsense inline.
- Apply the verification rule from A2: scale review depth to the autonomy you granted.
- Include a named security section, full coverage, not a beat:
  - Credential handling. Injection paths. Architectural shortcuts.
  - The characteristic flaw patterns of AI-generated code.
  - The ownership norm: you own the code with your name on it.
- Embed a deliberately flawed code change as a static diff. Plant several defects. Include at least one security-class flaw. The lesson walks the review; the learner finds the flaws first.
- Two of the five quiz questions cover security.
- The pointer: review your team's last AI-assisted PR with this checklist.

## Lesson 0004 — A4: First win, then make it yours

- Open with the spaced callback to record 0004's shaky item: the checklist you keep retyping is configuration waiting to be written down.
- Run the first win before any teaching. The practice folder holds a small Python program with one planted bug that crashes with a clear error message. The learner downloads the folder, runs the program, hands Claude Code the error, and verifies the fix. Ten minutes. This is the learner's first real session.
- Teach CLAUDE.md: the file every session reads first. What belongs: the rules and checks you would otherwise retype. What does not: bloat, which costs tokens in every session. Tie the cost back to the primer.
- Teach permission settings through three example setups the learner reads and adapts: cautious, balanced, and hands-off-with-guardrails. Match the setup to the risk of the work, tying back to A2's verification rule. State that hands-off requires an isolated workspace.
- Exercise: the practice folder's CLAUDE.md is deliberately bloated. Trim it. Then write your own permission settings and state why you chose that setup.
- The quiz tests judgment (what belongs in CLAUDE.md, which setup fits which situation), not syntax.
- Put file names, settings syntax, and commands in dated callouts.
- The pointer: write a CLAUDE.md and permission settings for your own repo.

## Lesson 0005 — A5: Guardrails and add-ons

- This lesson carries full weight (D36): both halves teach, and both halves practice.
- Teach guardrails: a guardrail is a rule the tool enforces automatically, with no model judgment involved. State when a guardrail beats an instruction: use a guardrail for anything that must never happen.
- Walk one worked example through its full loop. The practice folder has a failing test. The learner adds the guardrail that blocks Claude Code from declaring work done while the test fails. The learner watches the block fire, fixes the test, and watches the work complete.
- Teach add-ons (skills): packaged instructions that load only when needed. Loading on demand beats loading everything always; tie the cost back to the primer. Teach judging add-ons one at a time, never adopting bundles wholesale.
- Exercise, two parts: add the guardrail to the practice folder; then install one skill from a public collection and answer three questions — what it loads, when it loads, and whether it earns its place.
- Put event names, file locations, and install commands in dated callouts.
- The pointer: add one guardrail your team's rules already imply to your own repo.

## Lesson 0006 — A6: Small sessions

- Teach three habits: start a fresh session for each task; write the plan into a file so the next session picks it up; use git commits as save points.
- Add one paragraph, no exercise: Claude Code can send out a helper to do research so the main session stays small. Name the idea; depth comes in a later course.
- Exercise: the practice folder holds a task sized for planning. Session one produces a plan file and nothing else. Session two starts fresh, reads the plan file, and does the work.
- Put session commands and resume specifics in dated callouts.
- The pointer: split your next real task into a plan session and a work session.

## Lesson 0007 — A7: When things go wrong, and what it cost

- Teach the warning signs of a session gone bad: the session forgets earlier instructions, repeats itself, or states wrong things with confidence. Tie back to A3: claims are not evidence.
- Teach the restart rule: restarting with a better brief is usually cheaper than arguing with a long session. Re-downloading the practice folder is the reset.
- Teach the cost view: how to open it, and how to read where the tokens went.
- Final exercise — the course finale, and it uses every habit: build one small feature in the practice folder start to finish. Plan it first (A2). Keep it small (A1). Verify the result (A3). Then open the cost view and answer three questions about where the tokens went. Publish no expected range; compare against nobody (D33).
- Close the course in two lines: what the learner can now do, and what the efficiency course adds.
- Put cost-view commands in dated callouts.
- The pointer: take the same look at your next real session.
