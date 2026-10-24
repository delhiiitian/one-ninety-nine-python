"""Expense Tracker: record spending in a CSV file and see where the money goes.

Examples:
    python tracker.py add 450 food "Pizza night"
    python tracker.py add 1200 bills --date 2026-10-22
    python tracker.py list --last 5
    python tracker.py report 2026-10
    python tracker.py report 2026-10 --budget groceries=5000 --budget food=1000
    python tracker.py export expenses.json
"""

import argparse
import sys
from datetime import date

import reports
import storage


def parse_month(text):
    year, month = text.split("-")
    return int(year), int(month)


def parse_budget(text):
    category, _, amount = text.partition("=")
    return category.lower(), float(amount)


def build_parser():
    parser = argparse.ArgumentParser(description="Track your spending in a CSV file.")
    parser.add_argument("--file", default=storage.DEFAULT_FILE, help="CSV file to use")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", help="record an expense")
    add.add_argument("amount", type=float)
    add.add_argument("category")
    add.add_argument("note", nargs="?", default="")
    add.add_argument("--date", type=date.fromisoformat, default=date.today())

    show = sub.add_parser("list", help="show recent expenses")
    show.add_argument("--last", type=int, default=10)

    report = sub.add_parser("report", help="summary for a month (YYYY-MM)")
    report.add_argument("month", type=parse_month)
    report.add_argument("--budget", type=parse_budget, action="append", default=[])

    export = sub.add_parser("export", help="save everything as JSON")
    export.add_argument("output")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    expenses, problems = storage.load(args.file)
    for problem in problems:
        print("warning: skipped", problem, file=sys.stderr)

    if args.command == "add":
        if args.amount <= 0:
            print("error: amount must be positive", file=sys.stderr)
            return 1
        expense = storage.Expense(args.date, args.category.lower(), args.amount, args.note)
        storage.append(expense, args.file)
        print(f"Saved: {expense.date} {expense.category} Rs {expense.amount:,.2f} {expense.note}")
    elif args.command == "list":
        for e in sorted(expenses, key=lambda e: e.date)[-args.last:]:
            print(f"{e.date}  {e.category:<10} Rs {e.amount:>9,.2f}  {e.note}")
    elif args.command == "report":
        year, month = args.month
        chosen = reports.in_month(expenses, year, month)
        print(reports.format_report(chosen, f"Spending in {year}-{month:02}"))
        for cat, spent, limit in reports.check_budgets(chosen, dict(args.budget)):
            print(f"! Over budget on {cat}: spent Rs {spent:,.0f} of Rs {limit:,.0f}")
    elif args.command == "export":
        count = storage.export_json(expenses, args.output)
        print(f"Exported {count} expenses to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
