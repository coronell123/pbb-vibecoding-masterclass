# Plan Critique Checklist

> *Open this file in a side tab during Block 2. Use it on every plan Claude proposes — not just today.*

When Claude gives you a plan, walk through these five questions **before** you say "yes, go".

---

## 1. Does it state its assumptions out loud?

Look for explicit phrases like "I'm assuming X" or "this requires Y to exist".

If the plan reads like a confident command from someone who's seen the codebase 100 times — and Claude hasn't — that's a red flag. Push back.

---

## 2. Does it name the exact files it will touch?

Vague: "I'll update the parser logic."
Specific: "I'll edit `parser.py:42` and add `tests/test_parser.py`."

The specific version is reviewable. The vague version isn't.

---

## 3. Does it propose at least one test?

If the plan has no test step, it's incomplete. Ask: "What test will tell us this works?"

Exception: pure refactors with existing test coverage. Even then, the plan should *name* the existing tests it will rely on.

---

## 4. Is it scoped to what you asked?

Count the verbs. If you asked for one thing and the plan has 8 steps with 4 different verbs, scope creep is happening. Ask Claude to cut the optional parts.

Rule of thumb: **a good plan is shorter than you expected.**

---

## 5. Is it claiming things it cannot know?

"Following the existing convention…" — what convention? Did Claude actually read it?
"This is the standard approach…" — says who?

Anything that smells like a confident generality without a citation should be questioned. Ask: "Where did you see that?"

---

## When to walk away from the plan

If three or more of the five answers are weak, **don't revise the plan — start it over.** Sometimes a worse plan is salvageable. Sometimes it's better to clear the conversation and try again with a tighter prompt.
