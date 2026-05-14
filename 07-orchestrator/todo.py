"""A tiny todo CLI. Three features missing — implement one at a time.

Spec: spec.md
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
STORE = HERE / "tasks.json"


def load():
    return json.loads(STORE.read_text()) if STORE.exists() else []


def save(tasks):
    STORE.write_text(json.dumps(tasks, indent=2))


def next_id(tasks):
    return (max((t["id"] for t in tasks), default=0)) + 1


def main(argv):
    if len(argv) < 2:
        print("usage: todo {add|list|done}", file=sys.stderr)
        return 2

    cmd = argv[1]

    if cmd == "add":
        # F1: implement me
        raise NotImplementedError("F1 — see spec.md")

    if cmd == "list":
        # F2: implement me
        raise NotImplementedError("F2 — see spec.md")

    if cmd == "done":
        # F3: implement me
        raise NotImplementedError("F3 — see spec.md")

    print(f"unknown command: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
