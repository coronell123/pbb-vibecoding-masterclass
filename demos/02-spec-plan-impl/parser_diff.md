## Diff against `parser.py` — the implementation

```diff
@@ parser.py @@
 import csv
 from datetime import datetime
 from pathlib import Path
+from typing import Iterable

@@ end of file @@
+
+
+CSV_COLUMNS = ("date", "shop", "item", "price", "currency")
+
+
+def export_to_csv(rows: Iterable[dict], out_path: str | Path) -> Path:
+    """Write parsed receipt rows to a CSV file.
+
+    Spec: demos/02-spec-plan-impl/spec.md
+    """
+    out = Path(out_path)
+    if out.exists():
+        raise FileExistsError(f"{out} already exists")
+    with out.open("w", encoding="utf-8", newline="") as f:
+        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
+        writer.writeheader()
+        for r in rows:
+            writer.writerow({
+                **r,
+                "date": r["date"].strftime("%Y-%m-%d"),
+                "price": f"{r['price']:.2f}",
+            })
+    return out
```

## Test output

```
tests/test_export.py::test_round_trip PASSED                              [ 33%]
tests/test_export.py::test_empty_writes_header_only PASSED                [ 66%]
tests/test_export.py::test_refuses_to_overwrite PASSED                    [100%]

=========================== 3 passed in 0.04s ============================
```
