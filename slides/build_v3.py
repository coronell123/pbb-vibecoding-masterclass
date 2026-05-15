"""Driver: assemble v3 deck with new intro + discussion + outcome slides."""

import build_deck
from build_deck import SLIDES, prs, blank_layout, OUT
from _new_slides import (
    sA_about_me, sB_what_we_build, sC_what_vibe, sD_what_agentic,
    sE_llm_primer, sF_claude_vs_others, sG_maturity_ladder,
    sH_what_harness, sI_lifecycle, sJ_discussion_open,
    sK_discussion_workflows, sL_discussion_beyond, sM_discussion_ecosystem,
    sN_outcome_plan_mode, sO_outcome_hooks,
    sP_e2e_workflow, sQ_docker_pattern, sR_maintain_observe,
    sS_ml_frame, sT_ml_plan,
)


def fn_index(name):
    """Find index of a slide function in SLIDES by name."""
    for i, fn in enumerate(SLIDES):
        if fn.__name__ == name:
            return i
    raise ValueError(f"slide not found: {name}")


def insert_after(target, new_fns):
    """Insert new_fns into SLIDES right after the function named `target`."""
    idx = fn_index(target) + 1
    for fn in reversed(new_fns):
        SLIDES.insert(idx, fn)


# Splice in order (later insertions don't shift earlier-positioned slides)
insert_after("s77_recap_rhythm",        [sS_ml_frame, sT_ml_plan])
insert_after("s70_whats_coming",        [sM_discussion_ecosystem])
insert_after("s54_weekend_builds",      [sL_discussion_beyond])
insert_after("s42_production_checklist", [sK_discussion_workflows])
insert_after("s41_deployment",          [sP_e2e_workflow, sQ_docker_pattern, sR_maintain_observe])
insert_after("s29_hooks",               [sO_outcome_hooks])
insert_after("s26_plan_mode",           [sN_outcome_plan_mode])
insert_after("s02_agenda",              [sB_what_we_build, sC_what_vibe, sD_what_agentic,
                                          sE_llm_primer, sF_claude_vs_others,
                                          sG_maturity_ladder, sH_what_harness,
                                          sI_lifecycle, sJ_discussion_open])
insert_after("s01_title",               [sA_about_me])


def main():
    build_deck.TOTAL = len(SLIDES)
    for idx, fn in enumerate(SLIDES, start=1):
        build_deck.CURRENT_PAGE = idx
        s = prs.slides.add_slide(blank_layout)
        fn(s)
    prs.save(OUT)
    print(f"Wrote {OUT}  ·  {len(SLIDES)} slides")


if __name__ == "__main__":
    main()
