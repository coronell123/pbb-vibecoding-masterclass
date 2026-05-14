"""
Print the average daily temperature from weather.csv.

Expected output (roughly):
    Average daily temperature: 14.3 C
"""

import csv
from pathlib import Path


def average_temperature(path):
    total = 0
    count = 0
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            date, low, high = row
            # Daily average of low and high
            daily_avg = (low + high) / 2
            total += daily_avg
            count += 1
    return total / count


if __name__ == "__main__":
    csv_path = Path(__file__).parent / "weather.csv"
    avg = average_temperature(csv_path)
    print(f"Average daily temperature: {avg:.1f} C")
