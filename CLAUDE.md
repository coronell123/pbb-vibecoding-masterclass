# Project conventions — Vibecoding Masterclass

This file is read by Claude Code at the start of every session in this repo. Keep it short. Keep it true. ≤ 200 lines.

## What this repo is

A 4-hour masterclass on agentic coding with Claude Code. Hour 1 is a deep theory + demo session (slide deck in `slides/`). Hours 2-4 are hands-on exercises in `01-first-contact/` through `11-build/`. Reference demos with embedded screenshots live in `demos/`.

## The rhythm

Five steps. Always in this order:

```
SPEC  →  PLAN  →  TEST  →  IMPLEMENT  →  VERIFY
```

- **Spec**: checkable success criteria, written down.
- **Plan**: the recipe between spec and code. Read it like a senior engineer would.
- **Test**: at least one failing test before implementation.
- **Implement**: the boring step.
- **Verify**: run it, prove it, show the output.

Skip Verify and you didn't finish.

## When you're working in this repo

- **Use plan mode** for anything that touches more than one file.
- **Reference the spec** if it exists. Don't drift.
- **Write tests first** for any new function.
- **Never claim done without showing output** — paste the test result, the screenshot, the curl, the log.
- **Cite line numbers** (`file:line`) whenever you reference code.
- **No real client data** ever. Synthetic data only.

## What to avoid

- Long try/except blocks that swallow errors silently.
- Premature abstraction. Three callers is the rule of thumb for extracting a helper.
- Backwards-compat shims when there's nothing to be compatible with.
- Comments that explain what the code does. Names should do that.
- Generating slides without rendering them — always render and visually inspect.

## Project structure

| Path | What |
|---|---|
| `slides/build_deck.py` | Generates the 80-slide masterclass deck. Run with `python3 slides/build_deck.py`. |
| `slides/workshop.pptx` | The generated deck. Don't edit directly — regenerate. |
| `slides/assets/screens/` | Demo screenshots embedded in the deck. |
| `demos/` | Eight reference demos. Each has its own README and run command. |
| `01-first-contact/` … `11-build/` | Hands-on exercises in order. |
| `_handouts/` | Cheatsheet, anti-pattern bingo, plan critique checklist. |
| `_facilitator/` | Run-of-show, pre-workshop email. Instructor only. |
| `check.sh` | Pre-flight check for participants. |

## Building the deck

```bash
cd slides
python3 build_deck.py             # produces workshop.pptx
soffice --headless --convert-to pdf workshop.pptx   # produces workshop.pdf
```

## Capturing a new demo screenshot

```bash
# Take a screenshot at 1600×900 or smaller
# Save it under slides/assets/screens/<demo-id>-<seq>.jpg
# Reference it from a slide function in build_deck.py via embed_screenshot()
```

## House rules for the workshop day

The same rules apply to anyone (including you, Claude) working in this repo:

1. Trios, not duos — humans + Claude.
2. Show your plan before your code.
3. Evidence wins. "It works" is not done.
4. No real client data.
