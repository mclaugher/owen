# Curriculum

Read CONTEXT.md first. Use its terms. Generate lessons in this order, one per invocation of teach-curriculum.

## Sequence

| # | File | Lesson | Status |
|---|------|--------|--------|
| 0 | `0000-where-tokens-actually-go` | Shared primer | Specified below |
| 1 | `0001-the-mental-model` | A1 — Mental model | Specified below |
| 2 | `0002-scoping-and-modes` | A2 — Scoping, plan-before-code, modes | Specified below |
| 3 | `0003-reviewing-agent-output` | A3 — Reviewing output and security | Specified below |
| 4 | `0004-own-your-setup-1` | A4 — The .claude directory | Outline only; spec before generation |
| 5 | `0005-iteration-patterns` | A5 — Iteration patterns | Outline only |
| 6 | `0006-failure-and-recovery` | A6 — Failure modes, recovery, first audit | Outline only |
| 7 | `0007-audit-sessions` | B1 — Audit sessions (keystone) | Outline only |
| 8 | `0008-context-hygiene` | B2 — Context hygiene | Outline only |
| 9 | `0009-the-two-dials` | B3 — Right-sizing: model and thinking | Outline only |
| 10 | `0010-own-your-setup-2` | B4 — Setup ownership and sharing | Outline only |
| 11 | `0011-durable-state` | C1 — Plans and ADRs as durable state | Outline only |
| 12 | `0012-role-loops-and-routing` | C2 — Role loops and model routing | Outline only |
| 13 | `0013-parallel-sessions` | C3 — Parallel sessions | Outline only |

v0.1.0 ships lessons 0–3 (the pre-access core). Lessons 4–13 wait for their build cycle.

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
