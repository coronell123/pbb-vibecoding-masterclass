# Spec — Tiny Todo CLI

## Why

A buddy-built CLI to practice the orchestrator pattern. Three features, three subagent runs.

## What

`todo.py` exposes three commands. All state lives in `tasks.json` next to the script.

## Checkable success criteria

### F1 — `add`
1. `python todo.py add "buy milk"` exits 0 and prints a confirmation with the assigned ID.
2. The task is appended to `tasks.json` with: `id` (int, auto-increment), `text` (string), `done` (bool, default False).
3. Empty text → exit code 2 with `error: empty task` on stderr.

### F2 — `list`
4. `python todo.py list` prints one line per **incomplete** task, format: `[<id>] <text>`.
5. No incomplete tasks → exit 0, prints "Nothing to do." on stdout.

### F3 — `done`
6. `python todo.py done 3` sets `done=True` on the task with id `3`.
7. Unknown id → exit code 2 with `error: no task with id <n>` on stderr.

## What it must NOT do

- Lose existing tasks when `tasks.json` already has data.
- Renumber IDs.
- Add a `delete` command, a `--help` flag beyond what argparse provides, or any colors.

## Out of scope

- Subtasks, tags, deadlines, priorities, projects.
- Web UI. Sync. Persistence beyond `tasks.json`.

## Tests

`tests/test_todo.py` exercises each criterion. Subagents are responsible for adding their feature's tests.
