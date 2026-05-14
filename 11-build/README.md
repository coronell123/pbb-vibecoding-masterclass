# Block 5 — Build & Show

**Time:** 30 min build + 15 min show & tell
**Goal:** Synthesize the whole day into a small, working artifact — **following the four-step rhythm.**

---

## The rhythm (visible on the wall the whole time)

```
PLAN  →  TEST  →  IMPLEMENT  →  VERIFY
```

The instructor will refuse technical questions until you show your plan.

---

## Pick ONE project

### Project 1 — `whose-pr` (CLI tool)

A Python or Node script. Takes a GitHub repo as input (e.g. `anthropics/claude-code`). Prints the open pull requests with: PR number, title, author, age in days.

- Use the public GitHub API (no auth needed for ~60 calls/hour).
- Handle: repo doesn't exist, no PRs, network error.
- Output is human-readable. Bonus: a `--json` flag.

### Project 2 — Grade Cleaner (data script)

`grades_messy.csv` (in this folder) has 200 rows of student grades. The data is messy:

- Inconsistent capitalization in names
- Some grades as "B+", some as "85", some as "85%"
- A few rows missing the grade column

Produce `grades_clean.csv` with: `student_name` (Title Case), `grade_numeric` (0–100, integer), and skip rows where the grade is missing. Print a one-line summary at the end.

### Project 3 — Headlines (web scrape)

Pick a public news site that publishes an RSS feed (e.g. `https://www.tagesschau.de/xml/rss2/`). Pull the top 10 headlines and write them to `headlines.json` with: `title`, `link`, `published`. No paid APIs.

---

## The rules

1. **Plan first.** Before writing any code, ask Claude for a plan. Show it to your buddy and the instructor.
2. **Tests next.** At least one test. For the CLI: a smoke test that runs `whose-pr` against a known small repo. For the data script: a test that runs on 5 hand-crafted rows.
3. **Implement.** Now you can ask for code.
4. **Verify.** Run it. Show the output. If a test exists, show green.

---

## At the end

Three pairs demo on the projector. The demo lasts 3 minutes. **The plan walkthrough matters more than the working artifact.** A clean process beats a flashy demo.
