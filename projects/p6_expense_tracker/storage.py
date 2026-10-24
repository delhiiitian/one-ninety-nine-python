"""Reading and writing expenses. This is the only file that touches the disk."""

import csv
import json
from dataclasses import dataclass, asdict
from datetime import date
from pathlib import Path

FIELDS = ["date", "category", "amount", "note"]
DEFAULT_FILE = Path(__file__).parent / "data" / "expenses.csv"


@dataclass
class Expense:
    date: date
    category: str
    amount: float
    note: str = ""

    @classmethod
    def from_row(cls, row):
        return cls(date.fromisoformat(row["date"]), row["category"].strip().lower(),
                   float(row["amount"]), row.get("note", "").strip())

    def to_row(self):
        amount = int(self.amount) if self.amount == int(self.amount) else self.amount
        return {"date": self.date.isoformat(), "category": self.category,
                "amount": amount, "note": self.note}


def load(path=DEFAULT_FILE):
    """Return all expenses. A missing file simply means no expenses yet.
    Bad rows are skipped and reported instead of crashing the program."""
    path = Path(path)
    if not path.exists():
        return [], []
    expenses, problems = [], []
    with open(path, newline="", encoding="utf-8") as file:
        for line_no, row in enumerate(csv.DictReader(file), start=2):
            try:
                expenses.append(Expense.from_row(row))
            except (ValueError, KeyError, TypeError, AttributeError) as error:
                problems.append(f"line {line_no}: {error}")
    return expenses, problems


def append(expense, path=DEFAULT_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(expense.to_row())


def export_json(expenses, path):
    data = [e.to_row() for e in expenses]
    Path(path).write_text(json.dumps(data, indent=2), encoding="utf-8")
    return len(data)
