---
name: ste-style
description: Controlled-language rules for agent-facing docs. Use this skill when you write or edit a SKILL.md, a CLAUDE.md, a hook message, or agent instructions. Enforces simple words, short sentences, and one instruction per sentence.
---

# ste-style

Write agent-facing text in Simplified Technical English. Apply these rules.

## Rules

1. Write one instruction per sentence.
2. Keep every sentence to 20 words or fewer.
3. Use active voice. Name the actor. Write "Claude runs the test", not "the test is run".
4. Use approved simple words. Prefer "use" over "utilize". Prefer "start" over "initiate". Prefer "before" over "prior to".
5. Replace an ambiguous pronoun with the noun. Write "the hook blocks the command", not "it blocks it".
6. Use one term for one thing. Do not call it a "task" here and a "job" there.
7. Start each instruction with a verb. Write "Create the file", not "The file should be created".
8. Write positive instructions. Say what to do before you say what to avoid.
9. Split a long sentence at "and", "or", or a comma into separate sentences.
10. Cut filler words. Remove "just", "simply", "basically", "in order to".

## How to apply

- Read the target file first.
- Rewrite each sentence that breaks a rule.
- Keep the meaning identical.
- Do not change code, commands, or file paths.
- Report which rules you applied.
