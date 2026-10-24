"""6.5 CSV files: spreadsheets as plain text.

Real-world comparison: an Excel sheet saved as text. Each line is a
row and commas separate the columns. Banks, shops and government
portals all let you download data as CSV.
"""

import csv
from pathlib import Path

here = Path(__file__).parent
sales_file = here / "data" / "sales.csv"

# DictReader turns each row into a dictionary using the header line.
with open(sales_file, newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

print("First row:", rows[0])

# Everything comes in as text, so convert numbers.
revenue_by_product = {}
for row in rows:
    amount = int(row["quantity"]) * int(row["price"])
    revenue_by_product[row["product"]] = revenue_by_product.get(row["product"], 0) + amount

for product, revenue in sorted(revenue_by_product.items(), key=lambda kv: -kv[1]):
    print(f"{product:8} Rs {revenue}")

# Write a CSV summary with DictWriter.
out = here / "output"
out.mkdir(exist_ok=True)
with open(out / "summary.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["product", "revenue"])
    writer.writeheader()
    for product, revenue in revenue_by_product.items():
        writer.writerow({"product": product, "revenue": revenue})

print((out / "summary.csv").read_text(encoding="utf-8"))
