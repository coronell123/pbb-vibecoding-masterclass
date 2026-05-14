# Plan — CSV Export

Reviewed against `spec.md` (commit `a1b2c3d`). Touched files marked with `→`.

## Changes

→ `parser.py` — add `export_to_csv(rows, out_path)` at the bottom.
→ `tests/test_export.py` — new file. Three tests:
   1. round-trip: parse a sample, export, re-read, assert equality on dict-cast.
   2. empty list: assert file contains exactly one line (the header).
   3. overwrite refusal: write to an existing path, expect `FileExistsError`.

## Assumptions explicitly stated

- The CSV writer uses `csv.DictWriter` with `extrasaction="ignore"` so any future extra fields on rows don't break the export.
- `;` as delimiter would match the input format, but the spec says CSV — interpreted as comma per RFC 4180. **If wrong, flag and re-plan before coding.**
- `out_path` is `str | Path`. We `Path()`-wrap defensively.

## Out of scope (matches spec)

- No CLI flag.
- No xlsx.
- No multi-currency.

## Test command

```bash
pytest tests/test_export.py -v
```

## Definition of done

- All three tests green.
- `python -c "from parser import export_to_csv; export_to_csv([], 'empty.csv')"` produces a 1-line file.
- The function appears in `__all__` if `parser.py` has one (it doesn't — skip).
