# Spec — CSV Export for the Receipts Parser

**Owner:** Elias · **Status:** approved · **Last touched:** 2026-05-14

## Why

The receipts parser produces a list of dicts. The user (a small bookkeeping client) wants to drop the parsed data into their existing spreadsheet pipeline. That pipeline reads CSV.

## What

A new function `export_to_csv(rows, out_path)` in `parser.py` that writes the parsed rows to a CSV file at `out_path`.

## Checkable success criteria

1. Calling `export_to_csv(parse_receipts("receipts.csv"), "out.csv")` produces a file at `out.csv`.
2. The file opens cleanly in Excel **and** in `csv.reader`.
3. Columns, in order: `date`, `shop`, `item`, `price`, `currency`.
4. The header row is present.
5. Dates are formatted as `YYYY-MM-DD`.
6. Prices use a dot as the decimal separator (not a comma).
7. UTF-8 encoded.
8. If `rows` is empty, the file contains only the header row.

## What it must NOT do

- Mutate the input list.
- Overwrite existing files silently — raise `FileExistsError` if `out_path` exists.
- Add columns we didn't ask for (no `id`, no `created_at`).

## Out of scope

- Multi-currency conversion.
- Excel `.xlsx` output (CSV only).
- A CLI flag (Python API only for this iteration).

## Validation

A new test in `tests/test_export.py` exercises the success criteria and one failure mode (overwrite refusal).
