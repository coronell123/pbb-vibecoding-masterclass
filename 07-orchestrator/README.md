# Block 07 — Orchestrator Pattern

**Time:** 30 min hands-on
**Goal:** Build a small feature **feature-by-feature**, with the orchestrator pattern. Subagents per feature. Verified handoffs.

---

## The setup

A tiny todo CLI lives in `todo.py`. It's incomplete — three features are missing.

- **F1:** `todo add "buy milk"` should add a task.
- **F2:** `todo list` should list incomplete tasks with their IDs.
- **F3:** `todo done <id>` should mark a task complete.

The spec is `spec.md`. Read it first.

---

## Your task

You are the orchestrator. Claude is the worker. Each feature gets its own subagent run.

1. Read the spec out loud. Convince yourself you understand it.
2. For each feature, in this order:
   - Open a new Claude Code session (or `/clear`).
   - Tell it: "Here is the spec at `spec.md`. Implement **only F1**. Plan first."
   - Approve the plan.
   - Let it implement.
   - **Verify** before moving on: run the feature end-to-end. Run the tests. Read the diff.
3. Don't let one subagent touch more than its assigned feature. If it offers, refuse.

---

## The orchestrator rules

- Each subagent only knows about the spec and its assigned feature.
- Pass the spec by **file reference** (`spec.md`), not by copying it into the prompt.
- Before approving any plan, ask: does this stay inside the feature's scope?
- After each feature: paste the test output for your buddy to verify.

---

## What you're learning

That you don't multitask. The orchestrator (you) does. Subagents stay narrow. Handoffs are deliberate. Scope drift is what happens when you skip this discipline.
