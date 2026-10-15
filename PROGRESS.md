## Summary

(empty — housekeeping compacts old entries into this section)

## Entries

Task 2: Lesson template, quiz widget, inliner [done]
Added the shared lesson assets and the build tooling. The template keeps its CSS in a separate `assets/lesson.css` (linked, then inlined) so `scripts/inline.py` exercises both the `<link>` and `<script src>` paths; the quiz markup contract (`data-correct` on the question, `data-option` on each button, hidden `.quiz-feedback`/`.quiz-explain` elements) is documented in `assets/quiz.js` — the teach-curriculum fork (task 3) must follow it. Template asset paths are `../../assets/...`, which resolve from both `docs/lessons/` and `scripts/fixtures/`. Strengthened `scripts/check.sh` to reject any remaining `src=` or `<link href>` after inlining; plain `<a href>` stays allowed so the task-8 index can link lessons. Verified: `python3 scripts/inline.py scripts/fixtures/sample-lesson.html /tmp/out.html && bash scripts/check.sh /tmp/out.html` passes, and negative cases (missing referenced file, external script, non-inlined fixture) all fail as intended.
Files touched: assets/lesson-template.html, assets/lesson.css, assets/quiz.js, scripts/inline.py, scripts/fixtures/sample-lesson.html, scripts/check.sh, PROGRESS.md
