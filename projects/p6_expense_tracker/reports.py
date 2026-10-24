"""Turning a list of expenses into summaries. No file access here."""

from collections import defaultdict


def in_month(expenses, year, month):
    return [e for e in expenses if e.date.year == year and e.date.month == month]


def by_category(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.amount
    return dict(sorted(totals.items(), key=lambda kv: -kv[1]))


def monthly_totals(expenses):
    totals = defaultdict(float)
    for e in expenses:
        totals[e.date.strftime("%Y-%m")] += e.amount
    return dict(sorted(totals.items()))


def check_budgets(expenses, budgets):
    """Return (category, spent, budget) for every category over budget."""
    spent = by_category(expenses)
    return [(cat, spent.get(cat, 0), limit) for cat, limit in budgets.items()
            if spent.get(cat, 0) > limit]


def format_report(expenses, title):
    if not expenses:
        return f"{title}\n  (no expenses)"
    totals = by_category(expenses)
    grand = sum(totals.values())
    width = max(len(c) for c in totals)
    lines = [title, "-" * (width + 34)]
    for cat, amount in totals.items():
        bar = "#" * round(amount / grand * 20)
        lines.append(f"{cat:<{width}}  Rs {amount:>9,.0f}  {amount / grand:5.1%}  {bar}")
    lines.append("-" * (width + 34))
    lines.append(f"{'total':<{width}}  Rs {grand:>9,.0f}")
    return "\n".join(lines)
