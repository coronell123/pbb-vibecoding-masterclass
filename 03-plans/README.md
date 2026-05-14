# Block 2 — Would You Approve This Plan?

**Time:** 20 min hands-on
**Goal:** Get Claude to write a plan, then **review it like a senior engineer would.**

---

## Steps

1. Pick **one** of the three feature requests below. (Pick the one that interests you, not the easiest one.)

2. Open Claude Code in this folder. Tell it:
   > I want to add `<the feature you picked>`. Don't write code yet — give me a plan.

3. Read the plan. Run it through the **Plan Critique Checklist** card (handed to you at the start of Block 2).

4. Send **one** revision message to tighten the plan. Examples of good revision messages:
   - "Drop the backwards-compat shim — we don't need it."
   - "Add the specific test cases you'd write."
   - "You assumed X, but our codebase actually does Y. Adjust."

5. When you're happy with the revised plan, **read its title line out loud** when it's your pair's turn.

6. Quick discussion: which plans felt tight, which had hidden bloat?

---

## The three feature requests

### A) "Add a CSV export to the receipts parser."

Fuzzy on purpose. The parser is in `../01-first-contact/parser.py`. Claude does not know what CSV columns you want, where the file should go, or how the user triggers the export. Make Claude ask, or make Claude state assumptions.

### B) "Make the receipts parser handle multiple currencies."

Pretend the input now contains rows in USD and GBP, but the totals must be reported in EUR. Claude doesn't know your exchange rate source. Push back if it picks one without asking.

### C) "Add a CLI flag `--shop=REWE` to filter the output."

Looks simple. Notice what Claude proposes anyway — extra error handling? A logger? A new module? Apply the simplicity principle: cut anything that isn't strictly required.

---

## What "good" looks like

A plan you'd be happy to hand to a junior engineer and walk away. That means:

- States its assumptions out loud
- Names the exact files it will touch
- Proposes at least one test
- Doesn't quietly grow the scope
- Doesn't claim to know things it can't (e.g., "the existing convention is X" when there's no evidence)

When in doubt: cut it shorter.
