# Block 08 — Playwright E2E

**Time:** 25 min hands-on
**Goal:** Generate E2E tests for the Pomodoro app — straight from its spec.

---

## Setup

```bash
cd ..
npm init -y && npm install -D @playwright/test
npx playwright install chromium
```

---

## The task

The Pomodoro app at `demos/01-mvp-pomodoro/index.html` has a behaviour spec hidden in the README. Your job: get Claude Code to generate Playwright tests for it.

1. Open Claude Code in this folder.
2. Tell it:
   > Read `../demos/01-mvp-pomodoro/index.html` and its `README.md`.
   > Generate a Playwright test file at `tests/pomodoro.spec.ts` that exercises:
   >  - initial state (25:00, FOCUS mode)
   >  - START button ticks the timer
   >  - PAUSE freezes
   >  - RESET returns to 25:00
   >  - localStorage persistence across reloads
   > Don't run anything yet. Show me the file. Plan mode.
3. Approve the plan. Let Claude write the file.
4. Run:
   ```bash
   npx playwright test
   ```
5. Iterate until green.

---

## Reference

`demos/07-playwright/test_pomodoro.spec.ts` is what "good" looks like for this exact problem. Don't peek until you've tried.

---

## What you're learning

That Playwright + Claude Code is the cheapest way to get E2E coverage on a web UI. Five tests in 90 seconds. Spec-first, generated, green.
