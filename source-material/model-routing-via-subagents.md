# Source Material: Model Routing via Subagents

Seed material for Track C lesson 2 (role-based loops and model routing). Scrubbed of org references. Verify every claim against the current sub-agents documentation at authoring time: https://code.claude.com/docs/en/sub-agents. Model names below are current-as-of examples. Lessons use tier words (frontier, mid, small) in the spine and map names to tiers in dated callouts.

---

Model routing is natively supported. The `model` field in subagent frontmatter is the routing knob.

## Setup for the orchestrator/worker pattern

**1. Run the main session on the frontier model**

```bash
claude --model <frontier-alias>
```

**2. Define worker subagents pinned to smaller models** in `.claude/agents/` (project) or `~/.claude/agents/` (user):

```markdown
---
name: spec-implementer
description: Writes code from a fully-specified plan. Use when the spec is complete and no architectural decisions remain. Provide the spec file path, target files, and definition of done.
tools: Read, Write, Edit, Bash, Grep, Glob
model: sonnet
---
You implement exactly what the spec says. If the spec is ambiguous or requires a design decision, stop and report back rather than guessing.
```

The `model` field accepts an alias (e.g. `sonnet`, `opus`, `haiku`), a full model ID, or `inherit` (the default, which uses the main conversation's model). Without an explicit `model`, every subagent runs on the orchestrator's frontier model. That is the default trap to teach.

## Details worth knowing

- **Resolution order**: the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable (highest priority) → the per-invocation `model` parameter the orchestrator passes → frontmatter. The environment variable is a blunt "all subagents drop down a tier" hammer, and it overrides frontmatter. For per-agent granularity, leave it unset and pin in frontmatter.
- **Per-invocation override**: when the orchestrator invokes a subagent, it can pass a `model` parameter for that specific invocation. This enables escalation policy in CLAUDE.md: "dispatch spec-implementer on the mid tier normally; escalate to frontier only if the task involves concurrency or the agent fails twice."
- **The built-ins already do this**: the built-in Explore agent runs on a small model because fast, cheap search does not need a frontier model, while the general-purpose agent inherits the main model. Copy that logic: small models for read-only recon and grep-and-report agents, mid tier for from-spec implementation and code review, inherit/frontier only for work requiring real judgment.
- **Restrict delegation depth**: listing specific agents in the `tools` field (e.g. `Agent(worker, researcher)`) limits which subagents an agent can spawn. Omitting `Agent` entirely prevents the agent from spawning children. This is cost hygiene: a cheap worker must never recursively spawn frontier instances.

## Why the pattern works

The regime that makes routing pay: a fully-specified task with clean, scoped context. Given a durable-state loop architecture (dev-loop / review-loop with plans and decisions in files), the fit is natural. The frontier orchestrator writes the spec or task record to disk, then dispatches the pinned worker with a file path rather than pasted context. The fresh-context-per-unit-of-work discipline means the small model receives a clean, well-scoped prompt — which is exactly the regime where the mid tier matches frontier output quality.
