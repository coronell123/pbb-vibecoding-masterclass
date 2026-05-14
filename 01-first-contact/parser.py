"""
Parse a CSV of grocery receipts into a list of dicts.

Sample input row:
    2026-04-12;REWE;Milk 1L;1.49;EUR
"""

import csv
from datetime import datetime
from pathlib import Path


def parse_receipts(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for line_no, raw in enumerate(reader, start=1):
            if not raw or raw[0].startswith("#"):
                continue
            if len(raw) != 5:
                continue
            date_s, shop, item, price_s, currency = raw
            try:
                date = datetime.strptime(date_s.strip(), "%Y-%m-%d").date()
                price = float(price_s.replace(",", "."))
            except ValueError:
                continue
            rows.append({
                "date": date,
                "shop": shop.strip().upper(),
                "item": item.strip(),
                "price": price,
                "currency": currency.strip().upper(),
            })
    return rows


def total_by_shop(rows):
    totals = {}
    for r in rows:
        totals[r["shop"]] = totals.get(r["shop"], 0) + r["price"]
    return totals


if __name__ == "__main__":
    sample = Path(__file__).parent / "receipts.csv"
    data = parse_receipts(sample)
    print(f"Parsed {len(data)} rows")
    for shop, total in total_by_shop(data).items():
        print(f"  {shop}: {total:.2f}")
