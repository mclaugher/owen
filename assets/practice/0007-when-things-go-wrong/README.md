# Todo practice folder

Lesson 0007 ends the course inside this folder. One feature, every
habit, then the bill.

## What this is

`todo.py` is a small todo list. It stores items in `todo.txt`, one
line per item. `test_todo.py` holds four tests that define the
current behavior. All four pass: nothing here is broken. The work
is one new feature, done with every habit the course taught.

## Commands

- Add an item: `python3 todo.py add review the diff`
- Mark item 2 done: `python3 todo.py done 2`
- List items: `python3 todo.py list`
- Run the tests: `python3 -m unittest -v`

## The task: a sweep command

Add `python3 todo.py sweep`. The command moves every done item out
of `todo.txt` and appends it to `done.txt`, in the order the items
held in `todo.txt`, without the `[x]` mark. Open items stay in
`todo.txt` and keep their order. `done.txt` grows across sweeps;
sweep never erases it.

One possible shape, with items 1 and 3 marked done:

```
$ python3 todo.py list
1  [x] write the plan
2  [ ] review the diff
3  [x] commit the result
$ python3 todo.py sweep
swept 2 items
$ python3 todo.py list
1  [ ] review the diff
$ cat done.txt
write the plan
commit the result
```

Two decisions are deliberately left open. Decide both in your plan,
then hold the build to them:

1. What `sweep` prints. The example shows one good answer.
2. What `sweep` does when no item is done.

## Done when

- `python3 -m unittest -v` ends with `OK`.
- `test_todo.py` holds at least two new tests for `sweep`.
- A sweep like the example moves the done items into `done.txt`
  and leaves the open items in place.
