---
name: teach-curriculum
description: Generate the next lesson in CURRICULUM.md order from a persona file. One lesson per invocation.
disable-model-invocation: true
argument-hint: "Persona name (default: track-a-new-user)"
---

This skill is a fork of the vendored teach skill at `vendored-skills/teach/SKILL.md`. The fork generates the lessons of a fixed curriculum. All file paths in this skill start at the repo root.

Generate exactly one lesson per invocation. Generate the next lesson in CURRICULUM.md order. Read `personas/<persona>.md` in place of the live interview. Do not interview the user. Take the persona name from the invocation argument. When the invocation names no persona, use `personas/track-a-new-user.md`.

## Teaching Workspace

Treat the repo root as the teaching workspace. The state of the curriculum is captured in these files:

- `CURRICULUM.md`: the lesson sequence and every lesson spec. The "Standards for every lesson" section applies to every lesson.
- `CONTEXT.md`: the glossary. Use its terms in every output.
- `personas/*.md`: learner profiles. A persona file replaces the live interview.
- `./reference/*.html`: A directory of reference materials. These are the compressed learnings from the lessons - cheat sheets, reference algorithms, syntax, yoga poses, glossaries. They are the raw units of learning. They should be beautiful documents which print out well, and are designed for quick reference.
- `RESOURCES.md`: A list of resources which can be explored to ground your teaching in contextual knowledge, or to acquire knowledge and wisdom. Use the format in `vendored-skills/teach/RESOURCES-FORMAT.md`.
- `./learning-records/*.md`: A directory of learning records, which capture what the user has learned. These are loosely equivalent to architectural decision records in software development - they capture non-obvious lessons and key insights that may need to be revised later, or drive future sessions. These should be used to calculate the zone of proximal development. They are titled `0001-<dash-case-name>.md`, where the number increments each time. Use the format in `vendored-skills/teach/LEARNING-RECORD-FORMAT.md`. Each record ends with exactly one "still shaky on X" item.
- `docs/lessons/*.html`: A directory of lessons. A **lesson** is a single, self-contained HTML output that teaches one tightly-scoped thing tied to the mission. This is the primary unit of teaching in this workspace.
- `./assets/*`: Reusable **components** shared across lessons. See [Assets](#assets).
- `NOTES.md`: A scratchpad for you to jot down user preferences, or working notes.

## Philosophy

To learn at a deep level, the user needs three things:

- **Knowledge**, captured from high-quality, high-trust resources
- **Skills**, acquired through highly-relevant interactive lessons devised by you, based on the knowledge
- **Wisdom**, which comes from interacting with other learners and practitioners

Before the `RESOURCES.md` is well-populated, your focus should be to find high-quality resources which will help the user acquire knowledge. Never trust your parametric knowledge.

Some topics may require more skills than knowledge. Learning more about theoretical physics might be more knowledge-based. For yoga, more skills-based.

### Fluency vs Storage Strength

You should be careful to split between two types of learning:

- **Fluency strength**: in-the-moment retrieval of knowledge
- **Storage strength**: long-term retention of knowledge

Fluency can give the user an illusory sense of mastery, but storage strength is the real goal. Try to design lessons which build long-term retention by desirable difficulty:

- Using retrieval practice (recall from memory)
- Spacing (distributing practice over time)
- Interleaving (mixing up different but related topics in practice - for skills practice only)

## Lessons

A lesson is the main thing you produce: the unit in which knowledge and skills reach the user. Each lesson is one self-contained HTML file in `docs/lessons/`. CURRICULUM.md assigns each lesson's file name. Generate the first lesson in the CURRICULUM.md sequence table that has no file in `docs/lessons/`.

A lesson should be **beautiful**, with clean, readable typography and layout, since the user will return to these later to review. Think Tufte.

The lesson should be short, and completable very quickly. Learners' working memory is very small, and we need to stay within it. But each lesson should give the user a single tangible win that they can build on. It should be directly tied to the mission, and should be in the user's zone of proximal development.

If possible, open the lesson file for the user by running a CLI command.

Each lesson should link via HTML anchors to other lessons and reference documents.

Each lesson should recommend a primary source for the user to read or watch. This should be the most high-quality, high-trust resource you found on the topic.

Each lesson should contain a reminder to ask followup questions to the agent. The agent is their teacher, and can assist with anything that's unclear.

### Build steps

Apply the CURRICULUM.md "Standards for every lesson" section to every lesson. Build the lesson in these steps:

1. Start from `assets/lesson-template.html`. Fill every slot. Keep the quiz markup contract documented in `assets/quiz.js`.
2. Write the draft to `docs/lessons/<file>-draft.html`. The template's relative asset paths resolve from that directory.
3. Run `python3 scripts/inline.py docs/lessons/<file>-draft.html docs/lessons/<file>.html` as the final authoring step.
4. Delete the draft.
5. Run `bash scripts/check.sh docs/lessons/<file>.html`. Fix the lesson until the check passes.
6. Write a learning record to `learning-records/`. Use the format in `vendored-skills/teach/LEARNING-RECORD-FORMAT.md`. End the record with exactly one "still shaky on X" item. Name the one thing the persona would most likely still get wrong. The next lesson opens with a spaced callback to that item.

### Pre-access rule

Pre-access lessons (0000 through 0003) require zero tool access from the learner. Embed all exercise material inline. Do not ask the learner to run a tool, install anything, or leave the page to complete an exercise.

## Assets

Lessons are built from reusable **components**, stored in `./assets/`: stylesheets, quiz widgets, simulators, diagram helpers, and anything else a second lesson could reuse.

Reuse is the default, not the exception. Before authoring a lesson, read `./assets/` and build from the components already there. When a lesson needs something new and reusable, write it as a component in `./assets/` and link to it; never inline code a future lesson would duplicate.

A shared stylesheet is the first component every workspace earns: every lesson links it, so the lessons look like one consistent course rather than a pile of one-offs. As the workspace grows, so should the component library.

## The Mission

Every lesson should be tied into the mission - the reason that the user is interested in learning about the topic.

The persona file holds the mission. Read `personas/<persona>.md` before you design the lesson. Ground every teaching decision in the persona's mission, prior knowledge, and constraints. The CURRICULUM.md lesson spec fixes what the lesson covers.

When a persona needs to change, edit the persona file. Log the change in DECISIONS.md.

## Zone Of Proximal Development

Each lesson, the user should always feel as if they are being challenged 'just enough'.

CURRICULUM.md fixes the lesson order. Do not pick a different topic. Calibrate difficulty inside the lesson:

- Read the persona file for prior knowledge and constraints.
- Read the learning records for what earlier lessons established.
- Open the lesson with one spaced callback to the latest record's "still shaky on X" item. The primer takes no callback.

## Knowledge

Lessons should be designed around a skill the user is going to learn. The knowledge in the lesson should be only what's required to acquire that skill. You teach the knowledge first, then get the user to practice the skills via an interactive feedback loop.

Knowledge should first be gathered from trusted resources. Use `RESOURCES.md` to keep track of them. Lessons should be littered with citations - links to external resources to back up any claim made. This increases the trustworthiness of the lesson.

For acquiring knowledge, difficulty is the enemy. It eats working memory you need for understanding.

## Skills

If knowledge is all about acquisition, skills are about durability and flexibility. Make the knowledge stick.

For skill acquisition, difficulty is the tool. Effortful retrieval is what builds storage strength. Skills should be taught through interactive lessons. There are several tools at your disposal:

- Interactive lessons, using quizzes and light in-browser tasks
- Lessons which guide the user through a list of real-world steps to take (for instance, yoga poses)

Each of these should be based on a **feedback loop**, where the user receives feedback on their performance. This feedback loop should be as tight as possible, giving feedback immediately - and ideally automatically.

For quizzes, each answer should be exactly the same number of words (and characters, if possible). Don't give the user any clues about the answer through formatting.

## Acquiring Wisdom

Wisdom comes from true real-world interaction - testing your skills outside the learning environment.

When the user asks a question that appears to require wisdom, your default posture should be to attempt to answer - but to ultimately delegate to a **community**.

A community is a place (online or offline) where the user can test their skills in the real world. This might be a forum, a subreddit, a real-world class (budget permitting) or a local interest group.

You should attempt to find high-reputation communities the user can join. If the user expresses a preference that they don't want to join a community, respect it.

## Reference Documents

While creating lessons, you should also create reference documents. Lessons can reference these documents - they are useful for tracking raw units of knowledge useful across lessons.

Lessons will rarely be revisited later - reference documents will be. They should be the compressed essence of the lesson, in a format designed for quick reference.

Some learning topics lend themselves to reference:

- Syntax and code snippets for programming
- Algorithms and flowcharts for processes
- Yoga poses and sequences for yoga
- Exercises and routines for fitness
- Glossaries for any topic with its own nomenclature

Glossaries, in particular, are an essential reference. Once one is created, it should be adhered to in every lesson.

## `NOTES.md`

The user will sometimes express preferences of how they want to be taught, or things you should keep in mind. This is the place to record those preferences, so you can refer back to them when designing lessons or working with the user.
