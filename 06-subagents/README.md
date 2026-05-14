# Block 4 — Subagents: Delegate, Don't Multitask

**Time:** 10 min hands-on (after demo)
**Goal:** Spawn parallel investigators, read their reports, **then verify one of their claims yourself.**

---

## The setup

`sample_codebase/` is a small Python project — a fake URL shortener. It has bugs, opinions, and a half-baked test suite. You will not fix any of it.

---

## The task

Open Claude Code in this folder. Ask it to delegate to **three Explore subagents in parallel**:

1. **Agent 1:** find all places where the URL is validated.
2. **Agent 2:** list every external dependency and the version pinned.
3. **Agent 3:** find any place where a password or token might leak into logs.

Your prompt should look something like:
> Spawn three Explore subagents in parallel: (1) where is URL validation done? (2) what external dependencies and pinned versions? (3) any password/token leaking into logs? Synthesize all three reports for me.

---

## The trust step

Read the synthesis. Pick **one claim** from one of the agents and verify it yourself:

- If Agent 1 said "URL validation happens in `validators.py:42`" — open that file. Is it true?
- If Agent 2 listed `requests==2.31.0` — grep for it.
- If Agent 3 found a leak — read the code around the leak and decide if it's real.

Report to the instructor: *which claim did you verify and was the agent right?*

---

## The point

Subagents save you wall-clock time. They do **not** save you the responsibility of verifying their work. The orchestrator is you, even when the typing is done by something else.
