# Block 3a — TDD with Claude

**Time:** 15 min hands-on
**Goal:** See Red → Green → Refactor in action with Claude as the typist.

---

## The task

Build a function `validate_german_phone(s: str) -> bool` that returns:

- `True` for valid German phone numbers
- `False` for everything else

A *valid* German phone number for the purpose of this exercise:

- Starts with `+49 ` OR `0`
- Followed by 2–5 digit area code
- Followed by space or `-` or nothing
- Followed by 4–11 digits
- Optional spaces and dashes anywhere in the number part
- Total digit count (excluding the leading `+`): between 7 and 13

Examples:
- `+49 30 12345678` → True
- `030 12345678` → True
- `+49-89-1234567` → True
- `12345` → False (no prefix)
- `+44 20 1234 5678` → False (not Germany)
- `+49 30 12` → False (too few digits)

---

## The rules

1. Open Claude Code in this folder.
2. Your **first** instruction must be:
   > Write failing tests for `validate_german_phone` based on `README.md`. Do NOT implement the function yet. Run pytest and show me red.
3. Read the tests. Add or remove cases you care about.
4. Then:
   > Now implement the function. Show me green.
5. Then:
   > Look at the implementation. Can it be simpler? If yes, refactor. If no, say so and stop.

---

## The proof requirement

You are not done until the instructor has **seen the green pytest output** on your terminal.

No green output, no done. This is the rule of the day: **evidence over assertion.**

---

## Stretch (only if you finish early)

Add three "tricky" test cases your buddy would have missed. Compare them to your buddy's stretch cases.
