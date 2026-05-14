"""
Build the Vibecoding Masterclass deck — 80 slides, ~60-min intro session.

Design system:
  - Editorial book-feel — Georgia headers + Calibri body + Consolas code
  - Sandwich: cream content slides, navy section dividers + opener/close
  - Single coral accent. No icons-in-circles. No accent lines under titles.
  - Lehrstuhl footer on every content slide.

Rhythm: SPEC → PLAN → TEST → IMPLEMENT → VERIFY
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


HERE = Path(__file__).parent
OUT  = HERE / "workshop.pptx"

prs = Presentation()
prs.slide_width  = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
blank_layout = prs.slide_layouts[6]

NAVY      = RGBColor(0x14, 0x21, 0x3D)
NAVY_DEEP = RGBColor(0x0B, 0x14, 0x29)
CREAM     = RGBColor(0xFA, 0xF7, 0xF0)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
CORAL     = RGBColor(0xE8, 0x76, 0x1B)
INK       = RGBColor(0x1A, 0x1A, 0x1A)
MUTED     = RGBColor(0x6B, 0x6B, 0x6B)
RULE      = RGBColor(0xE5, 0xE0, 0xD5)
CODE_BG   = RGBColor(0x1E, 0x21, 0x27)
CODE_FG   = RGBColor(0xE6, 0xE6, 0xE6)
CODE_GRN  = RGBColor(0x98, 0xC3, 0x79)
CODE_RED  = RGBColor(0xE0, 0x6C, 0x75)
CODE_DIM  = RGBColor(0x7F, 0x84, 0x8A)
CODE_YEL  = RGBColor(0xE5, 0xC0, 0x7B)
DIM_LIGHT = RGBColor(0x88, 0x99, 0xB0)

F_HEAD = "Georgia"
F_BODY = "Calibri"
F_CODE = "Consolas"


def add_rect(slide, x, y, w, h, rgb):
    s = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = rgb
    s.line.fill.background()
    return s


def add_text(slide, x, y, w, h, text, *,
             font=F_BODY, size=14, color=INK, bold=False, italic=False,
             align="left", valign="top", line_spacing=1.15, letter_spacing=None):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True
    tf.vertical_anchor = {"top": MSO_ANCHOR.TOP, "middle": MSO_ANCHOR.MIDDLE,
                          "bottom": MSO_ANCHOR.BOTTOM}[valign]
    lines = text.split("\n") if isinstance(text, str) else text
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER,
                       "right": PP_ALIGN.RIGHT}[align]
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = line
        r.font.name = font
        r.font.size = Pt(size)
        r.font.color.rgb = color
        r.font.bold = bold
        r.font.italic = italic
        if letter_spacing is not None:
            rPr = r._r.get_or_add_rPr()
            rPr.set("spc", str(letter_spacing))
    return tb


CURRENT_PAGE = 1   # set by main() before each slide builds


def page_chrome(slide, *, label="", bg=CREAM, page_num=None, total=None):
    add_rect(slide, 0, 0, SW, SH, bg)
    add_rect(slide, Inches(0.6), SH - Inches(0.65), SW - Inches(1.2), Emu(9525), RULE)
    add_text(slide, Inches(0.6), SH - Inches(0.55), Inches(7), Inches(0.35),
             "CHAIR OF SUSTAINABILITY AND INNOVATION IN DIGITAL ECOSYSTEMS  ·  UNIVERSITY OF DUISBURG-ESSEN",
             font=F_BODY, size=8, color=MUTED, letter_spacing=120)
    if label:
        add_text(slide, Inches(0.6), SH - Inches(0.3), Inches(7), Inches(0.25),
                 label, font=F_BODY, size=8.5, color=NAVY, bold=True, letter_spacing=200)
    pn = page_num if page_num is not None else CURRENT_PAGE
    tt = total if total is not None else TOTAL
    add_text(slide, SW - Inches(1.5), SH - Inches(0.5), Inches(0.9), Inches(0.3),
             f"{pn:02d} / {tt:02d}",
             font=F_CODE, size=9, color=MUTED, align="right")


def dark_footer(slide, page_num=None, total=None, label_left=""):
    if label_left:
        add_text(slide, Inches(0.8), Inches(0.9), Inches(12), Inches(0.4),
                 label_left, font=F_BODY, size=11, color=CORAL,
                 bold=True, letter_spacing=400)
    pn = page_num if page_num is not None else CURRENT_PAGE
    tt = total if total is not None else TOTAL
    add_text(slide, Inches(0.8), SH - Inches(0.55), Inches(9), Inches(0.35),
             "CHAIR OF SUSTAINABILITY AND INNOVATION IN DIGITAL ECOSYSTEMS  ·  UNIVERSITY OF DUISBURG-ESSEN",
             font=F_BODY, size=8, color=DIM_LIGHT, letter_spacing=120)
    add_text(slide, SW - Inches(1.5), SH - Inches(0.55), Inches(0.9), Inches(0.3),
             f"{pn:02d} / {tt:02d}",
             font=F_CODE, size=9, color=DIM_LIGHT, align="right")


def page_no(slide, light=False):
    """Bare page-number marker for special-layout slides."""
    add_text(slide, SW - Inches(1.5), SH - Inches(0.5), Inches(0.9), Inches(0.3),
             f"{CURRENT_PAGE:02d} / {TOTAL:02d}",
             font=F_CODE, size=9, color=DIM_LIGHT if light else MUTED, align="right")


def code_block(slide, x, y, w, h, lines, *, fg=CODE_FG, bg=CODE_BG, size=14):
    add_rect(slide, x, y, w, h, bg)
    pad = Inches(0.28)
    tb = slide.shapes.add_textbox(x + pad, y + pad, w - 2*pad, h - 2*pad)
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    tf.word_wrap = True
    first = True
    for ln in lines:
        if isinstance(ln, tuple):
            txt, col = ln
        else:
            txt, col = ln, fg
        if first:
            p = tf.paragraphs[0]
            first = False
        else:
            p = tf.add_paragraph()
        p.line_spacing = 1.35
        r = p.add_run()
        r.text = txt
        r.font.name = F_CODE
        r.font.size = Pt(size)
        r.font.color.rgb = col


def embed_screenshot(slide, path, x, y, w, h, caption=""):
    add_rect(slide, x - Emu(9525), y - Emu(9525),
             w + Emu(19050), h + Emu(19050), RULE)
    p = HERE / "assets" / "screens" / path
    if p.exists():
        slide.shapes.add_picture(str(p), x, y, width=w, height=h)
    else:
        add_rect(slide, x, y, w, h, WHITE)
        add_text(slide, x, y + h/2 - Inches(0.2), w, Inches(0.4),
                 f"[ {path} ]", font=F_CODE, size=12,
                 color=MUTED, align="center", italic=True)
    if caption:
        add_text(slide, x, y + h + Inches(0.1), w, Inches(0.3),
                 caption, font=F_BODY, size=10, color=MUTED, italic=True)


def section_divider(slide, *, label, title, sub="", page=None, total=None):
    add_rect(slide, 0, 0, SW, SH, NAVY_DEEP)
    add_text(slide, Inches(0.8), Inches(0.9), Inches(12), Inches(0.4),
             label, font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(slide, Inches(0.8), Inches(2.3), Inches(12), Inches(2.6),
             title, font=F_HEAD, size=64, color=WHITE,
             italic=True, line_spacing=1.05)
    if sub:
        add_text(slide, Inches(0.8), Inches(5.0), Inches(12), Inches(0.6),
                 sub, font=F_HEAD, size=20, color=CREAM)
    add_text(slide, SW - Inches(1.5), Inches(0.9), Inches(0.8), Inches(0.4),
             "→", font=F_CODE, size=18, color=CORAL, align="right")
    add_text(slide, Inches(0.8), SH - Inches(0.55), Inches(9), Inches(0.35),
             "CHAIR OF SUSTAINABILITY AND INNOVATION IN DIGITAL ECOSYSTEMS",
             font=F_BODY, size=8, color=DIM_LIGHT, letter_spacing=120)
    pn = page if page is not None else CURRENT_PAGE
    tt = total if total is not None else TOTAL
    add_text(slide, SW - Inches(1.5), SH - Inches(0.55), Inches(0.9), Inches(0.3),
             f"{pn:02d} / {tt:02d}",
             font=F_CODE, size=9, color=DIM_LIGHT, align="right")


def _read(p):
    full = HERE.parent / p
    return full.read_text() if full.exists() else f"[ missing: {p} ]"


DEMO3 = _read("demos/03-multi-agent/orchestrator_log.txt")
DEMO4 = _read("demos/04-browser/session.txt")
ML_OUT = _read("demos/05-ml-classifier/training_output.txt")
VAULT = _read("demos/06-second-brain/vault_tree.txt")
PLAYWRIGHT = _read("demos/07-playwright/test_pomodoro.spec.ts")
CRON = _read("demos/08-automation/cron_output.txt")


def colorize_terminal(text, max_lines=22):
    out = []
    for ln in text.splitlines()[:max_lines]:
        s = ln.lstrip()
        if s.startswith(">"):
            out.append((ln, CORAL))
        elif "PASSED" in ln or "✓" in ln or "passed" in ln:
            out.append((ln, CODE_GRN))
        elif "FAILED" in ln or "✗" in ln or "Error" in ln:
            out.append((ln, CODE_RED))
        elif s.startswith("[") and ln.rstrip().endswith("]"):
            out.append((ln, CODE_DIM))
        elif s.startswith("$") or s.startswith("#"):
            out.append((ln, CODE_DIM))
        else:
            out.append((ln, CODE_FG))
    return out


SLIDES = []
def slide(fn):
    SLIDES.append(fn)
    return fn


# -------- PART 1: HOOK ----------

@slide
def s01_title(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_rect(s, Inches(0.8), Inches(0.9), Inches(2.2), Emu(12700), CORAL)
    add_text(s, Inches(0.8), Inches(1.05), Inches(8), Inches(0.4),
             "A MASTERCLASS", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.7), Inches(12), Inches(2.2),
             "Vibecoding.", font=F_HEAD, size=120, color=WHITE, italic=True)
    add_text(s, Inches(0.8), Inches(4.15), Inches(11.5), Inches(0.6),
             "Direct, verify, ship — with Claude Code.",
             font=F_HEAD, size=28, color=CREAM)
    add_text(s, Inches(0.8), Inches(4.95), Inches(12), Inches(0.5),
             "> a four-hour masterclass on agentic engineering",
             font=F_CODE, size=14, color=CORAL)
    add_text(s, Inches(0.8), SH - Inches(1.3), Inches(6), Inches(0.3),
             "ELIAS JELINEK", font=F_BODY, size=10, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), SH - Inches(1.0), Inches(10), Inches(0.3),
             "Place Beyond Bytes  ·  Chair of Sustainability and Innovation in Digital Ecosystems",
             font=F_BODY, size=10, color=CREAM)
    add_text(s, Inches(0.8), SH - Inches(0.75), Inches(8), Inches(0.3),
             "University of Duisburg-Essen  ·  Summer 2026",
             font=F_BODY, size=10, color=CREAM)
    page_no(s, light=True)


@slide
def s02_agenda(s):
    page_chrome(s, label="WHAT THE NEXT HOUR LOOKS LIKE")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "An hour of theory and demos. Then three hours of doing.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Agenda.", font=F_HEAD, size=44, color=NAVY)

    rows = [
        ("01", "What's possible", "Six live demos — code, multi-agent, browser, ML, automation"),
        ("02", "The mindset shift", "From vibe-coding to agentic engineering"),
        ("03", "Coding workflows — the core", "Specs, plans, repo setup, tests, orchestrator, deploy"),
        ("04", "Beyond coding", "Daily automations, project management, Second Brain"),
        ("05", "AI engineering", "Using Claude Code to scaffold ML training, RAG, evals"),
        ("06", "The wider toolbox", "Cursor, Cline, Aider, Codex — when to use what"),
        ("07", "Your turn", "Three hours of hands-on, in pairs, in this repo"),
    ]
    top = Inches(2.4)
    rh = Inches(0.55)
    for i, (n, head, body) in enumerate(rows):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.45),
                 n, font=F_CODE, size=16, color=CORAL)
        add_text(s, Inches(1.9), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, Inches(6.5), y + Inches(0.03), Inches(6.5), Inches(0.4),
                 body, font=F_BODY, size=12, color=INK)


@slide
def s03_demo_pomodoro(s):
    page_chrome(s, label="DEMO 01  ·  HOOK")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "From one paragraph to a working app, in under five minutes.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Vibe-build an MVP.", font=F_HEAD, size=34, color=NAVY)

    code_block(s, Inches(0.8), Inches(2.05), Inches(5.4), Inches(2.4),
               [("> claude", CORAL),
                ("", CODE_FG),
                ("\"Build a Pomodoro timer.", CODE_FG),
                (" 25 min focus, 5 min rest.", CODE_FG),
                (" Stats persist. Editorial style.", CODE_FG),
                (" Cream + coral. No frameworks.\"", CODE_FG)],
               size=13)

    embed_screenshot(s, "01-pomodoro.png",
                     Inches(6.5), Inches(2.05), Inches(6.0), Inches(3.4),
                     caption="Final UI · localStorage persistence · zero dependencies")

    add_text(s, Inches(0.8), Inches(4.7), Inches(5.6), Inches(0.4),
             "ONE PROMPT", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), Inches(5.1), Inches(5.6), Inches(1.5),
             "No framework. No build step. Spec-tight prompt + plan mode + render = working app.",
             font=F_HEAD, size=14, color=INK, line_spacing=1.4)

    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "But this is the easy part. Now what about real software?",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s04_demo_spec_plan_impl(s):
    page_chrome(s, label="DEMO 02  ·  THE FULL CYCLE")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "How production-ish features actually move through Claude Code.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Spec → Plan → Implementation.",
             font=F_HEAD, size=30, color=NAVY)

    cols = [
        ("SPEC", "demos/02-…/spec.md",
         [("# Spec — CSV Export", CORAL),
          ("", CODE_FG),
          ("Owner: Elias", CODE_DIM),
          ("Status: approved", CODE_DIM),
          ("", CODE_FG),
          ("## Checkable criteria", CODE_GRN),
          ("1. export_to_csv(rows, out) ...", CODE_FG),
          ("2. Header row present.", CODE_FG),
          ("3. UTF-8, RFC 4180.", CODE_FG),
          ("4. Empty rows → header only.", CODE_FG),
          ("5. Refuses to overwrite.", CODE_FG),
          ("", CODE_FG),
          ("## Out of scope", CODE_GRN),
          ("- xlsx output", CODE_DIM),
          ("- multi-currency", CODE_DIM)]),
        ("PLAN", "demos/02-…/plan.md",
         [("# Plan — CSV Export", CORAL),
          ("", CODE_FG),
          ("→ parser.py: add export_to_csv()", CODE_FG),
          ("→ tests/test_export.py: 3 tests", CODE_FG),
          ("", CODE_FG),
          ("## Assumptions", CODE_GRN),
          ("- csv.DictWriter, comma delim", CODE_FG),
          ("- Path-wrap out_path", CODE_FG),
          ("", CODE_FG),
          ("## Done when", CODE_GRN),
          ("- 3 tests green", CODE_FG),
          ("- empty.csv has 1 line", CODE_FG)]),
        ("DIFF + TEST", "parser.py + pytest",
         [("+ CSV_COLUMNS = ('date',", CODE_GRN),
          ("    'shop', 'item',", CODE_GRN),
          ("    'price', 'currency')", CODE_GRN),
          ("", CODE_FG),
          ("+ def export_to_csv(rows, out):", CODE_GRN),
          ("+     if out.exists():", CODE_GRN),
          ("+         raise FileExistsError", CODE_GRN),
          ("", CODE_FG),
          ("test_round_trip       PASSED", CODE_GRN),
          ("test_empty_header     PASSED", CODE_GRN),
          ("test_refuses_over     PASSED", CODE_GRN),
          ("", CODE_FG),
          ("=== 3 passed in 0.04s ===", CODE_GRN)]),
    ]
    col_w = Inches(3.95)
    col_h = Inches(4.5)
    gap = Inches(0.1)
    top = Inches(1.9)
    for i, (lab, caption, lines) in enumerate(cols):
        x = Inches(0.8) + (col_w + gap) * i
        add_text(s, x, top, col_w, Inches(0.3), lab,
                 font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
        add_text(s, x, top + Inches(0.32), col_w, Inches(0.25), caption,
                 font=F_CODE, size=9, color=MUTED)
        code_block(s, x, top + Inches(0.6), col_w, col_h - Inches(0.6), lines, size=10)

    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Three artifacts. Each reviewable. Each persists after the code ships.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s05_demo_multi_agent(s):
    page_chrome(s, label="DEMO 03  ·  ORCHESTRATION")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "One conversation. Three parallel investigators. Synthesized in seconds.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Multi-agent in motion.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.05), Inches(11.7), Inches(4.4),
               colorize_terminal(DEMO3, max_lines=26), size=11)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Three parallel agents. One synthesis. You read it like a tech lead.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s06_demo_browser(s):
    page_chrome(s, label="DEMO 04  ·  BEYOND THE TERMINAL")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "Claude Code drives a real browser — extraction, automation, admin.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Browser-driving Claude.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.05), Inches(11.7), Inches(4.4),
               colorize_terminal(DEMO4, max_lines=27), size=11)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Same model, different surface. Code is just one of the surfaces.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s07_demo_ml(s):
    page_chrome(s, label="DEMO 05  ·  TRAINING A MODEL")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "20-newsgroups, four topics. Claude scaffolds the pipeline; you read the numbers.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Claude trains an ML model.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.05), Inches(11.7), Inches(4.4),
               colorize_terminal(ML_OUT, max_lines=22), size=12)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "89.5% accuracy across four topics. Real dataset. Real numbers.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s08_demo_second_brain(s):
    page_chrome(s, label="DEMO 06  ·  THE SECOND BRAIN")
    add_text(s, Inches(0.8), Inches(0.55), Inches(12), Inches(0.4),
             "Claude Code writes to your vault. Every session ends as a note.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.8),
             "Notes that write themselves.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.05), Inches(7.5), Inches(4.4),
               colorize_terminal(VAULT, max_lines=25), size=12)
    add_text(s, Inches(8.6), Inches(2.05), Inches(4.0), Inches(0.4),
             "HOW IT WORKS",
             font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(8.6), Inches(2.45), Inches(4.0), Inches(4),
             "A SessionEnd hook fires when you close Claude Code.\n\n"
             "The hook writes a markdown note to your Obsidian vault — "
             "what you worked on, decisions made, open questions.\n\n"
             "Tomorrow's session reads it back. Nothing gets lost.",
             font=F_HEAD, size=13, color=INK, line_spacing=1.5)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Your brain has limits. Your filesystem doesn't.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s09_the_thread(s):
    page_chrome(s, label="WHAT THESE DEMOS HAVE IN COMMON")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Six demos. One shape.", font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The thread.", font=F_HEAD, size=44, color=NAVY)
    items = [
        ("01", "You wrote the spec, not the code.",
         "The prompt was a tight description of what you wanted."),
        ("02", "Claude proposed a plan before acting.",
         "Even on small demos, there's a plan you could intercept."),
        ("03", "The output was reviewable.",
         "Test green, screenshot, diff, accuracy — evidence each time."),
        ("04", "You stayed the human in the loop.",
         "Claude did the typing. You did the judging."),
    ]
    top = Inches(2.5)
    rh = Inches(0.95)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.9), Inches(0.5),
                 n, font=F_CODE, size=24, color=CORAL)
        add_text(s, Inches(2.0), y + Inches(0.02), Inches(10.5), Inches(0.5),
                 head, font=F_HEAD, size=20, color=NAVY)
        add_text(s, Inches(2.0), y + Inches(0.5), Inches(10.5), Inches(0.4),
                 body, font=F_BODY, size=13, color=INK)
    add_text(s, Inches(0.8), Inches(6.5), Inches(12), Inches(0.4),
             "Now let's unpack how to actually run this discipline.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


@slide
def s10_transition(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_text(s, Inches(0.8), Inches(3.0), Inches(12), Inches(2),
             "Now let's unpack how\nthis actually works.",
             font=F_HEAD, size=56, color=WHITE, italic=True, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(5.5), Inches(12), Inches(0.5),
             "The mindset → the workflow → the wider toolbox.",
             font=F_HEAD, size=18, color=CREAM)
    dark_footer(s, label_left="")


# -------- PART 2: MINDSET ----------

@slide
def s11_mindset_divider(s):
    section_divider(s, label="PART 02",
                    title="Vibecoding →\nAgentic Engineering.",
                    sub="A mindset shift, not a tool swap.")


@slide
def s12_the_premise(s):
    page_chrome(s, label="THE PREMISE")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "What the marketing says.", font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The promise.", font=F_HEAD, size=44, color=NAVY)
    add_rect(s, Inches(0.8), Inches(2.8), Emu(38100), Inches(3.0), CORAL)
    add_text(s, Inches(1.3), Inches(2.8), Inches(11.5), Inches(0.6),
             "“Describe what you want in natural language —",
             font=F_HEAD, size=24, color=INK, italic=True)
    add_text(s, Inches(1.3), Inches(3.35), Inches(11.5), Inches(0.6),
             "the AI writes the code for you.”",
             font=F_HEAD, size=24, color=INK, italic=True)
    add_text(s, Inches(1.3), Inches(4.5), Inches(11.5), Inches(0.6),
             "— every AI coding demo on every conference stage, 2024-2026",
             font=F_BODY, size=13, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(6.2), Inches(12), Inches(0.5),
             "And to be fair — sometimes it really does work like that.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


@slide
def s13_the_reality(s):
    page_chrome(s, label="THE REALITY")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "What you ship if you stop there.", font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "And the catch.", font=F_HEAD, size=44, color=NAVY)
    items = [
        ("✗", "Hallucinated APIs", "calls a function that doesn't exist"),
        ("✗", "Silent scope creep", "asked for one feature, got four"),
        ("✗", "Plausible bugs", "looks right; fails on the second input"),
        ("✗", "False “done”", "tests not run, output not seen"),
        ("✗", "No paper trail", "no spec, no plan, can't reproduce decisions"),
    ]
    top = Inches(2.5)
    rh = Inches(0.65)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=CORAL, bold=True)
        add_text(s, Inches(1.4), y, Inches(5), Inches(0.5),
                 head, font=F_HEAD, size=19, color=NAVY)
        add_text(s, Inches(6.5), y + Inches(0.05), Inches(6.5), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "We need engineering discipline back. With the AI, not despite it.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


@slide
def s14_three_lies_intro(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_text(s, Inches(0.8), Inches(2.7), Inches(12), Inches(0.5),
             "THE FRAMEWORK", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(3.05), Inches(2), Inches(2.5),
             "03", font=F_HEAD, size=160, color=CORAL, italic=True)
    add_text(s, Inches(3.6), Inches(3.5), Inches(9), Inches(2),
             "Three lies AI coding\ntools tell us.",
             font=F_HEAD, size=46, color=WHITE, line_spacing=1.1)
    dark_footer(s, label_left="")


def _lie_slide(s, n, lie, rebuttal, discipline):
    page_chrome(s, label=f"THE THREE LIES  ·  {n} OF 3")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             f"LIE {n}", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(1.1), Inches(12), Inches(2),
             f"“{lie}”", font=F_HEAD, size=72, color=NAVY, italic=True)
    add_rect(s, Inches(0.8), Inches(3.4), Inches(0.5), Emu(19050), CORAL)
    add_text(s, Inches(1.5), Inches(3.3), Inches(10.5), Inches(2.5),
             rebuttal, font=F_HEAD, size=22, color=INK, line_spacing=1.35)
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.4),
             "DISCIPLINE", font=F_BODY, size=10, color=MUTED,
             bold=True, letter_spacing=300)
    add_text(s, Inches(0.8), Inches(6.35), Inches(12), Inches(0.5),
             discipline, font=F_HEAD, size=20, color=CORAL, italic=True)


@slide
def s15_lie1(s):
    _lie_slide(s, 1, "It works.",
               "It looks like it works. The imports look right, the signature looks right, the README looks right.\n\nBut did anyone run it?",
               "Verification before done.")


@slide
def s16_lie2(s):
    _lie_slide(s, 2, "I understand.",
               "It pattern-matched your keywords.\n\nIt may have grasped the surface. It rarely grasps the intent.",
               "Write a spec. Or make Claude write one — then review it.")


@slide
def s17_lie3(s):
    _lie_slide(s, 3, "I'm done.",
               "“Done” is a status, not a feeling. Done means the code is written, the tests pass, the output was seen — by you.",
               "Stop conditions. Show your work.")


@slide
def s18_rhythm(s):
    page_chrome(s, label="THE RHYTHM")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The five steps. In this order. Every time.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The rhythm.", font=F_HEAD, size=40, color=NAVY)
    steps = [
        ("01", "Spec", "What you want. Checkable success criteria."),
        ("02", "Plan", "Recipe between spec and code. Reviewable."),
        ("03", "Test", "At least one failing test before code."),
        ("04", "Implement", "The boring step."),
        ("05", "Verify", "Run it. See the output. Show evidence."),
    ]
    col_w = Inches(2.3)
    gap = Inches(0.1)
    top = Inches(2.6)
    x0 = Inches(0.8)
    for i, (n, head, body) in enumerate(steps):
        x = x0 + (col_w + gap) * i
        add_rect(s, x, top, col_w, Inches(3.4), WHITE)
        add_rect(s, x, top, Inches(0.16), Inches(3.4), CORAL)
        add_text(s, x + Inches(0.35), top + Inches(0.3), col_w, Inches(0.5),
                 n, font=F_CODE, size=20, color=CORAL)
        add_text(s, x + Inches(0.35), top + Inches(1.0), col_w - Inches(0.5), Inches(0.5),
                 head, font=F_HEAD, size=23, color=NAVY)
        add_text(s, x + Inches(0.35), top + Inches(1.7), col_w - Inches(0.5), Inches(1.6),
                 body, font=F_BODY, size=12, color=INK, line_spacing=1.4)
        if i < 4:
            add_text(s, x + col_w, top + Inches(1.5), gap, Inches(0.5),
                     "→", font=F_HEAD, size=18, color=CORAL, align="center")
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "Skip any one of these and you didn't really ship.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


# -------- PART 3: WORKFLOWS ----------

@slide
def s19_workflow_divider(s):
    section_divider(s, label="PART 03",
                    title="Coding workflows.",
                    sub="Where the actual discipline lives.")


@slide
def s20_what_is_spec(s):
    page_chrome(s, label="SPECIFICATIONS  ·  01 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "A spec is not a wish list. It's a contract you can check.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What is a spec?", font=F_HEAD, size=42, color=NAVY)
    top = Inches(2.6)
    h = Inches(3.7)
    add_rect(s, Inches(0.8), top, Inches(5.9), h, WHITE)
    add_rect(s, Inches(0.8), top, Inches(5.9), Inches(0.55), MUTED)
    add_text(s, Inches(1.1), top + Inches(0.13), Inches(5.5), Inches(0.4),
             "VAGUE INTENT", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    bad = ["“Make the dashboard faster.”",
           "“Improve the user experience.”",
           "“Handle errors properly.”",
           "“Make it work for our enterprise client.”"]
    for i, t in enumerate(bad):
        add_text(s, Inches(1.1), top + Inches(0.9) + Inches(0.65) * i,
                 Inches(5.5), Inches(0.5), t,
                 font=F_HEAD, size=16, color=MUTED, italic=True)
    rx = Inches(7.0)
    add_rect(s, rx, top, Inches(5.5), h, WHITE)
    add_rect(s, rx, top, Inches(5.5), Inches(0.55), CORAL)
    add_text(s, rx + Inches(0.3), top + Inches(0.13), Inches(5), Inches(0.4),
             "CHECKABLE SUCCESS CRITERIA", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    good = ["Dashboard renders < 2s at p95.",
            "All forms submit < 250ms.",
            "Invalid input → 400 + body.error.",
            "Multi-tenant: row isolation per tenant_id."]
    for i, t in enumerate(good):
        add_text(s, rx + Inches(0.3), top + Inches(0.9) + Inches(0.65) * i,
                 Inches(5), Inches(0.5), t,
                 font=F_HEAD, size=16, color=NAVY)
    add_text(s, Inches(0.8), Inches(6.6), Inches(12), Inches(0.4),
             "If you can't tell whether you're done, you don't have a spec.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s21_anatomy_spec(s):
    page_chrome(s, label="SPECIFICATIONS  ·  02 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Five elements. Always.", font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Anatomy of a good spec.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("01", "Why", "The motivation. Who asked, what problem it solves."),
        ("02", "What", "The thing being built — one paragraph, no jargon."),
        ("03", "Checkable success criteria", "Numbered list. Each item testable. No interpretation."),
        ("04", "What it must NOT do", "Failure modes, scope boundaries, things to refuse."),
        ("05", "Out of scope", "Explicit exclusions. Prevents scope creep mid-build."),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.4),
                 n, font=F_CODE, size=18, color=CORAL)
        add_text(s, Inches(1.9), y - Inches(0.02), Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=19, color=NAVY)
        add_text(s, Inches(6.6), y + Inches(0.03), Inches(6.4), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK, line_spacing=1.4)
    add_text(s, Inches(0.8), Inches(6.5), Inches(12), Inches(0.4),
             "See demos/02-spec-plan-impl/spec.md for a real example.",
             font=F_CODE, size=12, color=MUTED)


@slide
def s22_capture_specs(s):
    page_chrome(s, label="SPECIFICATIONS  ·  03 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Clients give you wishes. You convert wishes into checkable criteria.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Capturing specs from clients.", font=F_HEAD, size=30, color=NAVY)
    questions = [
        ("›", "“What happens when this works?”", "Forces them to describe an outcome, not a feature."),
        ("›", "“What does failure look like?”", "Surfaces the unspoken edge cases."),
        ("›", "“Who else needs to sign off?”", "Reveals the actual decision tree, not the org chart."),
        ("›", "“What's explicitly OUT of scope?”", "The hardest question. The most valuable answer."),
        ("›", "“Can I read the spec back to you?”", "The demo-it-back loop. Catches misalignment before code."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, q, body) in enumerate(questions):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=CORAL)
        add_text(s, Inches(1.4), y, Inches(6.5), Inches(0.45),
                 q, font=F_HEAD, size=18, color=NAVY, italic=True)
        add_text(s, Inches(8.1), y + Inches(0.05), Inches(4.9), Inches(0.5),
                 body, font=F_BODY, size=12, color=INK)


@slide
def s23_specs_persistent(s):
    page_chrome(s, label="SPECIFICATIONS  ·  04 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Code rots fastest. Specs rot slowest. Treat them accordingly.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Specs outlive the code.", font=F_HEAD, size=34, color=NAVY)
    add_rect(s, Inches(0.8), Inches(2.5), Emu(38100), Inches(3.5), CORAL)
    add_text(s, Inches(1.2), Inches(2.5), Inches(6), Inches(0.6),
             "Code is an implementation.", font=F_HEAD, size=24, color=NAVY)
    add_text(s, Inches(1.2), Inches(3.1), Inches(6), Inches(0.6),
             "It changes weekly.", font=F_HEAD, size=24, color=NAVY, italic=True)
    add_text(s, Inches(1.2), Inches(4.4), Inches(6), Inches(0.6),
             "The spec is the contract.", font=F_HEAD, size=24, color=CORAL)
    add_text(s, Inches(1.2), Inches(5.0), Inches(6), Inches(0.6),
             "It changes when the deal changes.", font=F_HEAD, size=24, color=CORAL, italic=True)
    add_text(s, Inches(8.0), Inches(2.5), Inches(5), Inches(0.4),
             "WHY THIS MATTERS", font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    add_text(s, Inches(8.0), Inches(2.9), Inches(5), Inches(3.5),
             "When a regression hits production six months later, "
             "you don't ask “what did the code do.” You ask “what was "
             "this supposed to do.”\n\n"
             "The spec answers that. The code does not.\n\n"
             "Store specs in version control. Reference them in PRs. They are the contract.",
             font=F_BODY, size=13, color=INK, line_spacing=1.45)


@slide
def s24_what_is_plan(s):
    page_chrome(s, label="PLANS  ·  01 / 03")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The recipe between the spec and the code.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What is a plan?", font=F_HEAD, size=42, color=NAVY)
    boxes = [("SPEC", "What"), ("PLAN", "How"), ("CODE", "Done")]
    bx = Inches(1.5)
    bw = Inches(3.2)
    by = Inches(3.0)
    gap = Inches(0.6)
    for i, (lab, sub) in enumerate(boxes):
        x = bx + (bw + gap) * i
        col = CORAL if lab == "PLAN" else NAVY
        add_rect(s, x, by, bw, Inches(2.0), WHITE)
        add_rect(s, x, by, bw, Inches(0.55), col)
        add_text(s, x + Inches(0.3), by + Inches(0.12), bw, Inches(0.4),
                 lab, font=F_BODY, size=12, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.3), by + Inches(0.8), bw, Inches(0.6),
                 sub, font=F_HEAD, size=28, color=col, italic=True)
        if i < 2:
            add_text(s, x + bw, by + Inches(0.6), gap, Inches(0.6),
                     "→", font=F_HEAD, size=24, color=MUTED, align="center")
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.4),
             "Without a plan, the spec stays an idea and the code becomes a guess.",
             font=F_HEAD, size=14, color=INK, italic=True)
    add_text(s, Inches(0.8), Inches(6.5), Inches(12), Inches(0.4),
             "A good plan is shorter than you expect.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s25_anatomy_plan(s):
    page_chrome(s, label="PLANS  ·  02 / 03")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Five questions on every plan Claude proposes. Always.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Anatomy of a good plan.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("✓", "States its assumptions out loud", "“I'm assuming X.” Not silent guessing."),
        ("✓", "Names the exact files it will touch", "parser.py:42, not “the parser”."),
        ("✓", "Proposes at least one test", "“Here's the test that proves this works.”"),
        ("✓", "Stays scoped to what you asked", "Count the verbs. Cut bonus features."),
        ("✓", "Doesn't claim what it can't know", "“Following the existing convention” — which?"),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.6), Inches(0.5), mark,
                 font=F_HEAD, size=22, color=CORAL, bold=True)
        add_text(s, Inches(1.5), y, Inches(6.5), Inches(0.45),
                 head, font=F_HEAD, size=19, color=NAVY)
        add_text(s, Inches(8.2), y + Inches(0.05), Inches(4.8), Inches(0.5),
                 body, font=F_CODE, size=11.5, color=MUTED, italic=True)


@slide
def s26_plan_mode(s):
    page_chrome(s, label="PLANS  ·  03 / 03")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Plan mode = read-only exploration before any approval-gated change.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Plan mode in Claude Code.", font=F_HEAD, size=32, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(3.7),
               [("> claude /plan", CORAL),
                ("", CODE_FG),
                ("Task: refactor the auth middleware.", CODE_FG),
                ("", CODE_FG),
                ("[exploring codebase ...]", CODE_DIM),
                ("[reading 14 files in ./src/auth/]", CODE_DIM),
                ("[reading 3 test files]", CODE_DIM),
                ("", CODE_FG),
                ("Plan", CODE_GRN),
                ("1. Extract token validation into auth/tokens.py", CODE_FG),
                ("2. Replace direct DB calls with the new repo class", CODE_FG),
                ("3. Add 5 unit tests in tests/auth/test_tokens.py", CODE_FG),
                ("", CODE_FG),
                ("Assumptions", CODE_YEL),
                ("- Keeping the existing JWT secret env var", CODE_FG),
                ("- NOT changing the public API surface", CODE_FG),
                ("", CODE_FG),
                ("Approve? (y/n/edit)", CODE_GRN)],
               size=12)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "Nothing changes on disk until you approve. That's the point.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s27_repo_setup(s):
    page_chrome(s, label="REPO STRUCTURE")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "A layout Claude Code can navigate without guessing.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Repo setup for agent-friendly work.", font=F_HEAD, size=28, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.0), Inches(4.1),
               [("project/", CODE_FG),
                ("├── README.md         ← what + how to run", CODE_FG),
                ("├── CLAUDE.md         ← conventions, ≤ 200 lines", CORAL),
                ("├── specs/            ← versioned specs", CODE_FG),
                ("│   └── 0001-csv-export.md", CODE_DIM),
                ("├── src/", CODE_FG),
                ("│   └── parser.py", CODE_DIM),
                ("├── tests/", CODE_FG),
                ("│   └── test_parser.py", CODE_DIM),
                ("├── .claude/", CODE_FG),
                ("│   ├── hooks/        ← deterministic automation", CORAL),
                ("│   │   └── pre-commit.sh", CODE_DIM),
                ("│   └── skills/       ← capability uplift", CORAL),
                ("│       └── csv-export.md", CODE_DIM),
                ("└── .github/", CODE_FG),
                ("    └── workflows/    ← CI as a verify gate", CODE_FG)],
               size=12)
    add_text(s, Inches(8.2), Inches(2.4), Inches(4.5), Inches(0.4),
             "PRINCIPLES", font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    bullets = ["One CLAUDE.md per repo, root level",
               "Specs as first-class artifacts",
               "Hooks for the things you forget",
               "Skills for the things you repeat",
               "CI = automated verify gate",
               "No deep nesting"]
    for i, b in enumerate(bullets):
        add_text(s, Inches(8.2), Inches(2.85) + Inches(0.5) * i,
                 Inches(4.5), Inches(0.4),
                 "·  " + b, font=F_HEAD, size=14, color=INK)


@slide
def s28_claude_md(s):
    page_chrome(s, label="THE PERSISTENCE LAYER  ·  01 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Read at session start. Sticks across every prompt. Keep it short.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "CLAUDE.md — project DNA.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.0), Inches(4.1),
               [("# Project conventions", CORAL),
                ("", CODE_FG),
                ("## The rhythm", CODE_GRN),
                ("SPEC → PLAN → TEST → IMPL → VERIFY", CODE_FG),
                ("", CODE_FG),
                ("## When you're working here", CODE_GRN),
                ("- Use plan mode for >1 file changes", CODE_FG),
                ("- Tests before implementation", CODE_FG),
                ("- Never claim done without output", CODE_FG),
                ("- Cite file:line for every reference", CODE_FG),
                ("- No real client data, ever", CODE_FG),
                ("", CODE_FG),
                ("## What to avoid", CODE_GRN),
                ("- Long try/except that swallow errors", CODE_FG),
                ("- Premature abstraction (< 3 callers)", CODE_FG),
                ("- Comments that say what code does", CODE_FG)],
               size=11.5)
    add_text(s, Inches(8.2), Inches(2.4), Inches(4.5), Inches(0.4),
             "RULES", font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    rules = ["≤ 200 lines. Hard cap.",
             "Conventions, not code.",
             "“Why” over “what”.",
             "Update when the project drifts.",
             "Run `claude /init` to bootstrap.",
             "It's advisory — ~80% compliance."]
    for i, b in enumerate(rules):
        add_text(s, Inches(8.2), Inches(2.85) + Inches(0.5) * i,
                 Inches(4.5), Inches(0.4),
                 "·  " + b, font=F_HEAD, size=14, color=INK)


@slide
def s29_hooks(s):
    page_chrome(s, label="THE PERSISTENCE LAYER  ·  02 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "When 80% isn't good enough. Deterministic, every time.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Hooks — automate the must-haves.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.0), Inches(4.1),
               [("# .claude/settings.json", CODE_DIM),
                ("{", CODE_FG),
                ("  \"hooks\": {", CODE_FG),
                ("    \"PreToolUse\": [{", CODE_FG),
                ("      \"matcher\": \"Edit|Write\",", CODE_FG),
                ("      \"command\": \"ruff format --check\"", CORAL),
                ("    }],", CODE_FG),
                ("    \"PostToolUse\": [{", CODE_FG),
                ("      \"matcher\": \"Edit\",", CODE_FG),
                ("      \"command\": \"pytest -q tests/\"", CORAL),
                ("    }],", CODE_FG),
                ("    \"SessionEnd\": [{", CODE_FG),
                ("      \"command\": \"~/.claude/session-note.sh\"", CORAL),
                ("    }]", CODE_FG),
                ("  }", CODE_FG),
                ("}", CODE_FG)],
               size=12)
    add_text(s, Inches(8.2), Inches(2.4), Inches(4.5), Inches(0.4),
             "USE FOR", font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    rows = ["Linting and formatting",
            "Security checks before commit",
            "Auto-tests on file changes",
            "Session notes to your vault",
            "Logging, telemetry",
            "Refusing forbidden patterns"]
    for i, t in enumerate(rows):
        add_text(s, Inches(8.2), Inches(2.85) + Inches(0.5) * i,
                 Inches(4.5), Inches(0.4),
                 "·  " + t, font=F_HEAD, size=14, color=INK)


@slide
def s30_skills(s):
    page_chrome(s, label="THE PERSISTENCE LAYER  ·  03 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Two kinds: give Claude new abilities, or encode your taste.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Skills — capabilities + preferences.", font=F_HEAD, size=30, color=NAVY)
    top = Inches(2.5)
    h = Inches(3.8)
    add_rect(s, Inches(0.8), top, Inches(5.9), h, WHITE)
    add_rect(s, Inches(0.8), top, Inches(5.9), Inches(0.55), NAVY)
    add_text(s, Inches(1.1), top + Inches(0.13), Inches(5.5), Inches(0.4),
             "CAPABILITY UPLIFT", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, Inches(1.1), top + Inches(0.95), Inches(5.5), Inches(0.6),
             "Give Claude a new ability.", font=F_HEAD, size=20, color=NAVY)
    examples_a = ["pdf — read and edit PDF files",
                  "browser — open pages, fill forms",
                  "playwright — generate E2E tests",
                  "fastapi-backend-design",
                  "database-design",
                  "ml-training-pipelines"]
    for i, t in enumerate(examples_a):
        add_text(s, Inches(1.1), top + Inches(1.75) + Inches(0.35) * i,
                 Inches(5.5), Inches(0.3),
                 "·  " + t, font=F_CODE, size=12, color=INK)
    rx = Inches(7.0)
    add_rect(s, rx, top, Inches(5.5), h, WHITE)
    add_rect(s, rx, top, Inches(5.5), Inches(0.55), CORAL)
    add_text(s, rx + Inches(0.3), top + Inches(0.13), Inches(5), Inches(0.4),
             "ENCODED PREFERENCE", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, rx + Inches(0.3), top + Inches(0.95), Inches(5), Inches(0.6),
             "Guide existing capabilities.", font=F_HEAD, size=20, color=NAVY)
    examples_b = ["german-client-communication",
                  "gdpr-dsgvo-compliance",
                  "meeting-to-actions",
                  "writing-plans (this discipline!)",
                  "polished-ui-design",
                  "verification-before-completion"]
    for i, t in enumerate(examples_b):
        add_text(s, rx + Inches(0.3), top + Inches(1.75) + Inches(0.35) * i,
                 Inches(5), Inches(0.3),
                 "·  " + t, font=F_CODE, size=12, color=INK)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Skills are markdown. MCP is JSON-RPC. Skills know things; MCP does things.",
             font=F_HEAD, size=13, color=CORAL, italic=True)


@slide
def s31_mcp(s):
    page_chrome(s, label="THE PERSISTENCE LAYER  ·  04 / 04")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Claude can now act outside the terminal — through any MCP-speaking tool.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "MCP — the action layer.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.0), Inches(4.1),
               [("$ claude mcp add notion --token=...", CORAL),
                ("$ claude mcp add slack --workspace=...", CORAL),
                ("$ claude mcp add postgres --conn=...", CORAL),
                ("$ claude mcp add chrome", CORAL),
                ("", CODE_FG),
                ("$ claude", CODE_FG),
                ("> \"Read today's standup notes from Slack,", CODE_FG),
                ("   create a Notion page summarising blockers,", CODE_FG),
                ("   then open chrome to file the bug.\"", CODE_FG),
                ("", CODE_FG),
                ("[claude] mcp__slack__read_channel ...", CODE_DIM),
                ("[claude] mcp__notion__create-pages ...", CODE_DIM),
                ("[claude] mcp__chrome__navigate ...", CODE_DIM),
                ("[claude] mcp__chrome__form_input ...", CODE_DIM)],
               size=11.5)
    add_text(s, Inches(8.2), Inches(2.4), Inches(4.5), Inches(0.4),
             "POPULAR MCP SERVERS", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    rows = ["Notion (docs, databases)",
            "Slack (channels, threads)",
            "Linear (issues, projects)",
            "Gmail / Google Calendar",
            "Chrome (browser automation)",
            "GitHub (via gh CLI)",
            "Postgres / SQLite / DuckDB",
            "Filesystem with permissions"]
    for i, t in enumerate(rows):
        add_text(s, Inches(8.2), Inches(2.85) + Inches(0.45) * i,
                 Inches(4.5), Inches(0.4),
                 "·  " + t, font=F_HEAD, size=13, color=INK)


@slide
def s32_unit_tests(s):
    page_chrome(s, label="TESTING  ·  01 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Tests aren't safety nets. They're the spec, executable.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Unit tests — what they actually are.", font=F_HEAD, size=28, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.5), Inches(4.1),
               [("# tests/test_export.py", CODE_DIM),
                ("from parser import export_to_csv, parse_receipts", CODE_FG),
                ("", CODE_FG),
                ("def test_round_trip(tmp_path):", CODE_FG),
                ("    rows = parse_receipts(SAMPLE)", CODE_FG),
                ("    out = tmp_path / \"out.csv\"", CODE_FG),
                ("    export_to_csv(rows, out)", CODE_FG),
                ("    assert out.read_text().count(\"\\n\") == 14", CODE_FG),
                ("", CODE_FG),
                ("def test_empty_writes_header_only(tmp_path):", CODE_FG),
                ("    out = tmp_path / \"empty.csv\"", CODE_FG),
                ("    export_to_csv([], out)", CODE_FG),
                ("    assert out.read_text().splitlines() == [", CODE_FG),
                ("        \"date,shop,item,price,currency\"]", CODE_FG),
                ("", CODE_FG),
                ("def test_refuses_overwrite(tmp_path):", CODE_FG),
                ("    out = tmp_path / \"x.csv\"; out.touch()", CODE_FG),
                ("    with pytest.raises(FileExistsError):", CODE_FG),
                ("        export_to_csv([], out)", CODE_FG)],
               size=11)
    add_text(s, Inches(8.6), Inches(2.4), Inches(4.2), Inches(0.4),
             "GOOD UNIT TESTS", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    pts = ["Test one behavior",
           "Read like a spec",
           "Fail loudly with a clear message",
           "Don't share state",
           "Run in milliseconds",
           "Cover happy path AND one failure"]
    for i, t in enumerate(pts):
        add_text(s, Inches(8.6), Inches(2.85) + Inches(0.5) * i,
                 Inches(4.2), Inches(0.4),
                 "·  " + t, font=F_HEAD, size=13, color=INK)


@slide
def s33_tdd(s):
    page_chrome(s, label="TESTING  ·  02 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Standard TDD. Just with Claude as the typist.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Red, green, refactor.", font=F_HEAD, size=40, color=NAVY)
    cells = [("RED", "Failing tests first.", CODE_RED),
             ("GREEN", "Simplest code that passes.", CODE_GRN),
             ("REFACTOR", "Only if simpler. Else stop.", CORAL)]
    top = Inches(2.7)
    col_w = Inches(3.95)
    gap = Inches(0.1)
    for i, (label, body, col) in enumerate(cells):
        x = Inches(0.8) + (col_w + gap) * i
        add_rect(s, x, top, col_w, Inches(2.6), WHITE)
        add_rect(s, x, top, col_w, Inches(0.55), col)
        add_text(s, x + Inches(0.3), top + Inches(0.13), col_w, Inches(0.4),
                 label, font=F_BODY, size=12, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.3), top + Inches(0.85), col_w - Inches(0.6), Inches(1.7),
                 body, font=F_HEAD, size=22, color=NAVY, line_spacing=1.25)
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.4),
             "Claude *will* try to write the function first. Correct it. Always.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


@slide
def s34_playwright(s):
    page_chrome(s, label="E2E TESTING")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Web UI? Then Playwright tests, autogenerated from the spec.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Playwright + Claude Code.", font=F_HEAD, size=30, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(4.0),
               colorize_terminal(PLAYWRIGHT, max_lines=22), size=10.5)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Generated from the spec for the Pomodoro app. 90 seconds.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s35_verify_properly(s):
    page_chrome(s, label="VERIFICATION")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Green tests are necessary. Not sufficient.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Verify properly.", font=F_HEAD, size=40, color=NAVY)
    items = [
        ("01", "Run the feature end-to-end", "Not the test. The actual feature, as a user would."),
        ("02", "Inspect the artifact", "Open the CSV. Read the rendered page. Curl the endpoint."),
        ("03", "Try one adversarial input", "Empty list. Special chars. Concurrency. The thing that scared you."),
        ("04", "Compare to the spec", "Each checkable criterion: tick or not?"),
        ("05", "Show evidence", "Paste output, attach screenshot, save the log. Make it visible."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.4),
                 n, font=F_CODE, size=18, color=CORAL)
        add_text(s, Inches(1.9), y - Inches(0.02), Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.6), y + Inches(0.03), Inches(6.4), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s36_iteration(s):
    page_chrome(s, label="ITERATION CYCLES")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Feature by feature. Evidence each loop. No skipping.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Iteration cycles.", font=F_HEAD, size=40, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.5), Inches(11.7), Inches(3.9),
               [("loop:", CODE_GRN),
                ("    1. pick the next spec criterion", CODE_FG),
                ("    2. /plan — propose, review, approve", CODE_FG),
                ("    3. write failing test", CODE_FG),
                ("    4. implement", CODE_FG),
                ("    5. run test → green", CODE_FG),
                ("    6. run feature end-to-end → works", CODE_FG),
                ("    7. paste evidence", CODE_FG),
                ("    8. check against spec — drift? regenerate plan", CODE_YEL),
                ("    9. commit with spec reference in message", CODE_FG),
                ("   10. ↺", CODE_GRN),
                ("", CODE_FG),
                ("# do not move on while step 6 or 7 is incomplete.", CODE_RED)],
               size=14)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Small loops. Small reviews. Small risks. The compounding wins.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s37_spec_drift(s):
    page_chrome(s, label="SPEC DRIFT  ·  01 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The silent project killer in agentic workflows.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What is spec drift?", font=F_HEAD, size=40, color=NAVY)
    causes = [
        ("·", "Plan grows beyond the spec — Claude offers a “bonus” feature, you accept."),
        ("·", "Spec ambiguity resolved in conversation — but not written back."),
        ("·", "Tests cover the new shape, not the original criteria — green still ships drift."),
        ("·", "Stakeholder asks for “one tweak” mid-build — not added to the spec."),
        ("·", "Subagent decides on its own what done means — you don't notice."),
    ]
    top = Inches(2.6)
    rh = Inches(0.65)
    for i, (m, t) in enumerate(causes):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 m, font=F_HEAD, size=20, color=CORAL)
        add_text(s, Inches(1.3), y, Inches(11.5), Inches(0.5),
                 t, font=F_HEAD, size=17, color=NAVY)
    add_text(s, Inches(0.8), Inches(6.4), Inches(12), Inches(0.4),
             "By month two, no one can tell you what the system is supposed to do.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s38_prevent_drift(s):
    page_chrome(s, label="SPEC DRIFT  ·  02 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The spec stays canonical. Plans regenerate against it.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Preventing drift.", font=F_HEAD, size=40, color=NAVY)
    items = [
        ("01", "Spec is in version control", "Reviewable like code. Every change has a PR."),
        ("02", "Plans checked against the spec", "Before approving a plan, ask: does it stay inside?"),
        ("03", "Tests reference spec line numbers", "test docstring: “spec.md §2.3”. Drift visible in CI."),
        ("04", "Mid-build asks update the spec first", "If the spec doesn't change, the feature doesn't."),
        ("05", "Subagents inherit the spec, not the chat", "Pass spec as a file reference, not chat context."),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.4),
                 n, font=F_CODE, size=18, color=CORAL)
        add_text(s, Inches(1.9), y - Inches(0.02), Inches(5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(7.1), y + Inches(0.03), Inches(5.9), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s39_orchestrator(s):
    page_chrome(s, label="MULTI-AGENT  ·  01 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "One team lead. N subagents per feature. Verified handoffs.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The orchestrator pattern.", font=F_HEAD, size=32, color=NAVY)
    cx = Inches(6.7)
    add_rect(s, cx - Inches(1.8), Inches(2.5), Inches(3.6), Inches(0.9), NAVY)
    add_text(s, cx - Inches(1.8), Inches(2.65), Inches(3.6), Inches(0.6),
             "ORCHESTRATOR", font=F_HEAD, size=18, color=WHITE,
             align="center", italic=True)
    add_text(s, cx - Inches(1.8), Inches(3.55), Inches(3.6), Inches(0.4),
             "holds the spec  ·  routes work  ·  verifies",
             font=F_BODY, size=10, color=MUTED, align="center",
             italic=True, letter_spacing=120)
    pos_x = [Inches(1.4), Inches(5.6), Inches(9.8)]
    labels = [("FEATURE A", "spec § 2.1\nsubagent runs\nin own context"),
              ("FEATURE B", "spec § 2.2\nparallel,\nverified handoff"),
              ("FEATURE C", "spec § 2.3\nreports back\nwith evidence")]
    for x, (lab, body) in zip(pos_x, labels):
        add_rect(s, x + Inches(1.1), Inches(4.2), Emu(9525), Inches(0.8), CORAL)
        add_rect(s, x, Inches(5.0), Inches(2.3), Inches(1.7), WHITE)
        add_rect(s, x, Inches(5.0), Inches(2.3), Inches(0.4), CORAL)
        add_text(s, x + Inches(0.15), Inches(5.06), Inches(2), Inches(0.3),
                 lab, font=F_CODE, size=11, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.15), Inches(5.55), Inches(2), Inches(1.1),
                 body, font=F_HEAD, size=13, color=NAVY, line_spacing=1.3)


@slide
def s40_orch_vs_conductor(s):
    page_chrome(s, label="MULTI-AGENT  ·  02 / 02")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Two patterns. Pick by the shape of the work.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Orchestrator vs Conductor.", font=F_HEAD, size=30, color=NAVY)
    top = Inches(2.6)
    h = Inches(3.7)
    add_rect(s, Inches(0.8), top, Inches(5.9), h, WHITE)
    add_rect(s, Inches(0.8), top, Inches(5.9), Inches(0.55), NAVY)
    add_text(s, Inches(1.1), top + Inches(0.13), Inches(5.5), Inches(0.4),
             "ORCHESTRATOR", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, Inches(1.1), top + Inches(0.85), Inches(5.5), Inches(0.5),
             "One ensemble. One context.", font=F_HEAD, size=20, color=NAVY)
    pts_a = ["One agent runs the show",
             "Subagents return summaries",
             "Best for: research, refactor, planning",
             "Cheap and predictable",
             "Limit: serial bottlenecks"]
    for i, t in enumerate(pts_a):
        add_text(s, Inches(1.1), top + Inches(1.6) + Inches(0.4) * i,
                 Inches(5.5), Inches(0.35),
                 "·  " + t, font=F_HEAD, size=14, color=INK)
    rx = Inches(7.0)
    add_rect(s, rx, top, Inches(5.5), h, WHITE)
    add_rect(s, rx, top, Inches(5.5), Inches(0.55), CORAL)
    add_text(s, rx + Inches(0.3), top + Inches(0.13), Inches(5), Inches(0.4),
             "CONDUCTOR", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    add_text(s, rx + Inches(0.3), top + Inches(0.85), Inches(5), Inches(0.5),
             "Many agents. Bounded subtasks.", font=F_HEAD, size=20, color=NAVY)
    pts_b = ["Each agent owns a feature end-to-end",
             "Message bus / shared task list",
             "Best for: parallel features, async work",
             "More expensive, more coordination",
             "Limit: handoffs are where bugs live"]
    for i, t in enumerate(pts_b):
        add_text(s, rx + Inches(0.3), top + Inches(1.6) + Inches(0.4) * i,
                 Inches(5), Inches(0.35),
                 "·  " + t, font=F_HEAD, size=14, color=INK)


@slide
def s41_deployment(s):
    page_chrome(s, label="DEPLOYMENT")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The verify gate has to keep working when you're not looking.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Deployment.", font=F_HEAD, size=44, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.0), Inches(4.1),
               [("# .github/workflows/ci.yml", CODE_DIM),
                ("name: verify-before-ship", CODE_FG),
                ("on: [push, pull_request]", CODE_FG),
                ("", CODE_FG),
                ("jobs:", CODE_FG),
                ("  test:", CODE_FG),
                ("    runs-on: ubuntu-latest", CODE_FG),
                ("    steps:", CODE_FG),
                ("      - uses: actions/checkout@v4", CODE_FG),
                ("      - run: pip install -e .[test]", CODE_FG),
                ("      - run: pytest -q --cov", CODE_GRN),
                ("      - run: ruff check .", CODE_GRN),
                ("      - run: playwright test", CODE_GRN),
                ("      - run: ./scripts/smoke.sh staging", CORAL),
                ("", CODE_FG),
                ("# main is locked. PRs only.", CODE_DIM),
                ("# smoke.sh hits a real URL on staging.", CODE_DIM)],
               size=11.5)
    add_text(s, Inches(8.2), Inches(2.4), Inches(4.5), Inches(0.4),
             "GATES", font=F_BODY, size=10, color=CORAL, bold=True, letter_spacing=300)
    gates = ["Tests pass",
             "Linter clean",
             "E2E green",
             "Smoke test on staging",
             "Spec criteria checked off",
             "Manual approval for main",
             "Auto-rollback on health-fail"]
    for i, t in enumerate(gates):
        add_text(s, Inches(8.2), Inches(2.85) + Inches(0.45) * i,
                 Inches(4.5), Inches(0.4),
                 "·  " + t, font=F_HEAD, size=13, color=INK)


@slide
def s42_production_checklist(s):
    page_chrome(s, label="PRE-SHIP")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Eight items. Walk through them every time. No exceptions.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Production checklist.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("☐", "Spec criteria each ticked off"),
        ("☐", "Tests green locally AND in CI"),
        ("☐", "Feature exercised end-to-end (not just unit-tested)"),
        ("☐", "One adversarial input tried, behaved as expected"),
        ("☐", "Smoke test on staging green"),
        ("☐", "Rollback path verified (one command)"),
        ("☐", "Observability in place — logs, error alerts"),
        ("☐", "PR description references spec, plan, evidence"),
    ]
    top = Inches(2.5)
    rh = Inches(0.55)
    for i, (mark, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=CORAL)
        add_text(s, Inches(1.5), y, Inches(11.5), Inches(0.5),
                 body, font=F_HEAD, size=17, color=NAVY)


# -------- PART 4: BEYOND CODING ----------

@slide
def s43_beyond_divider(s):
    section_divider(s, label="PART 04",
                    title="Beyond coding.",
                    sub="Claude Code is an agent harness. Code is just one surface.")


@slide
def s44_harness_frame(s):
    page_chrome(s, label="REFRAMING THE TOOL")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "It edits files. Also reads emails, opens browsers, writes notes, runs cron.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Claude Code is not a code editor.", font=F_HEAD, size=28, color=NAVY)
    add_rect(s, Inches(5.0), Inches(3.3), Inches(3.3), Inches(1.5), NAVY)
    add_text(s, Inches(5.0), Inches(3.55), Inches(3.3), Inches(0.6),
             "CLAUDE CODE", font=F_HEAD, size=22, color=WHITE,
             align="center", italic=True)
    add_text(s, Inches(5.0), Inches(4.15), Inches(3.3), Inches(0.4),
             "an agent harness", font=F_BODY, size=10,
             color=DIM_LIGHT, align="center", letter_spacing=200)
    surfaces = [
        (Inches(0.8), Inches(2.7), "CODE", "src/, tests/, deploy"),
        (Inches(9.2), Inches(2.7), "BROWSER", "Chrome MCP, scrapes, forms"),
        (Inches(0.8), Inches(5.0), "FILES", "Obsidian, PDFs, spreadsheets"),
        (Inches(9.2), Inches(5.0), "APIS", "Notion, Slack, Linear, Gmail"),
    ]
    for x, y, lab, body in surfaces:
        add_rect(s, x, y, Inches(3.2), Inches(1.0), WHITE)
        add_rect(s, x, y, Inches(3.2), Inches(0.35), CORAL)
        add_text(s, x + Inches(0.3), y + Inches(0.05), Inches(3), Inches(0.3),
                 lab, font=F_BODY, size=11, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.3), y + Inches(0.45), Inches(3), Inches(0.55),
                 body, font=F_HEAD, size=14, color=NAVY)


@slide
def s45_pm(s):
    page_chrome(s, label="BEYOND  ·  PROJECT MANAGEMENT")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The PM work nobody actually wants to do. Delegate it.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Claude as co-PM.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("›", "Sprint reviews", "Read the PRs, write demo notes, draft retro."),
        ("›", "Status writeups", "Daily standup digest from Slack threads."),
        ("›", "Blocker triage", "Scan tickets, group by theme, propose owners."),
        ("›", "Risk surfacing", "Compare burndown to scope. Flag silently dropped items."),
        ("›", "Decision logs", "Every accepted plan auto-logged with context."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.5),
                 mark, font=F_HEAD, size=22, color=CORAL)
        add_text(s, Inches(1.4), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.2), y + Inches(0.05), Inches(6.8), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s46_automations(s):
    page_chrome(s, label="BEYOND  ·  AUTOMATIONS")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Anything you do twice a week is a candidate.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Daily automations.", font=F_HEAD, size=36, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(4.0),
               colorize_terminal(CRON, max_lines=24), size=11.5)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Cron + Claude + a few scripts. Your inbox, triaged. Every morning.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s47_browser_automation(s):
    page_chrome(s, label="BEYOND  ·  BROWSER")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "The web is a UI. UIs are scriptable. So are people, occasionally.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Browser automation.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("›", "Data extraction", "Scrape competitor pricing weekly. Slack a diff."),
        ("›", "Form filling", "Submit timesheets. Pull data from project tools."),
        ("›", "QA replay", "Walk through critical flows. Screenshot results."),
        ("›", "Admin work", "Onboarding portals, expense filings, account cleanup."),
        ("›", "Research", "Open 20 tabs, summarize each, output markdown brief."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.5),
                 mark, font=F_HEAD, size=22, color=CORAL)
        add_text(s, Inches(1.4), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.2), y + Inches(0.05), Inches(6.8), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s48_email(s):
    page_chrome(s, label="BEYOND  ·  EMAIL + CALENDAR")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Drafts, summaries, triage. You stay the final say.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Email and calendar.", font=F_HEAD, size=36, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(3.8),
               [("> claude", CORAL),
                ("\"Summarise unread emails since Friday.", CODE_FG),
                ("Group by sender. Flag what needs reply today.", CODE_FG),
                ("Draft replies for me to review.\"", CODE_FG),
                ("", CODE_FG),
                ("[claude] mcp__gmail__list_messages ...", CODE_DIM),
                ("[claude] mcp__gmail__read_message ... × 47", CODE_DIM),
                ("", CODE_FG),
                ("Inbox (47 unread, since 2026-05-10):", CODE_GRN),
                ("  • 3 from clients   →  reply today    [drafts ready]", CODE_FG),
                ("  • 12 newsletters   →  auto-archive   [done]", CODE_FG),
                ("  • 8 from team      →  read & reply   [drafts ready]", CODE_FG),
                ("  • 24 misc          →  triaged later  [labelled]", CODE_FG),
                ("", CODE_FG),
                ("→ Drafts saved. Open Gmail to review and send.", CORAL)],
               size=11.5)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "House rule: never let Claude send. Always review the draft.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s49_integrations(s):
    page_chrome(s, label="BEYOND  ·  INTEGRATIONS")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Every MCP server is a verb Claude can use.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Integrations through MCP.", font=F_HEAD, size=32, color=NAVY)
    rows = [
        ("NOTION",   "create-pages, fetch, search, update-page"),
        ("SLACK",    "send-message, read-channel, search, create-canvas"),
        ("GMAIL",    "list, read, reply (drafts only by rule)"),
        ("CALENDAR", "list-events, create-event, find-free-slot"),
        ("LINEAR",   "list-issues, create-issue, update-status"),
        ("GITHUB",   "via gh CLI — issues, PRs, releases, runs"),
        ("CHROME",   "navigate, click, get-text, screenshot"),
        ("FS",       "with permissions — your filesystem + your vault"),
    ]
    top = Inches(2.6)
    rh = Inches(0.5)
    add_text(s, Inches(0.8), top, Inches(4), Inches(0.4),
             "SERVER", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_text(s, Inches(5.0), top, Inches(8), Inches(0.4),
             "VERBS YOU GET", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    for i, (k, v) in enumerate(rows):
        y = top + Inches(0.55) + rh * i
        add_text(s, Inches(0.8), y, Inches(4), Inches(0.4),
                 k, font=F_CODE, size=14, color=NAVY, bold=True)
        add_text(s, Inches(5.0), y + Inches(0.02), Inches(8), Inches(0.4),
                 v, font=F_BODY, size=13, color=INK)


@slide
def s50_second_brain(s):
    page_chrome(s, label="BEYOND  ·  SECOND BRAIN")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Capture, distill, link. Your brain isn't a database — your vault is.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The Second Brain method.", font=F_HEAD, size=32, color=NAVY)
    cols = [
        ("01", "CAPTURE", "Anything that resonates. Lower the bar to entry."),
        ("02", "DISTILL", "Progressively summarise: highlight → bold → summary → gist."),
        ("03", "LINK", "Connect to existing notes — backlinks make the graph."),
    ]
    top = Inches(2.5)
    col_w = Inches(3.95)
    gap = Inches(0.1)
    for i, (n, head, body) in enumerate(cols):
        x = Inches(0.8) + (col_w + gap) * i
        add_rect(s, x, top, col_w, Inches(2.6), WHITE)
        add_rect(s, x, top, Inches(0.16), Inches(2.6), CORAL)
        add_text(s, x + Inches(0.35), top + Inches(0.3), col_w, Inches(0.5),
                 n, font=F_CODE, size=20, color=CORAL)
        add_text(s, x + Inches(0.35), top + Inches(0.95), col_w - Inches(0.5), Inches(0.5),
                 head, font=F_HEAD, size=22, color=NAVY)
        add_text(s, x + Inches(0.35), top + Inches(1.55), col_w - Inches(0.5), Inches(1.5),
                 body, font=F_BODY, size=13, color=INK, line_spacing=1.4)
    add_text(s, Inches(0.8), Inches(5.5), Inches(12), Inches(0.4),
             "Claude Code is the perfect Distill + Link tool. Capture is still you.",
             font=F_HEAD, size=15, color=CORAL, italic=True)


@slide
def s51_obsidian(s):
    page_chrome(s, label="BEYOND  ·  OBSIDIAN + CLAUDE")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "A SessionEnd hook writes today's note. Tomorrow's session reads it.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Obsidian + Claude Code.", font=F_HEAD, size=32, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(7.5), Inches(4.0),
               colorize_terminal(VAULT, max_lines=22), size=11)
    add_text(s, Inches(8.6), Inches(2.4), Inches(4.2), Inches(0.4),
             "THE LOOP", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    add_text(s, Inches(8.6), Inches(2.8), Inches(4.2), Inches(3.5),
             "Session starts: hook injects today's project note as context.\n\n"
             "Session ends: hook captures what you worked on, what was decided, what's open.\n\n"
             "No state is lost. No retelling tomorrow.",
             font=F_HEAD, size=13, color=INK, line_spacing=1.5)


@slide
def s52_daily_setup(s):
    page_chrome(s, label="BEYOND  ·  THE SETUP")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "What's running on my machine right now. Yours can look similar.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Example: my own setup.", font=F_HEAD, size=32, color=NAVY)
    items = [
        ("›", "Claude Code", "Primary terminal interface, two named sessions, prompt caching on"),
        ("›", "MCP servers", "Notion, Slack, Gmail, Chrome, Filesystem (permissioned)"),
        ("›", "Skills", "~50 personal skills — German comm, GDPR, debugging, plan-writing"),
        ("›", "Hooks", "SessionEnd → Obsidian, pre-commit → tests + lint, push → vault log"),
        ("›", "Obsidian Vault", "PARA structure, 800+ notes, daily session captures, linked"),
        ("›", "Cron + Routines", "06:00 digest, 18:00 standup prep, weekly review on Fridays"),
        ("›", "Worktrees", "Per-feature isolated branches, parallel work without churn"),
    ]
    top = Inches(2.5)
    rh = Inches(0.6)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=20, color=CORAL)
        add_text(s, Inches(1.3), y, Inches(4), Inches(0.45),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, Inches(5.5), y + Inches(0.05), Inches(7.5), Inches(0.5),
                 body, font=F_BODY, size=12.5, color=INK)


@slide
def s53_non_coder(s):
    page_chrome(s, label="BEYOND  ·  NON-CODE WORK")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Most of your job isn't writing code. Most of your code isn't writing code.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Workflows for non-coders.", font=F_HEAD, size=32, color=NAVY)
    items = [
        ("›", "Proposals & funding", "Draft a Förderantrag. Match required structure."),
        ("›", "Status reports", "Monthly client update from project tool + git activity."),
        ("›", "Client comms", "Tone-correct drafts in your language, your style."),
        ("›", "Research", "“Read these 15 PDFs and tell me what they disagree on.”"),
        ("›", "Spreadsheets", "Clean messy CSVs. Build pivot tables. Generate charts."),
        ("›", "Decks", "Like this one. Generated by the script you're looking at."),
    ]
    top = Inches(2.5)
    rh = Inches(0.65)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=20, color=CORAL)
        add_text(s, Inches(1.3), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.05), Inches(7), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s54_weekend_builds(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(2.4), Inches(12), Inches(0.5),
             "WHAT YOU COULD BUILD FOR YOURSELF", font=F_BODY, size=11,
             color=CORAL, bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(2.85), Inches(12), Inches(2.5),
             "One weekend.\nOne useful tool.", font=F_HEAD, size=54,
             color=NAVY, line_spacing=1.05)
    add_text(s, Inches(0.8), Inches(5.5), Inches(12), Inches(0.5),
             "Spec it. Plan it. Test it. Ship it. By Sunday evening.",
             font=F_HEAD, size=22, color=CORAL, italic=True)
    page_no(s)


# -------- PART 5: AI/ML ----------

@slide
def s55_ml_divider(s):
    section_divider(s, label="PART 05",
                    title="AI engineering\nwith Claude Code.",
                    sub="Scaffold the pipeline. Read the numbers. Judge the model.")


@slide
def s56_ml_frame(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  FRAMING")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Claude doesn't invent new architectures. It wires up the boring parts.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Where Claude shines in ML.", font=F_HEAD, size=32, color=NAVY)
    top = Inches(2.6)
    h = Inches(3.7)
    add_rect(s, Inches(0.8), top, Inches(5.9), h, WHITE)
    add_rect(s, Inches(0.8), top, Inches(5.9), Inches(0.55), CORAL)
    add_text(s, Inches(1.1), top + Inches(0.13), Inches(5.5), Inches(0.4),
             "GOOD AT", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    pts_a = ["Data prep & cleaning",
             "Dataloader scaffolding",
             "Training loop boilerplate",
             "Hyperparameter sweeps",
             "Eval metric reporting",
             "Result visualization",
             "RAG pipelines",
             "LoRA / adapter fine-tuning"]
    for i, t in enumerate(pts_a):
        add_text(s, Inches(1.1), top + Inches(0.85) + Inches(0.36) * i,
                 Inches(5.5), Inches(0.35),
                 "·  " + t, font=F_HEAD, size=14, color=INK)
    rx = Inches(7.0)
    add_rect(s, rx, top, Inches(5.5), h, WHITE)
    add_rect(s, rx, top, Inches(5.5), Inches(0.55), MUTED)
    add_text(s, rx + Inches(0.3), top + Inches(0.13), Inches(5), Inches(0.4),
             "STILL YOUR JOB", font=F_BODY, size=11, color=WHITE,
             bold=True, letter_spacing=300)
    pts_b = ["Choosing the problem",
             "Designing the dataset",
             "Picking the right loss",
             "Diagnosing why metrics moved",
             "Reading model failures",
             "Deciding when it's good enough",
             "Ethical scrutiny",
             "Buying the GPU time"]
    for i, t in enumerate(pts_b):
        add_text(s, rx + Inches(0.3), top + Inches(0.85) + Inches(0.36) * i,
                 Inches(5), Inches(0.35),
                 "·  " + t, font=F_HEAD, size=14, color=MUTED)


@slide
def s57_scaffolding(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  SCAFFOLDING")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "From “I have a CSV” to “I have a trained model with eval” — in 30 minutes.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Scaffolding a training pipeline.", font=F_HEAD, size=28, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(4.0),
               [("> claude", CORAL),
                ("\"I have reviews.csv with `text` and `label` columns.", CODE_FG),
                ("Build me a sentiment classifier. TF-IDF + Naive Bayes or LR.", CODE_FG),
                ("Show me train/test accuracy and a confusion matrix.\"", CODE_FG),
                ("", CODE_FG),
                ("[claude] /plan", CODE_DIM),
                ("Plan:", CODE_GRN),
                ("  1. Load CSV → DataFrame, drop NA, stratified split", CODE_FG),
                ("  2. Pipeline: TfidfVectorizer → LinearSVC", CODE_FG),
                ("  3. Fit, predict, report classification_report + cm", CODE_FG),
                ("  4. Save metrics to results.json", CODE_FG),
                ("  5. Smoke test: predict on hand-crafted pos + neg", CODE_FG),
                ("", CODE_FG),
                ("Approve? (y/n)", CODE_GRN)],
               size=12)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "The pipeline is mechanical. The judgement is yours.",
             font=F_HEAD, size=14, color=CORAL, italic=True)


@slide
def s58_ml_demo_deep(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  THE NUMBERS")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Real dataset. Real classifier. Real test accuracy.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Demo 5 in detail.", font=F_HEAD, size=32, color=NAVY)
    code_block(s, Inches(0.8), Inches(2.4), Inches(11.7), Inches(4.0),
               colorize_terminal(ML_OUT, max_lines=22), size=11)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "4 topics. 2,323 train docs. LinearSVC. 89.5% test accuracy. Fifteen minutes.",
             font=F_HEAD, size=13, color=CORAL, italic=True)


@slide
def s59_training_walkthrough(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  READING OUTPUT")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "What to look at. What to ignore.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Training output, decoded.", font=F_HEAD, size=30, color=NAVY)
    items = [
        ("01", "Accuracy ≠ everything",
         "A 95% accurate spam filter that misses every actual spam is useless. Look at recall on the rare class."),
        ("02", "Confusion matrix > single number",
         "Which classes does it confuse? That's where you'd add data."),
        ("03", "Train >> test accuracy?",
         "Overfitting. Regularize, simplify, or get more data."),
        ("04", "Per-class precision/recall",
         "“macro avg” weights every class equally. “weighted avg” weights by support."),
    ]
    top = Inches(2.5)
    rh = Inches(0.95)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.9), Inches(0.5),
                 n, font=F_CODE, size=22, color=CORAL)
        add_text(s, Inches(2.0), y + Inches(0.02), Inches(11), Inches(0.4),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(2.0), y + Inches(0.46), Inches(11), Inches(0.45),
                 body, font=F_BODY, size=13, color=INK, line_spacing=1.4)


@slide
def s60_eval_harness(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  EVALUATION")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "An eval harness is just a test suite for your model.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Evaluation harnesses.", font=F_HEAD, size=30, color=NAVY)
    items = [
        ("01", "Hold out a real test set", "Never train on it. Don't peek."),
        ("02", "Define what good means", "Numbers from the spec. Accuracy, FP rate, latency."),
        ("03", "Run the harness in CI", "Every model change. Same as code tests."),
        ("04", "Add adversarial cases", "Things you've seen fail. Edge inputs. Known-hard examples."),
        ("05", "Log + compare runs", "Today vs yesterday. Track regressions like bugs."),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.4),
                 n, font=F_CODE, size=18, color=CORAL)
        add_text(s, Inches(1.9), y - Inches(0.02), Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.5), y + Inches(0.05), Inches(6.5), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s61_rag(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  RAG")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "For most teams in 2026: RAG beats fine-tuning. Try it first.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Retrieval-Augmented Generation.", font=F_HEAD, size=28, color=NAVY)
    boxes = [("01", "INGEST", "Read your docs. Split by paragraph or section."),
             ("02", "EMBED", "Each chunk → vector via embedding model."),
             ("03", "STORE", "Vector DB — LanceDB, pgvector, Pinecone."),
             ("04", "RETRIEVE", "User query → vector → top-k chunks."),
             ("05", "GENERATE", "Stuff chunks into the prompt. Claude answers grounded.")]
    top = Inches(2.5)
    bw = Inches(2.36)
    gap = Inches(0.07)
    for i, (n, head, body) in enumerate(boxes):
        x = Inches(0.8) + (bw + gap) * i
        add_rect(s, x, top, bw, Inches(2.6), WHITE)
        add_rect(s, x, top, bw, Inches(0.4), CORAL)
        add_text(s, x + Inches(0.2), top + Inches(0.07), bw, Inches(0.3),
                 n, font=F_CODE, size=11, color=WHITE, bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.2), top + Inches(0.55), bw - Inches(0.3), Inches(0.5),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, x + Inches(0.2), top + Inches(1.1), bw - Inches(0.3), Inches(1.4),
                 body, font=F_BODY, size=11.5, color=INK, line_spacing=1.4)
    add_text(s, Inches(0.8), Inches(5.55), Inches(12), Inches(0.4),
             "Claude Code scaffolds all five steps. You bring the docs and the questions.",
             font=F_HEAD, size=14, color=INK, italic=True)


@slide
def s62_finetune(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  FINE-TUNING")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "When prompt + RAG aren't enough. Rare. But real.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Fine-tuning, briefly.", font=F_HEAD, size=32, color=NAVY)
    items = [
        ("›", "LoRA / QLoRA adapters", "Train a small adapter on top of a frozen base model. Fast and cheap."),
        ("›", "Hugging Face skills", "Claude Code has a `hf-skills-training` flow that wraps the boilerplate."),
        ("›", "Domain vocabulary", "Best use case: highly specialized terminology a base model doesn't know."),
        ("›", "Style / format", "Second-best: you need consistent output in a specific shape."),
        ("›", "Not a substitute for data quality", "If your prompt-engineering doesn't work, fine-tuning rarely fixes it."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=20, color=CORAL)
        add_text(s, Inches(1.3), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.05), Inches(7), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s63_wrong_tool(s):
    page_chrome(s, label="ML WITH CLAUDE  ·  WHEN NOT TO")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Most “we should train a model” problems aren't model problems.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "When ML training is the wrong tool.", font=F_HEAD, size=28, color=NAVY)
    items = [
        ("✗", "When a regex or SQL query would do", "Don't train a classifier to find “invoice” in emails."),
        ("✗", "When the rule is known and simple", "Write the rule. Tests pass. Move on."),
        ("✗", "When labelling will take longer than the project", "Time-box. If labelling > 1 week, reconsider."),
        ("✗", "When prompting + RAG already works at 90%", "Get the last 10% with rules + human review."),
        ("✗", "When you can't measure success", "Without an eval set, you have a vibe-classifier."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.5),
                 mark, font=F_HEAD, size=22, color=CORAL, bold=True)
        add_text(s, Inches(1.5), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.2), y + Inches(0.05), Inches(6.8), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s64_open_q(s):
    add_rect(s, 0, 0, SW, SH, CREAM)
    add_text(s, Inches(0.8), Inches(2.0), Inches(12), Inches(0.5),
             "AN OPEN QUESTION", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(2.5), Inches(12), Inches(3),
             "What should the\nAI engineer of 2027\nknow how to do alone?",
             font=F_HEAD, size=44, color=NAVY, line_spacing=1.1)
    add_text(s, Inches(0.8), Inches(6.0), Inches(12), Inches(0.5),
             "Discuss with your buddy for two minutes.",
             font=F_HEAD, size=18, color=CORAL, italic=True)
    page_no(s)


# -------- PART 6: ECOSYSTEM ----------

@slide
def s65_eco_divider(s):
    section_divider(s, label="PART 06",
                    title="The wider toolbox.",
                    sub="Claude Code is one of many. Know the others.")


@slide
def s66_cursor(s):
    page_chrome(s, label="ECOSYSTEM  ·  01 / 05")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "IDE-native. Fast. Parallel agent tabs.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Cursor.", font=F_HEAD, size=44, color=NAVY)
    items = [
        ("✓", "VS-Code-derived UI", "Pleasant for IDE-first workflows"),
        ("✓", "Cloud agents on isolated VMs", "Worktree per task, parallel"),
        ("✓", "Inline edits", "Faster than terminal for small changes"),
        ("✗", "Stalls at ambiguous decisions", "Without supervision"),
        ("✗", "No long-running autonomous mode", "Not built for overnight work"),
        ("✗", "Less context flexibility", "Tied to current file/workspace"),
    ]
    top = Inches(2.5)
    rh = Inches(0.65)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        col = CORAL if mark == "✓" else MUTED
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=col, bold=True)
        add_text(s, Inches(1.4), y, Inches(5.5), Inches(0.5),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, Inches(7.0), y + Inches(0.05), Inches(6), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s67_cline_codex_aider(s):
    page_chrome(s, label="ECOSYSTEM  ·  02 / 05")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Open-source. Model-agnostic. Bring your own provider.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Cline · Codex CLI · Aider.", font=F_HEAD, size=32, color=NAVY)
    cols = [
        ("CLINE", "Apache 2.0",
         ["VS Code + JetBrains + Zed",
          "Bring your own model",
          "OpenAI / Anthropic / Bedrock",
          "5M+ installs",
          "Great for cost-sensitive teams"]),
        ("CODEX CLI", "OpenAI",
         ["Terminal-first, OpenAI-only",
          "Open-source harness",
          "Strong on patches & refactors",
          "Good plugin ecosystem"]),
        ("AIDER", "OG, model-agnostic",
         ["The original terminal CLI",
          "Auto-commits to git",
          "Bring your own model",
          "Gold standard for pair-coding"]),
    ]
    top = Inches(2.5)
    col_w = Inches(3.95)
    gap = Inches(0.1)
    for i, (name, tag, pts) in enumerate(cols):
        x = Inches(0.8) + (col_w + gap) * i
        add_rect(s, x, top, col_w, Inches(3.7), WHITE)
        add_rect(s, x, top, col_w, Inches(0.55), CORAL)
        add_text(s, x + Inches(0.3), top + Inches(0.13), col_w, Inches(0.4),
                 name, font=F_BODY, size=12, color=WHITE,
                 bold=True, letter_spacing=300)
        add_text(s, x + Inches(0.3), top + Inches(0.85), col_w, Inches(0.4),
                 tag, font=F_CODE, size=12, color=MUTED, italic=True)
        for j, p in enumerate(pts):
            add_text(s, x + Inches(0.3), top + Inches(1.4) + Inches(0.42) * j,
                     col_w - Inches(0.5), Inches(0.4),
                     "·  " + p, font=F_HEAD, size=13, color=INK)


@slide
def s68_routines(s):
    page_chrome(s, label="ECOSYSTEM  ·  03 / 05")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Anthropic's “supervised autonomous” mode. The future of overnight work.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Anthropic Routines.", font=F_HEAD, size=36, color=NAVY)
    items = [
        ("›", "Package a Claude config", "Prompt + repos + tools + permissions, as one bundle"),
        ("›", "Schedule it", "Nightly, hourly, or on GitHub events (PR opened, release tagged)"),
        ("›", "Runs on Anthropic-managed cloud", "Not on your laptop. Your laptop can sleep."),
        ("›", "Result-validation loops", "Re-runs if tests fail, escalates if they keep failing"),
        ("›", "Handoffs to humans", "Pings you when judgement is needed; otherwise keeps going"),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=20, color=CORAL)
        add_text(s, Inches(1.3), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.05), Inches(7), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s69_decision_matrix(s):
    page_chrome(s, label="ECOSYSTEM  ·  04 / 05")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Quick decision matrix. Read it once, internalise.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "When to use which.", font=F_HEAD, size=32, color=NAVY)
    headers = ["YOUR NEED", "PICK", "WHY"]
    rows = [
        ("Long autonomous runs", "Claude Code + Routines", "Built for it"),
        ("Inline IDE editing speed", "Cursor", "Fastest small-change loop"),
        ("Cost-sensitive, open-source", "Cline", "BYO model, free harness"),
        ("Terminal pair-programming", "Aider or Claude Code", "Both terminal-native"),
        ("OpenAI-only stack", "Codex CLI", "Best fit for that model family"),
        ("Production workflows", "Claude Code", "Plan mode, hooks, MCP, skills"),
        ("Multi-agent orchestration", "Claude Code", "First-class subagents"),
        ("Browser-driving tasks", "Claude Code + Chrome MCP", "Best surface today"),
    ]
    top = Inches(2.5)
    col_x = [Inches(0.8), Inches(5.0), Inches(8.6)]
    col_w = [Inches(4.0), Inches(3.4), Inches(4.4)]
    for j, h in enumerate(headers):
        add_text(s, col_x[j], top, col_w[j], Inches(0.4),
                 h, font=F_BODY, size=10, color=CORAL,
                 bold=True, letter_spacing=300)
    add_rect(s, Inches(0.8), top + Inches(0.4),
             SW - Inches(1.6), Emu(9525), RULE)
    rh = Inches(0.48)
    for i, r in enumerate(rows):
        y = top + Inches(0.55) + rh * i
        for j, cell in enumerate(r):
            size = 13 if j != 1 else 14
            col = INK if j != 1 else CORAL
            italic = j == 0
            bold = j == 1
            add_text(s, col_x[j], y, col_w[j], Inches(0.4),
                     cell, font=F_HEAD, size=size, color=col,
                     italic=italic, bold=bold)


@slide
def s70_whats_coming(s):
    page_chrome(s, label="ECOSYSTEM  ·  05 / 05")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Where this is going, late 2026 and beyond.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "What's coming.", font=F_HEAD, size=44, color=NAVY)
    items = [
        ("→", "Multi-agent harnesses become first-class",
         "Less DIY orchestration; more declarative agent teams."),
        ("→", "Agentic IDEs", "VS Code-style tools but agent-native — Cursor 4, Zed AI, Windsurf."),
        ("→", "Cheaper long-running autonomy",
         "Routines + cheap inference make overnight work the default."),
        ("→", "Verified handoffs as primitive",
         "Subagents return cryptographic “done” proofs, not just text."),
        ("→", "Tighter loops with formal methods",
         "Specs as types. Plans as checked artifacts. Less drift."),
    ]
    top = Inches(2.5)
    rh = Inches(0.78)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=CORAL, bold=True)
        add_text(s, Inches(1.4), y - Inches(0.02), Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.05), Inches(7), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


# -------- PART 7: HANDS-ON BRIDGE ----------

@slide
def s71_handson_divider(s):
    section_divider(s, label="PART 07",
                    title="Your turn.",
                    sub="Three hours. The repo. Pair up. Go deep.")


@slide
def s72_the_repo(s):
    page_chrome(s, label="HANDS-ON  ·  THE REPO")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Everything from today, plus the demos, plus the exercises.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Clone this.", font=F_HEAD, size=44, color=NAVY)

    # Left: clone command + check.sh output
    code_block(s, Inches(0.8), Inches(2.5), Inches(7.2), Inches(3.8),
               [("$ git clone \\", CODE_FG),
                ("    github.com/Place-Beyond-Bytes/", CORAL),
                ("    pbb-vibecoding-masterclass.git", CORAL),
                ("$ cd pbb-vibecoding-masterclass", CODE_FG),
                ("$ bash check.sh", CODE_FG),
                ("", CODE_FG),
                ("  ✓ Node.js 20+", CODE_GRN),
                ("  ✓ git", CODE_GRN),
                ("  ✓ Claude Code installed", CODE_GRN),
                ("  ✓ api.anthropic.com reachable", CODE_GRN),
                ("", CODE_FG),
                ("  All good. See you on the day.", CODE_GRN)],
               size=13)

    # Right: QR code with caption
    add_text(s, Inches(8.4), Inches(2.5), Inches(4.2), Inches(0.4),
             "OR SCAN", font=F_BODY, size=10, color=CORAL,
             bold=True, letter_spacing=300)
    qr = HERE / "assets" / "screens" / "repo-qr.png"
    if qr.exists():
        s.shapes.add_picture(str(qr), Inches(8.6), Inches(2.9),
                             width=Inches(3.4), height=Inches(3.4))
    add_text(s, Inches(8.4), Inches(6.35), Inches(4.2), Inches(0.3),
             "github.com/coronell123/pbb-vibecoding-masterclass",
             font=F_CODE, size=9, color=MUTED, align="center")

    add_text(s, Inches(0.8), Inches(6.55), Inches(7.5), Inches(0.4),
             "If check.sh isn\'t green, raise your hand. Buddy starts without you.",
             font=F_HEAD, size=13, color=CORAL, italic=True)


@slide
def s73_exercises(s):
    page_chrome(s, label="HANDS-ON  ·  EXERCISES")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Ten exercises. Work in order until the break, then mix freely.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The ten exercises.", font=F_HEAD, size=32, color=NAVY)
    rows = [
        ("01", "First contact", "Read code, plan an improvement — no edits."),
        ("02", "Specs", "Convert a fuzzy client wish into checkable criteria."),
        ("03", "Plans", "Critique three plans. Reject what's wrong."),
        ("04", "TDD", "Red → green → refactor on validate_german_phone."),
        ("05", "Debug", "Name the root cause before the fix."),
        ("06", "Subagents", "Spawn three parallel investigators. Verify one claim."),
        ("07", "Orchestrator", "Feature-by-feature build with verified handoffs."),
        ("08", "Playwright", "Generate E2E tests for the Pomodoro app."),
        ("09", "Second Brain", "Wire up an Obsidian SessionEnd hook."),
        ("10", "ML scaffold", "Train your own classifier. Read the numbers."),
    ]
    top = Inches(2.45)
    rh = Inches(0.4)
    for i, (n, head, body) in enumerate(rows):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.8), Inches(0.35),
                 n, font=F_CODE, size=14, color=CORAL)
        add_text(s, Inches(1.8), y, Inches(4), Inches(0.35),
                 head, font=F_HEAD, size=15, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.03), Inches(7), Inches(0.35),
                 body, font=F_BODY, size=12, color=INK)
    add_text(s, Inches(0.8), Inches(6.55), Inches(12), Inches(0.4),
             "Plus 11-build: pick a project, ship it, demo it.",
             font=F_HEAD, size=13, color=CORAL, italic=True)


@slide
def s74_pair_up(s):
    page_chrome(s, label="HANDS-ON  ·  PAIR UP")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Mixed pairs. High-experience with low. Buddy stays for the day.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Trios, not duos.", font=F_HEAD, size=40, color=NAVY)
    items = [
        ("01", "Pair up by show of hands", "Experience: 1 (never) → 5 (daily). Highs and lows pair."),
        ("02", "Negotiate before prompting", "Two humans align on the prompt. Claude is the third party."),
        ("03", "Driver/navigator rotates", "Every 15 minutes. Both seats teach you different things."),
        ("04", "Talk through your plan out loud", "Your buddy is the first reviewer. Claude is the second."),
    ]
    top = Inches(2.5)
    rh = Inches(0.95)
    for i, (n, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.9), Inches(0.5),
                 n, font=F_CODE, size=22, color=CORAL)
        add_text(s, Inches(2.0), y + Inches(0.02), Inches(11), Inches(0.5),
                 head, font=F_HEAD, size=20, color=NAVY)
        add_text(s, Inches(2.0), y + Inches(0.5), Inches(11), Inches(0.4),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s75_house_rules(s):
    page_chrome(s, label="HANDS-ON  ·  HOUSE RULES")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "On the wall the whole time. Live by them today.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Four rules for the room.", font=F_HEAD, size=38, color=NAVY)
    rules = [
        ("01", "Trios, not duos.", "You, your buddy, and Claude. Two humans negotiate before either prompts."),
        ("02", "Show your plan before your code.", "If you're stuck and ask me, the first question back is “what's your plan?”"),
        ("03", "Evidence wins.", "“It works” is not done. Show the green test. Show the screenshot. Verify."),
        ("04", "No real client data.", "Synthetic data only. No keys, no PII, no NDA-covered material."),
    ]
    top = Inches(2.5)
    rh = Inches(0.95)
    for i, (n, head, body) in enumerate(rules):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(1), Inches(0.5),
                 n, font=F_CODE, size=28, color=CORAL)
        add_text(s, Inches(2.2), y + Inches(0.05), Inches(10.5), Inches(0.45),
                 head, font=F_HEAD, size=22, color=NAVY)
        add_text(s, Inches(2.2), y + Inches(0.5), Inches(10.5), Inches(0.5),
                 body, font=F_BODY, size=14, color=INK)


@slide
def s76_go(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_text(s, Inches(0.8), Inches(2.5), Inches(12), Inches(0.5),
             "YOUR TURN", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    add_text(s, Inches(0.8), Inches(2.5), Inches(12), Inches(4),
             "Go.", font=F_HEAD, size=220, color=WHITE, italic=True)
    dark_footer(s, label_left="")


# -------- PART 8: CLOSE ----------

@slide
def s77_recap_rhythm(s):
    page_chrome(s, label="WRAP-UP  ·  THE RHYTHM")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "If you take one thing home, take this.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "The rhythm, again.", font=F_HEAD, size=40, color=NAVY)
    steps = ["SPEC", "PLAN", "TEST", "IMPLEMENT", "VERIFY"]
    bw = Inches(2.2)
    by = Inches(3.0)
    gap = Inches(0.16)
    x0 = Inches(0.85)
    for i, name in enumerate(steps):
        x = x0 + (bw + gap) * i
        col = CORAL if name == "VERIFY" else NAVY
        add_rect(s, x, by, bw, Inches(1.6), WHITE)
        add_rect(s, x, by, bw, Inches(0.18), col)
        add_text(s, x + Inches(0.3), by + Inches(0.6), bw, Inches(0.7),
                 name, font=F_HEAD, size=22, color=col,
                 align="center", italic=True)
        if i < 4:
            add_text(s, x + bw, by + Inches(0.5), gap, Inches(0.5),
                     "→", font=F_HEAD, size=20, color=CORAL, align="center")
    add_text(s, Inches(0.8), Inches(5.5), Inches(12), Inches(0.5),
             "In that order. Every time. Skip Verify and you didn't finish.",
             font=F_HEAD, size=18, color=CORAL, italic=True, align="center")


@slide
def s78_when_not(s):
    page_chrome(s, label="WRAP-UP  ·  HONESTY")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "We spent today on the right way. Here's the other half.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "When NOT to use Claude Code.", font=F_HEAD, size=30, color=NAVY)
    items = [
        ("✕", "High-stakes security-critical code", "Human review is non-negotiable."),
        ("✕", "Code touching real client data", "Confidentiality rules apply. Personal accounts only."),
        ("✕", "When you don't know what you want yet", "Talk to a human first. Claude can't decide what to build."),
        ("✕", "Five-line tweaks", "Just type them. Overhead isn't worth it."),
        ("✕", "When the problem isn't a software problem", "Most “tech” problems are coordination problems."),
    ]
    top = Inches(2.5)
    rh = Inches(0.75)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.5), Inches(0.5),
                 mark, font=F_HEAD, size=22, color=CORAL, bold=True)
        add_text(s, Inches(1.5), y, Inches(4.5), Inches(0.45),
                 head, font=F_HEAD, size=18, color=NAVY)
        add_text(s, Inches(6.2), y + Inches(0.05), Inches(6.8), Inches(0.5),
                 body, font=F_BODY, size=13, color=INK)


@slide
def s79_resources(s):
    page_chrome(s, label="WRAP-UP  ·  TAKE WITH YOU")
    add_text(s, Inches(0.8), Inches(0.7), Inches(12), Inches(0.4),
             "Bookmark these. Office hours open for two weeks.",
             font=F_HEAD, size=14, color=MUTED, italic=True)
    add_text(s, Inches(0.8), Inches(1.05), Inches(12), Inches(1),
             "Resources.", font=F_HEAD, size=44, color=NAVY)
    items = [
        ("›", "Workshop repo", "github.com/coronell123/pbb-vibecoding-masterclass"),
        ("›", "Anthropic docs", "code.claude.com/docs/en  ·  the source of truth"),
        ("›", "Anthropic Skilljar (free)", "Claude Code in Action — official video course"),
        ("›", "Cheatsheet", "_handouts/cheatsheet.md — top commands and anti-patterns"),
        ("›", "Plan Critique Checklist", "_handouts/plan-critique-checklist.md — the five questions"),
        ("›", "Office hours", "30-min slots for two weeks. Email me to book."),
    ]
    top = Inches(2.5)
    rh = Inches(0.65)
    for i, (mark, head, body) in enumerate(items):
        y = top + rh * i
        add_text(s, Inches(0.8), y, Inches(0.4), Inches(0.4),
                 mark, font=F_HEAD, size=22, color=CORAL)
        add_text(s, Inches(1.4), y, Inches(4.5), Inches(0.4),
                 head, font=F_HEAD, size=17, color=NAVY)
        add_text(s, Inches(6.0), y + Inches(0.05), Inches(7), Inches(0.4),
                 body, font=F_CODE, size=12, color=MUTED)


@slide
def s80_close(s):
    add_rect(s, 0, 0, SW, SH, NAVY_DEEP)
    add_text(s, Inches(0.8), Inches(0.9), Inches(12), Inches(0.4),
             "ONE THING TO TAKE HOME", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400)
    rhythms = [("Spec.", WHITE), ("Plan.", WHITE), ("Test.", WHITE),
               ("Implement.", WHITE), ("Verify.", CORAL)]
    y0 = Inches(1.4)
    rh = Inches(1.05)
    for i, (word, col) in enumerate(rhythms):
        add_text(s, Inches(0.8), y0 + rh * i, Inches(12), Inches(1.1),
                 word, font=F_HEAD, size=64, color=col, italic=True)
    add_text(s, SW - Inches(5.5), Inches(1.9), Inches(5), Inches(0.4),
             "IN THAT ORDER", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400, align="right")
    add_text(s, SW - Inches(5.5), Inches(2.35), Inches(5), Inches(0.4),
             "EVERY TIME", font=F_BODY, size=11, color=CORAL,
             bold=True, letter_spacing=400, align="right")
    add_text(s, SW - Inches(5.5), Inches(4.5), Inches(5), Inches(0.6),
             "Thank you.", font=F_HEAD, size=44, color=WHITE,
             italic=True, align="right")
    add_text(s, Inches(0.8), SH - Inches(0.55), Inches(9), Inches(0.35),
             "ELIAS JELINEK  ·  PLACE BEYOND BYTES  ·  SUST  ·  UDE",
             font=F_BODY, size=8, color=DIM_LIGHT, letter_spacing=200)
    page_no(s, light=True)


# ============================================================

TOTAL = len(SLIDES)


def main():
    global CURRENT_PAGE
    for idx, build in enumerate(SLIDES, start=1):
        CURRENT_PAGE = idx
        s = prs.slides.add_slide(blank_layout)
        build(s)
    prs.save(OUT)
    print(f"Wrote {OUT}  ·  {len(SLIDES)} slides")


if __name__ == "__main__":
    main()
