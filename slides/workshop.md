---
marp: true
theme: default
paginate: true
backgroundColor: #fff
header: 'Vibecoding Workshop'
footer: 'Mahnoor AI course · Elias Jelinek'
style: |
  section { font-size: 28px; }
  h1 { font-size: 52px; color: #1a1a1a; }
  h2 { font-size: 38px; color: #1a1a1a; }
  code { background: #f0f0f0; padding: 2px 6px; border-radius: 4px; }
  pre code { font-size: 20px; }
  .small { font-size: 22px; color: #666; }
---

<!-- _class: lead -->

# Vibecoding

## with Claude Code

<br>

A 4-hour workshop on directing AI to ship real code.

<br>

<span class="small">Elias Jelinek · Mahnoor AI Course · 2026</span>

---

# House rules

1. **Trios, not duos.** You + your buddy + Claude.
2. **Show your plan before your code.**
3. **Evidence wins.** "It works" is not done.
4. **No real client data.** Synthetic only.

---

# What is "Vibecoding"?

> "I vibe-coded a startup in a weekend."

Sounds cool. Works in demos. **Falls apart at scale.**

We're going to learn what makes it fall apart, and how not to.

---

# The Bad Vibe Demo

I'm going to type something into Claude Code.

You watch.

> *"Build me a todo app with React and SQLite, make it nice."*

---

<!-- _class: lead -->

# Show of hands: would you ship this to a client?

---

# The Three Lies

AI coding tools tell us three things that aren't quite true.

---

# Lie 1: "It works."

It *looks* like it works.

The imports look right. The function signature looks right. The README looks right.

But did anyone run it?

**Discipline:** Verification before done.

---

# Lie 2: "I understand."

It pattern-matched your keywords.

It may have understood the surface. It rarely understands the *intent*.

**Discipline:** Write a spec. Or make Claude write one and review it.

---

# Lie 3: "I'm done."

"Done" is a status, not a feeling.

Done = the code is written **and** the tests pass **and** the verification ran **and** you saw the output.

**Discipline:** Stop conditions. Show your work.

---

# The four-step rhythm

<br>

```
PLAN  →  TEST  →  IMPLEMENT  →  VERIFY
```

<br>

This will be on the wall the whole day.

Skip step 4 and you didn't finish.

---

<!-- _class: lead -->

# Block 1 — First Contact (20 min)

`01-first-contact/`

You will **not** edit any code. Promise.

---

# Block 1 — What you'll do

1. Open Claude Code in the folder.
2. Have Claude **explain** `parser.py`.
3. Ask for **a plan** to improve it. Not code.
4. Read the plan. Critique it with your buddy.

---

# Reflection

What surprised you about how Claude responds when you don't ask for code?

(Think → Pair → Share — 2 / 1 / 2 min)

---

<!-- _class: lead -->

# Block 2 — Plan Before You Prompt

You are not the typist.
You are the reviewer.

---

# A good plan…

✅ States its assumptions out loud
✅ Names the files it will touch
✅ Proposes at least one test
✅ Stays scoped to what you asked
✅ Doesn't claim things it can't know

**A good plan is shorter than you expect.**

---

# Plan Mode Demo

I will:

1. Give Claude a fuzzy task in plan mode.
2. Read the plan aloud.
3. **Reject two parts.** Watch how.

---

# Your turn — Block 2 exercise

`02-plans/`

1. Pick **one** of the three feature requests.
2. Get a plan.
3. Run it through the **Plan Critique Checklist** in `_handouts/`.
4. Send **one** revision message.
5. Be ready to read your final plan title out loud.

---

# Why plans beat prompts

| 1-line prompt | 20-line plan |
|---|---|
| Claude guesses scope | Scope is fixed |
| Claude picks libraries | You pick libraries |
| You discover problems mid-code | You discover problems mid-plan |
| 30 min of corrections | 5 min upfront |

---

<!-- _class: lead -->

# ☕ Break — 15 min

Talk to me if the pace is off — too slow, too fast, lost somewhere.

---

<!-- _class: lead -->

# Block 3 — Test, Verify, Debug

If you can't measure "done", you're not done.

---

# TDD with Claude

Standard TDD. Just with Claude as the typist.

**Red → Green → Refactor.**

Demo: `parse_iban` — instructor lets Claude make the wrong call first, then corrects.

---

# Your turn — TDD exercise

`03-tdd/`

Build `validate_german_phone`.

1. Tests **first**. Show red.
2. Implement. Show green.
3. Refactor — only if simpler.

**Done = green pytest output on your terminal, seen by the instructor.** No output, no done.

---

# Systematic Debugging

There are two ways to ask AI to debug something.

| Bad | Good |
|---|---|
| "Fix it." | "Reproduce. Hypothesize. Test. Then fix." |
| Roulette | Science |

You'll be doing the second one.

---

# Bug Hunt — `03-debug/`

`mystery.py` is broken.

**Rule for credit:** name the root cause in one sentence **before** showing the fix.

The fix without the cause does not count.

---

<!-- _class: lead -->

# Block 4 — Powers

Subagents · Skills · MCP · Worktrees

You'll outgrow the basics. Bookmark these.

---

# Subagents = Delegate, don't multitask

You orchestrate. They investigate.

You spawn 3 in parallel → they each return a synthesis → you read → **you verify one claim yourself**.

The orchestrator is always you.

---

# Power tour (5 min each)

- **Slash commands & skills:** `/security-review`, custom skills
- **MCP servers:** Claude opens a browser, reads a page, screenshots
- **Worktrees:** isolated branches without polluting your main checkout

---

# Hooks — automate the verification step

A `pre-commit` hook that runs your tests.

If the tests fail, the commit fails. The verification step is no longer optional.

We'll set one up together.

---

<!-- _class: lead -->

# Block 5 — Build & Show

`05-build/`

30 min build. 15 min demo.

The plan walkthrough matters more than the demo working.

---

# Pick one

| Project | What |
|---|---|
| **whose-pr** | CLI tool listing open PRs in a GitHub repo |
| **Grade Cleaner** | Clean up a messy CSV of student grades |
| **Headlines** | Pull 10 RSS headlines into JSON |

Each project. Same rhythm. Same rules.

---

# Show & Tell

Three pairs. Three minutes each.

We're not grading whether it works.

We're grading whether you can **walk us through your plan**.

---

# When NOT to use Claude Code

- High-stakes security-critical code → human review mandatory
- Code with real client data → confidentiality rules apply
- "I don't know what I want yet" → talk to a human first
- 5-line tweaks → just type them

---

# Cheatsheet

In the repo: `_handouts/cheatsheet.md`

Repo stays open. Office hours: 30-min slots, next 2 weeks.

---

<!-- _class: lead -->

# Before you leave

Three questions on the whiteboard. Pick one to answer out loud, or email me later:

1. One thing you'll do differently.
2. What was unclear or too fast.
3. Would you recommend this to a peer? Why / why not?

---

<!-- _class: lead -->

# One thing to take home

<br>

```
PLAN  →  TEST  →  IMPLEMENT  →  VERIFY
```

<br>

In that order. Every time.

Thank you.
