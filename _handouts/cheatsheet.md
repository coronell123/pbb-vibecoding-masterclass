# Vibecoding Cheatsheet — Claude Code

> *Open in a side tab on your laptop during the workshop. Repo URL is on the slide.*

## Commands you'll use today

| Command | What it does |
|---|---|
| `claude` | Open Claude Code in the current folder |
| `/plan` | Enter plan mode — Claude proposes, you approve |
| `/clear` | Reset the conversation (start fresh) |
| `/help` | List all built-in commands |
| `Ctrl-C` | Interrupt a runaway response |
| `@filename` | Attach a specific file to your message |
| `/review` | Ask for a code review of pending changes |
| `/security-review` | OWASP-style scan of your changes |
| Subagent prompt | "Spawn an Explore subagent to find X" |
| `/init` | Create a `CLAUDE.md` for your project |

## Five anti-patterns to avoid

1. **The Vague Prompt.** "Make this better." Claude has to guess. Be specific or use plan mode.
2. **Skipping the Plan.** Code-first lets Claude run wild. Plan-first lets you stay in the driver's seat.
3. **Trusting Without Testing.** "It works" is not a fact. Run it. Test it. Look at the output.
4. **Endless Edits Without Reset.** Long conversations drift. Use `/clear` and start fresh with context.
5. **"Fix It" Debugging.** Don't ask for fixes — ask for root cause first, then verify the fix.

## The four-step rhythm

```
PLAN  →  TEST  →  IMPLEMENT  →  VERIFY
```

If you skip step 4, you didn't finish. Paste the output. Show the green.
