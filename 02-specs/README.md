# Block 02 — Specs

**Time:** 25 min hands-on
**Goal:** Convert a fuzzy client wish into a tight, checkable spec.

---

## The client wish

> "We need a way for our team to see who's doing what. The current setup is a mess. Make it work for everyone, not just the developers."

Read it twice. Notice what it does NOT tell you.

---

## Your task

1. Open Claude Code in this folder.
2. Tell Claude:
   > Read `client-wish.md`. Help me extract a spec. Use plan mode — don't write the spec for me yet, just help me question the wish.
3. Claude will propose 5–10 clarifying questions. Pick the top 3.
4. Now — you write the spec at `spec.md` using the structure from slide 21:
   - Why
   - What
   - 5 checkable success criteria
   - What it must NOT do
   - Out of scope
5. Have Claude critique your spec: "Read spec.md. Where would a senior engineer push back?"
6. Iterate once.

---

## Reference

See `demos/02-spec-plan-impl/spec.md` for an example of what "good" looks like — five checkable criteria, clear scope, explicit exclusions.

---

## The proof

Hand your spec to your buddy. Can they tell, **without asking you**, whether a given implementation satisfies it? If yes, your spec is good. If they keep asking clarifying questions, the spec isn't done yet.
