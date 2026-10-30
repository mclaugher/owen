# Tally practice folder

Lesson 0006 works inside this folder, across two sessions.

## What this is

`tally.py` is a small expense tracker. It stores entries in
`tally.csv`, one row per expense. `test_tally.py` holds four tests
that define the current behavior. All four pass: nothing here is
broken. The work is one new feature. The exercise is how you hand
that work from one session to the next.

## Commands

- Add an entry: `python3 tally.py add 4.60 coffee flat white`
- List entries: `python3 tally.py list`
- Run the tests: `python3 -m unittest -v`

## The task: a report command

Add `python3 tally.py report`. The command prints one line per
category with that category's total, largest total first. Equal
totals print in alphabetical order. A final `total` line carries
the grand total. With no entries it prints `no entries`, the same
as `list`.

One possible shape, after five adds (4.60 and 4.50 coffee,
12.00 and 12.00 lunch, 3.20 bus):

```
$ python3 tally.py report
lunch      24.00
coffee      9.10
bus         3.20
total      36.30
```

The exact spacing is a decision, not a given. Decide it in your
plan, then hold the build to it. The example shows one good
answer.

## The check

Work in this folder is done when `python3 -m unittest -v` ends
with `OK` and the run includes at least two new tests for
`report` — one for the grouping and order, one for the empty
case.

Re-download the folder for a fresh copy.
