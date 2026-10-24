"""9.9 Simple data analysis.

Real-world comparison: a shopkeeper's end-of-month review. Looking
at the sales book, she asks: what sold best? Which day was busiest?
Is business growing? Python answers these with a few lines, and
libraries like pandas take the same ideas much further.
"""

import csv
import statistics
from collections import defaultdict
from io import StringIO

SALES_CSV = """date,item,qty,price
2026-10-01,tea,30,20
2026-10-01,coffee,10,40
2026-10-02,tea,28,20
2026-10-02,samosa,40,15
2026-10-03,coffee,22,40
2026-10-03,tea,35,20
2026-10-04,samosa,55,15
2026-10-04,coffee,25,40
"""

rows = list(csv.DictReader(StringIO(SALES_CSV)))
for row in rows:
    row["revenue"] = int(row["qty"]) * int(row["price"])

by_item = defaultdict(int)
by_day = defaultdict(int)
for row in rows:
    by_item[row["item"]] += row["revenue"]
    by_day[row["date"]] += row["revenue"]

print("Revenue by item:")
for item, revenue in sorted(by_item.items(), key=lambda kv: -kv[1]):
    share = revenue / sum(by_item.values())
    print(f"  {item:7} Rs {revenue:5}  {share:5.1%}  {'#' * (revenue // 100)}")

daily = list(by_day.values())
print("Daily revenue:", daily)
print("Average day: Rs", round(statistics.mean(daily)))
print("Spread (std dev): Rs", round(statistics.stdev(daily)))
best_day = max(by_day, key=by_day.get)
print("Best day:", best_day, "with Rs", by_day[best_day])

growth = (daily[-1] - daily[0]) / daily[0]
print(f"Growth from first to last day: {growth:.0%}")

# Trend line: is revenue going up each day?
days = list(range(len(daily)))
slope, intercept = statistics.linear_regression(days, daily)
print(f"Trend: about Rs {slope:.0f} more every day")
