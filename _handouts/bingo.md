# Anti-Pattern Bingo

> *On screen during Block 1, available in the repo. Copy this file to your laptop, mark a square every time you spot the anti-pattern — your own session OR another pair's.*

| | | | |
|---|---|---|---|
| **Hallucinated import** (imports a module that doesn't exist) | **Imaginary function** (calls an API that's not in the file) | **Phantom test** (writes a test for a function it didn't define) | **Confident wrong** ("This is the standard convention" — no source) |
| **Scope creep** (asked for X, delivered X + Y + Z) | **Unrequested refactor** (rewrote 3 other files "while I was here") | **Stealth comment graveyard** (left `# TODO`, `# old code`, `# kept for compat`) | **The fake "done"** ("done!" — never ran the code) |
| **The magic try/except** (swallows all errors silently) | **Premature abstraction** (3 layers of indirection for 2 callers) | **Backwards-compat shim** (you didn't ask for one) | **The optimistic await** (assumed an async API that's actually sync) |
| **The phantom flag** (added a `--verbose` you didn't ask for) | **Mislabeled refactor** ("just cleanup" — actually behavior change) | **Lost the thread** (forgot earlier constraint after 10 turns) | **Done without test** (changed code, didn't run tests) |

**Rules:**
- First pair to bingo (4 in a row, column, or diagonal) shouts "BINGO" — quick discussion of what they spotted.
- Cards stay live the whole day.
- If you spot one in your own session, you still mark it. Self-awareness is a skill.
