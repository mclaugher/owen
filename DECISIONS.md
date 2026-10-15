# Decisions

Log format: ID, decision, why. Append new entries at the end. Never rewrite an entry; supersede it with a new one.

## From the design session, 2026-10-15

- **D1 — Scope v0.1.0 to the pre-access core.** Primer + A1–A3 as self-contained HTML, live on GitHub Pages, tagged. Practice repo, A4–A6, Tracks B/C: scaffolded, not built. Why: external proposal deadline; the pre-access core is deliberately the zero-dependency unit.
- **D2 — Repo `owen`, public, practice repo as a future subdirectory.** Why: one clone, one version tag per release.
- **D3 — Engineer voice, one version.** Workshop audiences get live facilitation, supplements later. Why: the provenance ("built for working engineers") is the pitch.
- **D4 — First-wins menu kept, subordinated.** Menu items are instances of one property (bounded scope, checkable outcome, small context footprint); the quiz tests the property. Why: first-session success drives adoption; framing prevents bag-of-tricks reading.
- **D5 — Full security coverage in A3, one public version.** Named section: credentials, injection, architectural shortcuts, ownership norm; ≥1 security flaw planted in the embedded diff; 2 of 5 quiz questions. Why: safe agentic coding is universal, not org-specific. Stays a section, not a lesson, to hold the one-hour core promise.
- **D6 — Lessons ship as single self-contained HTML files.** Shared template and quiz widget inlined at generation time. Why: offline requirement, single-file distribution, no build system to maintain.
- **D7 — Hosting: GitHub Pages from `docs/` on main.** Why: free, no domain, static files serve a 100-person workshop trivially.
- **D8 — Vendor teach skill at release v1.3.1** (mattpocock/skills, MIT). Record tag + commit in vendored-skills/VENDORING.md; LICENSE travels with the copy. Source path: `skills/productivity/teach/`.
- **D9 — Minimal fork for v0.1.0.** Implemented: CURRICULUM.md sequencing, persona-file read, footer standard (quiz + pointer), zero-tool-access rule, asset inlining, learning records. Deferred: practice-repo exercise line (N/A pre-access), richer record simulation. Why: four artifacts do not need thirteen-lesson machinery.
- **D10 — Primer is its own page.** A1 recaps, never repeats. Why: Tracks B/C learners get the primer without A1; "13 lessons plus the shared primer" reads as separate artifacts.
- **D11 — One worked hook in A4, no full hooks lesson.** Why: one rule ("hooks enforce what must never depend on model judgment") needs one example; a hooks course is a tool tour.
- **D12 — Two-week applied window is a norm, not a gate.** The pre-access gate is enforced (access provisioning is the chokepoint); the applied window is held by managers, evidenced by the capstone share, never by revocation. The course recommends; the organization decides.
- **D13 — B4 capstone kept with a provided plugin skeleton.** The 30 minutes buy judgment, not plumbing. Fallback if QA overruns the box: packaging becomes optional, capstone is the report alone. Evidence decides.
- **D14 — No pre-release pilot cohort.** Cohort one is the pilot; the lesson-footer feedback link is the channel. Why: a mis-aimed spaced callback is a blemish, not a failure.
- **D15 — MCP exclusion stands; add a short loading note.** B1 notes that MCP tool loading behavior differs by setup: deferred (lazy) loading in the default setup, possibly disabled behind third-party API gateways. Verify against current docs at authoring; specifics in a dated callout. Frontmatter is taught as vocabulary when A4 first opens a skill file.
- **D16 — C3's only entry condition is work shape.** Independent pieces, clear ownership. Tooling is plain git (worktrees are universal). The lesson states the condition up front.
- **D17 — Transfer-gap trigger defined.** Capstone shares carry an optional "applied anything to real work yet?" line. Under one-third yes in cohort one promotes the flagship pointers to required homework.
- **D18 — Baselines are self-describing.** Each range publishes its config (tier, settings, thinking level) and date, with the sentence: read the comparison as directional once the model lineup changes. Track A content is durable; B/C refresh quarterly, no faster.
- **D19 — Future idea, recorded, not built: release-notes delta lessons.** Short "what changed since you took this" lessons for returning learners, on the release cadence.
- **D20 — Technique-report share template.** First field: what I changed and why. The number comes last. Beyond the template, sharing culture is a management matter, out of course scope.
- **D21 — All exercise material synthesized from publicly available sources** (public datasets, public coding tasks). Nothing recorded from real sessions, nothing to sanitize.
- **D22 — B4 capstone measures three things.** Token spend vs. baseline; setup footprint (what loads per session); allocation judgment via config-critique scenarios (spot the frontier model behind a small-model variable and the reverse; debug "it patches wrong": stale package context vs. underpowered model). Model names in scenarios live in dated callouts.
- **D23 — Plugins share subsets; dotfiles switch profiles.** B4 teaches packaging the additive subset (skills, commands, hooks) as a plugin; one sentence contrasts the personal dotfiles-branch approach. Why: the distinction confused a practitioner during design; the course resolves it in one line.
- **D24 — Pedagogy open questions 1–12 are all resolved** by D4, D5, D11–D18, D20, D21. No open question gates any future lesson's generation.
