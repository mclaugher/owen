## Summary

(empty — housekeeping compacts old entries into this section)

## Entries

Task 1: Vendor the teach skill at v1.3.1 [done]
Copied `skills/productivity/teach/` from github.com/mattpocock/skills at tag v1.3.1 (commit 24fe0ef7737efae15c87225755e9f6f5965e4888) into `vendored-skills/teach/`, verified the clone's HEAD matched the tag's resolved commit, and copied the repo's MIT LICENSE alongside it. VENDORING.md records tag, commit, retrieval date (2026-10-15), and a no-edit rule: fork into `.claude/skills/` instead of editing the vendored copy. Gotcha for task 3: the skill ships extra files beyond SKILL.md — `agents/openai.yaml`, GLOSSARY-FORMAT.md, LEARNING-RECORD-FORMAT.md, MISSION-FORMAT.md, RESOURCES-FORMAT.md — the fork spec only names SKILL.md, so decide there what the format files mean for the fork.
Files touched: `vendored-skills/teach/` (6 files), `vendored-skills/LICENSE`, `vendored-skills/VENDORING.md`.
