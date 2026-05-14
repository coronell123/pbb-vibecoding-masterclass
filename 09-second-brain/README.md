# Block 09 — Second Brain

**Time:** 20 min hands-on
**Goal:** Wire up a `SessionEnd` hook so every Claude Code session leaves a note in your vault.

---

## Setup

Pick a folder to play with — your real Obsidian vault, a temporary `~/practice-vault/`, anywhere with markdown.

---

## The task

1. Open Claude Code in this folder.
2. Tell it:
   > Read `vault_example.md` and the demo at `../demos/06-second-brain/vault_tree.txt`.
   > Build me a `SessionEnd` hook that writes a note to `~/practice-vault/08-Sessions/YYYY-MM-DD-<project>.md`.
   > The note should include: what I worked on, decisions made, open questions.
   > Wire it up in `.claude/settings.json` for this repo. Plan first.
3. Approve. Implement.
4. Test: end the session, check that the note appeared. Read it. Is it useful?
5. Adjust the hook script to capture what's actually useful for **you**, not the generic template.

---

## Reference

`demos/06-second-brain/vault_tree.txt` shows what a working vault structure looks like — PARA, `08-Sessions/` for auto-generated session notes.

---

## What you're learning

That state doesn't have to die between sessions. The vault carries it forward. Tomorrow Claude reads what today Claude did.
