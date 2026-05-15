"""New slide functions to splice into build_deck.py."""

from build_deck import (
    Inches, Pt, Emu, RGBColor,
    SW, SH,
    NAVY, NAVY_DEEP, CREAM, WHITE, CORAL, INK, MUTED, RULE,
    CODE_BG, CODE_FG, CODE_GRN, CODE_RED, CODE_DIM, CODE_YEL, DIM_LIGHT,
    F_HEAD, F_BODY, F_CODE,
    add_rect, add_text, page_chrome, dark_footer, page_no,
    code_block, embed_screenshot, section_divider, colorize_terminal,
)


def sA_about_me(s):
    page_chrome(s, label="ABOUT THE INSTRUCTOR")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "WHO IS RUNNING THIS",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(1.5),
             "Hi. I'm Elias.", font=F_HEAD, size=64, color=NAVY, italic=True)
    add_text(s, Inches(0.8), Inches(3.0), Inches(7.5), Inches(0.4),
             "WHAT I DO",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), Inches(3.4), Inches(7.5), Inches(3),
             "I research AI agents for the founding phase of startups - "
             "how teams can use agentic systems to go from idea to MVP "
             "to first revenue with a fraction of the headcount.\n\n"
             "On the side, I build the thing I research:",
             font=F_HEAD, size=15, color=INK, line_spacing=1.45)
    add_rect(s, Inches(8.6), Inches(3.0), Inches(4.0), Inches(1.7), WHITE)
    add_rect(s, Inches(8.6), Inches(3.0), Inches(0.16), Inches(1.7), CORAL)
    add_text(s, Inches(8.85), Inches(3.15), Inches(3.7), Inches(0.4),
             "QUERSHIFT", font=F_BODY, size=12, color=NAVY,
             bold=True, letter_spacing=300)
    add_text(s, Inches(8.85), Inches(3.55), Inches(3.7), Inches(0.4),
             "Agentic AI startup",
             font=F_HEAD, size=15, color=CORAL, italic=True)
    add_text(s, Inches(8.85), Inches(3.95), Inches(3.7), Inches(0.7),
             "Building exactly the kind of system this masterclass teaches.",
             font=F_BODY, size=12, color=INK, line_spacing=1.4)
    add_rect(s, Inches(8.6), Inches(4.95), Inches(4.0), Inches(1.4), WHITE)
    add_rect(s, Inches(8.6), Inches(4.95), Inches(0.16), Inches(1.4), CORAL)
    add_text(s, Inches(8.85), Inches(5.1), Inches(3.7), Inches(0.4),
             "DIFFUSIONE", font=F_BODY, size=12, color=NAVY,
             bold=True, letter_spacing=300)
    add_text(s, Inches(8.85), Inches(5.5), Inches(3.7), Inches(0.4),
             "Side ventures",
             font=F_HEAD, size=15, color=CORAL, italic=True)
    add_text(s, Inches(8.85), Inches(5.9), Inches(3.7), Inches(0.45),
             "Where I keep building things by hand.",
             font=F_BODY, size=12, color=INK)
    add_text(s, Inches(0.8), Inches(6.45), Inches(7.5), Inches(0.4),
             "Plus a chair seat at the University of Duisburg-Essen - same topic.",
             font=F_HEAD, size=13, color=MUTED, italic=True)


def sB_what_we_build(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.4),
             "TIME TO BUILD AN MVP",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.7), Inches(12), Inches(2.2),
             "By 18:00 today,", font=F_HEAD, size=54, color=WHITE,
             italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(3.4), Inches(12), Inches(2.2),
             "you'll have shipped\nsomething real.",
             font=F_HEAD, size=54, color=CORAL,
             italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.5),
             "Pick one: a CLI tool - a data script - a small web scraper - a trained model.",
             font=F_HEAD, size=16, color=CREAM)
    dark_footer(s, label_left="")


def sC_what_vibe(s):
    page_chrome(s, label="DEFINITIONS  ·  01 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "First, two terms. They sound similar. They're not.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Vibe Coding.", font=F_HEAD, size=44, color=NAVY)
    add_rect(s, Inches(0.8), Inches(2.6), Emu(38100), Inches(3.0), CORAL)
    add_text(s, Inches(1.3), Inches(2.6), Inches(11.5), Inches(2),
             "“I described what I wanted in plain English\nand the AI built it.”",
             font=F_HEAD, size=26, color=NAVY, italic=True, line_spacing=1.3)
    add_text(s, Inches(1.3), Inches(4.4), Inches(11.5), Inches(0.5),
             "Fast. Magical. Often broken on the second input.",
             font=F_HEAD, size=18, color=CORAL, italic=True)
    add_text(s, Inches(1.3), Inches(4.95), Inches(11.5), Inches(0.4),
             "Great for prototypes. Great for solo weekends. Less great for clients.",
             font=F_BODY, size=14, color=INK, italic=True)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "The vibe is the prompt. The result is whatever Claude felt like producing.",
             font=F_HEAD, size=14, color=MUTED, italic=True)


def sD_what_agentic(s):
    page_chrome(s, label="DEFINITIONS  ·  02 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Where this masterclass actually lives.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Agentic Engineering.", font=F_HEAD, size=44, color=NAVY)
    top = Inches(2.7); h = Inches(3.5)
    add_rect(s, Inches(0.8), top, Inches(5.9), h, WHITE)
    add_rect(s, Inches(0.8), top, Inches(5.9), Inches(0.55), MUTED)
    add_text(s, Inches(1.1), top + Inches(0.13), Inches(5.5), Inches(0.4),
             "VIBE CODING", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, Inches(1.1), top + Inches(0.95), Inches(5.5), Inches(0.5),
             "Prompt -> result.", font=F_HEAD, size=18, color=NAVY, italic=True)
    add_text(s, Inches(1.1), top + Inches(1.6), Inches(5.5), Inches(2),
             "You ask. AI delivers. You verify (or don't).\n\n"
             "Works for: throwaway scripts, quick prototypes, fun.",
             font=F_BODY, size=13, color=INK, line_spacing=1.4)
    rx = Inches(7.0)
    add_rect(s, rx, top, Inches(5.5), h, WHITE)
    add_rect(s, rx, top, Inches(5.5), Inches(0.55), CORAL)
    add_text(s, rx + Inches(0.3), top + Inches(0.13), Inches(5), Inches(0.4),
             "AGENTIC ENGINEERING", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, rx + Inches(0.3), top + Inches(0.95), Inches(5), Inches(0.5),
             "Spec -> plan -> verify -> repeat.",
             font=F_HEAD, size=18, color=NAVY, italic=True)
    add_text(s, rx + Inches(0.3), top + Inches(1.6), Inches(5), Inches(2),
             "You stay the engineer. AI does the typing. "
             "Every step has evidence.\n\n"
             "Works for: clients, production systems, your career.",
             font=F_BODY, size=13, color=INK, line_spacing=1.4)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Today is about the right side. The left is just where we start.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


def sE_llm_primer(s):
    page_chrome(s, label="QUICK PRIMER  ·  01 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Forty seconds. Enough to understand what's actually happening.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What is an LLM?", font=F_HEAD, size=44, color=NAVY)
    boxes = [
        ("01", "TRAINED ON TEXT",
         "Read most of the internet, plus books, code, papers - once."),
        ("02", "PREDICTS NEXT TOKEN",
         "Given a sequence so far, returns the most likely next chunk."),
        ("03", "REPEATED",
         "Run that prediction over and over. The result looks like reasoning."),
    ]
    top = Inches(2.7); bw = Inches(3.95); gap = Inches(0.1)
    for i, (n, head, body) in enumerate(boxes):
        x = Inches(0.8) + (bw + gap) * i
        add_rect(s, x, top, bw, Inches(2.7), WHITE)
        add_rect(s, x, top, bw, Inches(0.5), CORAL)
        add_text(s, x + Inches(0.3), top + Inches(0.08), bw, Inches(0.35),
                 n, font=F_CODE, size=14, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.3), top + Inches(0.8), bw - Inches(0.4), Inches(0.5),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, x + Inches(0.3), top + Inches(1.45), bw - Inches(0.4), Inches(1.1),
                 body, font=F_BODY, size=13, color=INK, line_spacing=1.4)
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.4),
             "It is not a database. It is not a calculator. It is a very good guesser.",
             font=F_HEAD, size=14, color=INK, italic=True)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "Everything we'll learn today is about how to make the guessing useful.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


def sF_claude_vs_others(s):
    page_chrome(s, label="QUICK PRIMER  ·  02 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Same underlying tech. Very different products.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Claude - and where it sits.",
             font=F_HEAD, size=36, color=NAVY)
    rows = [
        ("CHATGPT", "OpenAI", "General-purpose chatbot, biggest mindshare, broadest API"),
        ("CLAUDE", "Anthropic", "Strong on long context, careful reasoning, agentic workflows"),
        ("GEMINI", "Google", "Tight Workspace integration, strong multi-modal"),
        ("LLAMA / MISTRAL", "Open weights", "Run locally or on your own infra; smaller, hackable"),
        ("CLAUDE CODE", "Anthropic CLI", "What we'll use today - a terminal-native agent harness"),
    ]
    top = Inches(2.5); rh = Inches(0.65)
    add_text(s, Inches(0.8), top, Inches(3.5), Inches(0.4),
             "MODEL", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_text(s, Inches(4.5), top, Inches(2.2), Inches(0.4),
             "VENDOR", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_text(s, Inches(7.0), top, Inches(6), Inches(0.4),
             "WHAT IT'S BEST AT", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_rect(s, Inches(0.8), top + Inches(0.4),
             SW - Inches(1.6), Emu(9525), RULE)
    for i, (model, vendor, body) in enumerate(rows):
        y = top + Inches(0.55) + rh * i
        col = CORAL if model == "CLAUDE CODE" else INK
        weight = model == "CLAUDE CODE"
        add_text(s, Inches(0.8), y, Inches(3.5), Inches(0.45),
                 model, font=F_HEAD, size=16, color=col, bold=weight, italic=True)
        add_text(s, Inches(4.5), y + Inches(0.03), Inches(2.2), Inches(0.45),
                 vendor, font=F_CODE, size=12, color=MUTED)
        add_text(s, Inches(7.0), y + Inches(0.03), Inches(6), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK)


def sG_maturity_ladder(s):
    page_chrome(s, label="THE MATURITY LADDER")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Where AI lives in your workflow. Each rung needs different tools.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Five levels of AI integration.",
             font=F_HEAD, size=30, color=NAVY)
    rungs = [
        ("01", "CHATBOT",        "Tab open. Copy-paste. Manual.",
         "ChatGPT, Claude.ai web"),
        ("02", "IDE INTEGRATION", "AI in your editor. Inline completions, side-chat.",
         "Cursor, Copilot, Continue"),
        ("03", "AGENTIC CODING",  "Terminal-native. Plans, edits, runs tests.",
         "Claude Code, Aider, Codex CLI"),
        ("04", "MULTI-AGENT",     "Orchestrator + subagents. Parallel work, verified handoffs.",
         "Agent Teams, custom harnesses"),
        ("05", "AUTO-DEV",        "Continuous: spec in, deployed code out. Human approves milestones.",
         "Anthropic Routines, Devin-class"),
    ]
    top = Inches(2.45); rh = Inches(0.7)
    for i, (n, name, body, examples) in enumerate(rungs):
        y = top + rh * i
        bar_w = Inches(0.6) + Inches(0.8) * i
        add_rect(s, Inches(0.8), y + Inches(0.1), bar_w, Inches(0.45),
                 CORAL if i >= 2 else MUTED)
        add_text(s, Inches(0.8) + bar_w + Inches(0.2), y, Inches(0.6), Inches(0.5),
                 n, font=F_CODE, size=13, color=CORAL)
        add_text(s, Inches(6.5), y + Inches(0.03), Inches(2.5), Inches(0.45),
                 name, font=F_HEAD, size=15, color=NAVY)
        add_text(s, Inches(6.5), y + Inches(0.38), Inches(6.5), Inches(0.3),
                 examples, font=F_CODE, size=10, color=MUTED, italic=True)
        add_text(s, Inches(9.2), y + Inches(0.03), Inches(4), Inches(0.5),
                 body, font=F_BODY, size=12, color=INK)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "Today we operate at levels 3 and 4 - and look at level 5.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


def sH_what_harness(s):
    page_chrome(s, label="THE HARNESS")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "What turns a chatbot into an agent. What Claude Code actually is.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What is an agent harness?",
             font=F_HEAD, size=32, color=NAVY)
    add_text(s, Inches(0.8), Inches(2.6), Inches(5.5), Inches(0.4),
             "THE SHORT VERSION",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), Inches(3.0), Inches(5.5), Inches(3.5),
             "A program that gives an LLM the ability to do things.\n\n"
             "Read files. Run commands. Call APIs. Loop until done. "
             "Stop when stuck. Ask for approval.\n\n"
             "The LLM is the brain. The harness is the body.",
             font=F_HEAD, size=15, color=INK, line_spacing=1.5)
    add_text(s, Inches(7.0), Inches(2.6), Inches(5.5), Inches(0.4),
             "WHAT'S INSIDE",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    components = [
        ("LLM CORE",        "The model. Predicts the next action."),
        ("TOOL LAYER",      "Read, Write, Edit, Bash, WebFetch, MCP servers."),
        ("CONTEXT MANAGER", "What's in the prompt right now. Files, memory, history."),
        ("LOOP / PLANNER",  "Decides what to do next. Detects done. Detects stuck."),
        ("PERMISSIONS",     "Asks before destructive actions. Sandboxes."),
    ]
    top = Inches(3.0); rh = Inches(0.66)
    for i, (lab, body) in enumerate(components):
        y = top + rh * i
        add_rect(s, Inches(7.0), y, Inches(5.5), Inches(0.55), WHITE)
        add_rect(s, Inches(7.0), y, Inches(0.14), Inches(0.55), CORAL)
        add_text(s, Inches(7.25), y + Inches(0.03), Inches(2.2), Inches(0.45),
                 lab, font=F_CODE, size=11, color=NAVY, bold=True)
        add_text(s, Inches(9.5), y + Inches(0.07), Inches(3), Inches(0.45),
                 body, font=F_BODY, size=11, color=INK)


def sI_lifecycle(s):
    page_chrome(s, label="THE FULL LIFECYCLE")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Real software has more than five steps. Here's the bigger loop.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Plan -> Test -> Implement -> Deploy -> Maintain.",
             font=F_HEAD, size=24, color=NAVY)
    steps = [
        ("01", "PLAN", "Spec it. Sketch the plan. Review."),
        ("02", "TEST", "Failing tests first. Define done."),
        ("03", "IMPLEMENT", "Code. Pass the tests."),
        ("04", "DEPLOY", "Ship to staging. Smoke-check."),
        ("05", "MAINTAIN", "Watch logs. Fix regressions. Loop."),
    ]
    top = Inches(2.6); bw = Inches(2.36); gap = Inches(0.06)
    for i, (n, head, body) in enumerate(steps):
        x = Inches(0.8) + (bw + gap) * i
        col = CORAL if i == 4 else NAVY
        add_rect(s, x, top, bw, Inches(2.5), WHITE)
        add_rect(s, x, top, bw, Inches(0.45), col)
        add_text(s, x + Inches(0.25), top + Inches(0.08), bw, Inches(0.3),
                 n, font=F_CODE, size=12, color=WHITE, bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.25), top + Inches(0.65), bw - Inches(0.4), Inches(0.4),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, x + Inches(0.25), top + Inches(1.2), bw - Inches(0.4), Inches(1.2),
                 body, font=F_BODY, size=12, color=INK, line_spacing=1.4)
        if i < 4:
            add_text(s, x + bw, top + Inches(1.0), gap, Inches(0.5),
                     "->", font=F_HEAD, size=18, color=CORAL, align="center")
    add_text(s, Inches(0.8), Inches(5.4), Inches(12), Inches(0.5),
             "back to PLAN.",
             font=F_HEAD, size=18, color=CORAL, italic=True, align="center")
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "Most teams stop at step 3. The whole point of agentic work is step 5.",
             font=F_HEAD, size=14, color=INK, italic=True)


def sJ_discussion_open(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "DISCUSSION  ·  04 MINUTES",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.5), Inches(12), Inches(3.5),
             "What's the most boring,\nmost repetitive thing\nyou do every week?",
             font=F_HEAD, size=46, color=NAVY,
             italic=True, line_spacing=1.1)
    add_rect(s, Inches(0.8), Inches(5.7), Inches(12), Inches(1.2), WHITE)
    add_text(s, Inches(1.1), Inches(5.85), Inches(11), Inches(0.4),
             "HOW TO DISCUSS",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(1.1), Inches(6.25), Inches(11), Inches(0.5),
             "Two minutes with your buddy. Then two pairs share with the room.",
             font=F_HEAD, size=15, color=INK, italic=True)
    page_no(s)


def sK_discussion_workflows(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "DISCUSSION  ·  05 MINUTES",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.5), Inches(12), Inches(3.5),
             "Where in your work today\ncould a spec save you\nthe most pain?",
             font=F_HEAD, size=44, color=NAVY,
             italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(5.6), Inches(12), Inches(0.4),
             "PROMPTS",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    pts = [
        "·  A client request that always comes back vague",
        "·  A feature you've rebuilt twice already",
        "·  A piece of code nobody remembers the reason for",
    ]
    for i, t in enumerate(pts):
        add_text(s, Inches(0.8), Inches(6.0) + Inches(0.32) * i,
                 Inches(12), Inches(0.3),
                 t, font=F_HEAD, size=14, color=INK)
    page_no(s)


def sL_discussion_beyond(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "DISCUSSION  ·  05 MINUTES",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.5), Inches(12), Inches(3.5),
             "Which integration\nwould change your day\nthe most?",
             font=F_HEAD, size=46, color=NAVY,
             italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(5.6), Inches(12), Inches(0.4),
             "PICK FROM YOUR LIST",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    pts = [
        "·  Email - drafts, triage, summaries",
        "·  Calendar - find-a-slot, prep notes",
        "·  Notion / Linear / Slack - status, blockers",
        "·  Browser - admin work, scraping, forms",
        "·  Vault - capture, distill, link",
    ]
    for i, t in enumerate(pts):
        add_text(s, Inches(0.8), Inches(6.0) + Inches(0.27) * i,
                 Inches(12), Inches(0.3),
                 t, font=F_HEAD, size=13, color=INK)
    page_no(s)


def sM_discussion_ecosystem(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "DISCUSSION  ·  04 MINUTES",
             font=F_BODY, size=11, color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.5), Inches(12), Inches(3.5),
             "If you had to pick\none tool for your\nnext project - which?",
             font=F_HEAD, size=46, color=NAVY,
             italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(5.7), Inches(12), Inches(0.4),
             "RULES",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), Inches(6.1), Inches(12), Inches(0.5),
             "State the project. State the choice. Defend it in one sentence.",
             font=F_HEAD, size=15, color=INK, italic=True)
    page_no(s)


def sN_outcome_plan_mode(s):
    page_chrome(s, label="PLAN MODE  ·  WHAT YOU ACTUALLY GET")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "From the plan above to the change on disk. Side by side.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Plan -> approved -> outcome.",
             font=F_HEAD, size=30, color=NAVY)
    add_text(s, Inches(0.8), Inches(2.3), Inches(6.0), Inches(0.4),
             "THE APPROVED PLAN",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    code_block(s, Inches(0.8), Inches(2.7), Inches(6.0), Inches(3.7),
               [("Plan", CODE_GRN),
                ("1. Extract token validation", CODE_FG),
                ("   -> auth/tokens.py", CODE_FG),
                ("2. Replace direct DB calls", CODE_FG),
                ("3. Add 5 unit tests", CODE_FG),
                ("", CODE_FG),
                ("Approved by Elias at 14:23", CODE_DIM)],
               size=12)
    add_text(s, Inches(7.0), Inches(2.3), Inches(5.7), Inches(0.4),
             "THE OUTCOME ON DISK",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    code_block(s, Inches(7.0), Inches(2.7), Inches(5.7), Inches(3.7),
               [("$ git diff --stat", CODE_FG),
                ("  auth/middleware.py  | -28 +6", CODE_FG),
                ("  auth/tokens.py      | +42 (new)", CODE_GRN),
                ("  tests/test_tokens.py| +73 (new)", CODE_GRN),
                ("  3 files, +121 -28", CODE_FG),
                ("", CODE_FG),
                ("$ pytest auth/", CODE_FG),
                ("  5 passed in 0.06s", CODE_GRN),
                ("", CODE_FG),
                ("$ git status", CODE_FG),
                ("  clean working tree", CODE_GRN)],
               size=12)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "The plan was the spec. The outcome was the implementation. Both reviewable.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


def sO_outcome_hooks(s):
    page_chrome(s, label="HOOKS  ·  WHAT YOU ACTUALLY GET")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The hook fires. The wrong commit gets blocked. The right one ships.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Hooks in action.", font=F_HEAD, size=32, color=NAVY)
    add_text(s, Inches(0.8), Inches(2.3), Inches(6.0), Inches(0.4),
             "FAILING COMMIT  ·  BLOCKED",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    code_block(s, Inches(0.8), Inches(2.7), Inches(6.0), Inches(3.7),
               [("$ git commit -m \"add CSV export\"", CODE_FG),
                ("", CODE_FG),
                ("[hook] pre-commit: ruff format --check", CODE_DIM),
                ("Would reformat: parser.py", CODE_RED),
                ("[hook] pre-commit: pytest -q", CODE_DIM),
                ("  test_round_trip       FAILED", CODE_RED),
                ("  AssertionError at line 47", CODE_RED),
                ("", CODE_FG),
                ("Commit blocked.", CODE_RED),
                ("$ ", CORAL)],
               size=12)
    add_text(s, Inches(7.0), Inches(2.3), Inches(5.7), Inches(0.4),
             "PASSING COMMIT  ·  SHIPS",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    code_block(s, Inches(7.0), Inches(2.7), Inches(5.7), Inches(3.7),
               [("$ git commit -m \"add CSV export\"", CODE_FG),
                ("", CODE_FG),
                ("[hook] pre-commit: ruff format --check", CODE_DIM),
                ("All formatted.", CODE_GRN),
                ("[hook] pre-commit: pytest -q", CODE_DIM),
                ("  3 passed in 0.04s", CODE_GRN),
                ("", CODE_FG),
                ("[main 7a3f2c1] add CSV export", CODE_GRN),
                (" 2 files changed, 49 +", CODE_GRN),
                ("$ ", CORAL)],
               size=12)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "The verify step is now part of the commit. You can't forget it.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


def sP_e2e_workflow(s):
    page_chrome(s, label="DEPLOYMENT  ·  THE FULL LOOP")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Spec to running service to alert to patch to redeploy. One rhythm.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The build-to-prod loop.", font=F_HEAD, size=38, color=NAVY)

    stages = [
        ("01", "SPEC",      "Checkable\nsuccess\ncriteria"),
        ("02", "PROJECT",   "Repo,\nCLAUDE.md,\nplan mode"),
        ("03", "BUILD",     "TDD rhythm,\nverify gate,\nartifact"),
        ("04", "DOCKER",    "Dockerfile,\ncompose,\nhealthcheck"),
        ("05", "DEPLOY",    "CI/CD,\nsmoke test,\nrollback"),
        ("06", "MAINTAIN",  "Logs,\nalerts,\npatch loop"),
    ]
    pill_w = Inches(1.9)
    pill_h = Inches(2.7)
    pill_y = Inches(2.55)
    gap    = Inches(0.12)
    total_w = pill_w * 6 + gap * 5
    start_x = (SW - total_w) / 2

    for i, (num, head, body) in enumerate(stages):
        x = start_x + (pill_w + gap) * i
        add_rect(s, x, pill_y, pill_w, pill_h, WHITE)
        add_rect(s, x, pill_y, pill_w, Inches(0.16), CORAL)
        add_text(s, x + Inches(0.22), pill_y + Inches(0.35), pill_w - Inches(0.44), Inches(0.35),
                 num, font=F_CODE, size=14, color=CORAL, bold=True)
        add_text(s, x + Inches(0.22), pill_y + Inches(0.78), pill_w - Inches(0.44), Inches(0.5),
                 head, font=F_HEAD, size=17, color=NAVY, bold=True)
        add_text(s, x + Inches(0.22), pill_y + Inches(1.3), pill_w - Inches(0.44), Inches(1.4),
                 body, font=F_BODY, size=11, color=INK, line_spacing=1.4)
        if i < 5:
            arr_x = x + pill_w - Inches(0.05)
            add_text(s, arr_x, pill_y + pill_h/2 - Inches(0.18), Inches(0.25), Inches(0.4),
                     ">", font=F_CODE, size=18, color=CORAL, bold=True, align="center")

    add_text(s, Inches(0.8), Inches(5.65), Inches(12), Inches(0.4),
             "Maintain feeds back into Spec. A bug ticket becomes a new line in the spec.",
             font=F_HEAD, size=14, color=INK, italic=True, align="center")
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Same five-step rhythm at every box. Claude does the typing. You hold the gates.",
             font=F_HEAD, size=14, color=CORAL, italic=True, align="center")


def sQ_docker_pattern(s):
    page_chrome(s, label="DEPLOYMENT  ·  CONTAINERIZATION")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Same image on your laptop and on the box. No more 'works on my machine'.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Wrap it in Docker.", font=F_HEAD, size=38, color=NAVY)

    code_block(s, Inches(0.8), Inches(2.4), Inches(7.4), Inches(4.1),
               [("# Dockerfile", CODE_DIM),
                ("FROM python:3.12-slim", CODE_FG),
                ("WORKDIR /app", CODE_FG),
                ("COPY requirements.txt .", CODE_FG),
                ("RUN pip install -r requirements.txt", CODE_FG),
                ("COPY src/ ./src", CODE_FG),
                ('HEALTHCHECK CMD curl -f localhost:8000/health', CORAL),
                ('CMD ["uvicorn", "src.main:app", "--host=0.0.0.0"]', CODE_FG),
                ("", CODE_FG),
                ("# docker-compose.yml", CODE_DIM),
                ('services:', CODE_FG),
                ('  api:  { build: ., ports: ["8000:8000"],', CODE_FG),
                ('          env_file: .env,', CODE_FG),
                ('          restart: unless-stopped }', CODE_GRN)],
               size=11)

    add_text(s, Inches(8.45), Inches(2.4), Inches(4.3), Inches(0.4),
             "WHY IT MATTERS", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    points = [
        ("Reproducibility",   "Same binary, every host."),
        ("Health checks",     "Restarts itself when broken."),
        ("Local-prod parity", "compose up runs what CI runs."),
        ("One-line deploy",   "Push image. Pull image. Done."),
        ("Easy rollback",     "Previous tag, one command away."),
    ]
    top = Inches(2.85)
    rh = Inches(0.7)
    for i, (head, body) in enumerate(points):
        y = top + rh * i
        add_text(s, Inches(8.45), y, Inches(4.3), Inches(0.32),
                 "·  " + head, font=F_HEAD, size=13.5, color=NAVY, bold=True)
        add_text(s, Inches(8.6), y + Inches(0.3), Inches(4.15), Inches(0.32),
                 body, font=F_BODY, size=11, color=INK, line_spacing=1.3)

    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.3),
             "Claude writes this for you. Same template every time.",
             font=F_HEAD, size=13, color=CORAL, italic=True, align="center")


def sR_maintain_observe(s):
    page_chrome(s, label="DEPLOYMENT  ·  MAINTAIN")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Shipped is not done. Done is shipped, observed, fixable.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "When prod cries, Claude reads the logs.",
             font=F_HEAD, size=30, color=NAVY)

    pillars = [
        ("LOGS",
         "Structured JSON.\nLevels: debug, info, warn, error.\nOne line per request, with a request-id.\nWrite to stdout — Docker captures it."),
        ("ALERTS",
         "Sentry / OTLP / Logflare.\nGroup by error fingerprint.\nPage on rate spike,\nnot on single events.\nLink alert → trace → log line."),
        ("PATCH LOOP",
         "Alert fires. Hand Claude the trace.\nClaude reads logs, reproduces locally,\nadds a failing test, fixes, redeploys.\nVerify gate is the same as before."),
    ]
    col_w = Inches(3.85)
    col_h = Inches(3.3)
    col_y = Inches(2.3)
    col_gap = Inches(0.2)
    total_w = col_w * 3 + col_gap * 2
    start_x = (SW - total_w) / 2

    for i, (head, body) in enumerate(pillars):
        x = start_x + (col_w + col_gap) * i
        add_rect(s, x, col_y, col_w, col_h, WHITE)
        add_rect(s, x, col_y, Inches(0.16), col_h, CORAL)
        add_text(s, x + Inches(0.4), col_y + Inches(0.3), col_w - Inches(0.55), Inches(0.4),
                 head, font=F_BODY, size=11, color=CORAL,
                 bold=True, letter_spacing=400)
        add_text(s, x + Inches(0.4), col_y + Inches(0.85), col_w - Inches(0.55), col_h - Inches(1.1),
                 body, font=F_HEAD, size=13.5, color=INK, line_spacing=1.5)

    code_block(s, Inches(0.8), Inches(5.7), Inches(11.7), Inches(0.85),
               [("$ ssh prod 'docker logs api --since 10m | grep ERROR' \\", CODE_FG),
                ("    | claude -p 'find the cause, write a failing test, then fix it'", CORAL)],
               size=11.5)
    add_text(s, Inches(0.8), Inches(6.65), Inches(12), Inches(0.3),
             "Logs are evidence. Evidence is what Claude is good at.",
             font=F_HEAD, size=13, color=MUTED, italic=True, align="center")


def sS_ml_frame(s):
    page_chrome(s, label="CAPSTONE  ·  AN ML PROJECT, START TO FINISH  ·  01")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Before any code: five questions. Write the answers down.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Frame the problem first.", font=F_HEAD, size=34, color=NAVY)

    items = [
        ("01", "What do I have?",
         "Shape of the data. Rows, columns, label balance, how clean. "
         "Open the CSV. Look at it. One sentence describing it."),
        ("02", "What do I want?",
         "Task type — classify, predict a number, cluster, generate. Be precise. "
         "A 'sentiment classifier' is not a task — '3-class sentiment on customer reviews' is."),
        ("03", "What does good look like?",
         "A number with a threshold. 'macro-F1 ≥ 0.80 on held-out 20%' is checkable. "
         "'Works well' is not. Decide before you train, not after."),
        ("04", "What's the constraint?",
         "CPU-only. Trains in under a minute. Fits on my laptop. Runs as a small Docker container. "
         "State this up front — it rules out the wrong models."),
        ("05", "What's the dumb baseline?",
         "Most-frequent-class. TF-IDF + logistic regression. If the dumb thing already clears the bar, "
         "ship that and go home."),
    ]
    top = Inches(2.4)
    rh = Inches(0.9)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.9), Inches(0.5),
                 n, font=F_CODE, size=22, color=CORAL)
        add_text(s, Inches(2.0), y + Inches(0.02), Inches(11), Inches(0.4),
                 head, font=F_HEAD, size=17, color=NAVY, bold=True)
        add_text(s, Inches(2.0), y + Inches(0.42), Inches(11), Inches(0.45),
                 body, font=F_BODY, size=12.5, color=INK, line_spacing=1.4)


def sT_ml_plan(s):
    page_chrome(s, label="CAPSTONE  ·  AN ML PROJECT, START TO FINISH  ·  02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Five answers become one spec. Hand the spec to Claude.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The spec I'd hand to Claude.", font=F_HEAD, size=30, color=NAVY)

    code_block(s, Inches(0.8), Inches(2.35), Inches(7.2), Inches(4.1),
               [("# SPEC — sentiment classifier on reviews", CODE_DIM),
                ("", CODE_FG),
                ("DATA       reviews.csv  ·  8k rows  ·  text + label", CODE_FG),
                ("TASK       3-class classification (pos/neg/neutral)", CODE_FG),
                ("", CODE_FG),
                ("SUCCESS    macro-F1 >= 0.80 on held-out 20%", CODE_GRN),
                ("           confusion matrix to results.json", CODE_GRN),
                ("", CODE_FG),
                ("CONSTRAINTS  CPU only  ·  train < 60s  ·  Docker", CORAL),
                ("             exposes /predict and /health", CODE_FG),
                ("", CODE_FG),
                ("BASELINE   most-frequent — beat by 30 pts", CODE_FG),
                ("MODEL      TF-IDF + LinearSVC", CODE_FG),
                ("NON-GOAL   no fine-tuning, no transformers", CODE_RED)],
               size=11)

    add_text(s, Inches(8.4), Inches(2.35), Inches(4.4), Inches(0.4),
             "THE RHYTHM", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    steps = [
        ("PLAN",      "Plan mode. Right model? Honest split?"),
        ("TEST",      "Smoke test before train. 3 in, labels out."),
        ("IMPLEMENT", "Approve. Claude writes pipeline + eval."),
        ("VERIFY",    "Run it. Beat baseline? Honest confusion?"),
        ("CONTAINER", "Dockerfile + compose. docker run, /predict."),
        ("DEPLOY",    "Push image. Smoke staging. Logs flowing."),
    ]
    top = Inches(2.8)
    rh = Inches(0.6)
    for i, (head, body) in enumerate(steps):
        y = top + rh * i
        add_text(s, Inches(8.4), y, Inches(2.0), Inches(0.3),
                 head, font=F_CODE, size=11, color=CORAL,
                 bold=True, letter_spacing=200)
        add_text(s, Inches(8.4), y + Inches(0.28), Inches(4.4), Inches(0.34),
                 body, font=F_BODY, size=10.5, color=INK, line_spacing=1.25)

    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.3),
             "The thinking is yours. The typing is Claude's.",
             font=F_HEAD, size=14, color=CORAL, italic=True, align="center")
