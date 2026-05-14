# Run of Show — Vibecoding Masterclass (4h)

> Facilitator notes. Keep open on a second screen. **Hour 1 is the heavy deck.** Hours 2-4 are hands-on with the instructor floating.

---

## T-30 min — Setup

- Demo laptop: large terminal, dark theme, Claude Code authenticated
- Repo open in a browser tab
- Whiteboard with the five-step rhythm written large:
  `SPEC → PLAN → TEST → IMPLEMENT → VERIFY`
- House rules also on the board (Trios, Plan-First, Evidence, No-real-data)
- Slides open at slide 1 (`workshop.pdf` or `.pptx`)

---

## 00:00 — Block 0 — Arrival & Pair-Up (10 min)

| Min | What |
|---|---|
| 0–3 | Welcome. Show of hands: "Who has coded before? Who has used an AI coding tool before?" |
| 3–8 | Pair-up: heterogeneous pairs (one high-experience, one low). No exceptions. |
| 8–10 | Confirm everyone passed `check.sh`. Helper triages stragglers. |

**Cue line:** "Your pair is your buddy for the whole day. Two humans negotiate before you prompt. Claude is the third party."

---

## 00:10 — Hour 1 — The Deck (60 min)

Slide pacing — keep moving. Aim for ~45 sec/slide on average. Demo slides linger 2-3 min.

### Part 1: HOOK — slides 01-10 (10 min)
- Open big. Show the six demos with screenshots.
- The point isn't to explain every demo — it's to set the floor of "what's possible".

### Part 2: MINDSET — slides 11-18 (8 min)
- The three lies, deliberate and slow.
- End on the five-step rhythm slide. Point at the whiteboard.

### Part 3: WORKFLOWS — slides 19-42 (22 min)
- The dense section. Spend the most time here.
- Specs (4 slides), Plans (3 slides), Persistence Layer (4 slides), Tests (2 slides), Verify properly, Iteration, Drift, Orchestrator, Deployment, Checklist.
- Walk slowly through the orchestrator diagram (slide 39).

### Part 4: BEYOND CODING — slides 43-54 (8 min)
- Show that this isn't just a code tool.
- Highlight slide 52 (my own setup) — make it concrete.

### Part 5: AI/ML — slides 55-64 (6 min)
- Embed the real training output (slide 58).
- End on the open question (slide 64) — let the room sit with it.

### Part 6: ECOSYSTEM — slides 65-70 (4 min)
- Decision matrix on slide 69 is the takeaway slide.

### Part 7: BRIDGE — slides 71-76 (2 min)
- Quick. The point is to launch the hands-on.

### Part 8: CLOSE later — defer slides 77-80 until the end of hour 4

**Cue line at slide 76:** "Now stop watching. Start doing."

---

## 01:10 — Break (10 min)

- Quick pulse check: "Pace OK? Too dense?"
- Top up water/snacks.

---

## 01:20 — Hours 2-4 — Hands-On (170 min, includes one 15-min break)

The instructor is no longer presenting. You **float**.

### How to float

- Visit every pair every 20 minutes.
- First question always: "What's your plan?"
- Refuse to answer technical questions until you see the plan.
- Watch for spec drift — point it out gently.

### Exercise pacing — suggested

| Time | Block | What |
|---|---|---|
| 01:20–01:40 | `01-first-contact/` | Plan-only, no edits |
| 01:40–02:05 | `02-specs/` | Spec from a fuzzy wish |
| 02:05–02:20 | `03-plans/` | Critique three plans |
| 02:20–02:35 | **Short break** | 15 min |
| 02:35–02:55 | `04-tdd/` | Red-green-refactor |
| 02:55–03:05 | `05-debug/` | Root cause first |
| 03:05–03:20 | `06-subagents/` | Parallel investigators |
| 03:20–03:50 | `07-orchestrator/` OR `10-ml-scaffold/` | Pick by interest |
| 03:50–04:05 | `08-playwright/` OR `09-second-brain/` | Pick by interest |
| 04:05–04:20 | `11-build/` | Pick a micro-project, start shipping |

This schedule slips. That's fine. The point is depth on a few exercises, not breadth on all.

### Last 10 minutes

- Pull everyone back together.
- Show slides 77-80 (the close).
- Ask one pair to walk through their best plan from today.
- One thing each: "What will you do differently in your next coding session?"

---

## Backstops

- **Anthropic outage** — demos are cached as screenshots in the deck. Walk through them as case studies.
- **Half the room can't install** — pair them with someone who can. Non-installer drives the discussion.
- **Way ahead pair** — send them to `11-build/` early.
- **Way behind pair** — drop blocks 07, 08, 10. Focus on 02, 03, 04, 05.

---

## Recognition

Call out by name when you see:
- A particularly tight spec in block 02
- A pair that correctly refused Claude's plan in block 03
- The first correct root cause in block 05
- A pair whose orchestrator handoffs in block 07 were clean
- Any pair whose ML eval reading in block 10 surprised you
