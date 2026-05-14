# Block 3b — Systematic Debugging

**Time:** 10 min hands-on
**Goal:** Find the *root cause* before you ask Claude to fix anything.

---

## The mystery

`mystery.py` is supposed to print the **average daily temperature** from `weather.csv`. Instead it prints something wrong.

Run it:
```bash
python mystery.py
```

Compare what you see to what you'd expect.

---

## The rules

You **may not** type "fix it" or "what's wrong" into Claude. Those prompts produce guesses.

Instead, run this sequence:

1. **Reproduce.** Have Claude run the script and quote the wrong output.
2. **Hypothesize.**
   > Look at `mystery.py` and `weather.csv`. Propose one or two hypotheses for why the output is wrong. Don't fix anything yet.
3. **Test.** Pick the strongest hypothesis. Ask Claude:
   > Add a single print statement that would confirm or refute hypothesis #1. Then run.
4. **Fix only after the root cause is named.** Tell the instructor the root cause in **one sentence** before you write the fix.

---

## What counts as credit

You name the root cause in one sentence. The fix without the root cause does not count.

---

## Why this matters

When you ask AI "fix it", it will *probably* fix something. Sometimes the right something. Sometimes it'll silently change behavior that was correct. The discipline of naming the cause before the fix prevents both — and trains you to keep being the brain in the loop.
