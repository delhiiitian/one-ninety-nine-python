"""Bill splitting logic. No input() or print() here, so it is easy to test."""

GST_PERCENT = 5


def subtotal(items):
    """items is a list of (name, price, quantity) tuples."""
    total = 0
    for name, price, quantity in items:
        total += price * quantity
    return total


def tax_amount(amount, percent=GST_PERCENT):
    return round(amount * percent / 100, 2)


def tip_amount(amount, percent):
    return round(amount * percent / 100, 2)


def split(total, people):
    """Return the share per person, rounded UP to the next rupee,
    and how much extra that rounding collects."""
    if people < 1:
        raise ValueError("at least one person must pay")
    exact = total / people
    share = int(exact) if exact == int(exact) else int(exact) + 1
    extra = round(share * people - total, 2)
    return share, extra


def build_bill(items, tip_percent, people):
    """Do every calculation and return the results in one dictionary."""
    sub = subtotal(items)
    tax = tax_amount(sub)
    tip = tip_amount(sub, tip_percent)
    total = round(sub + tax + tip, 2)
    share, extra = split(total, people)
    return {
        "items": items,
        "subtotal": sub,
        "tax": tax,
        "tip": tip,
        "tip_percent": tip_percent,
        "total": total,
        "people": people,
        "share": share,
        "extra": extra,
    }


def format_receipt(bill, restaurant="Python Diner"):
    width = 36
    lines = [
        "=" * width,
        restaurant.center(width),
        "=" * width,
    ]
    for name, price, quantity in bill["items"]:
        left = f"{name} x{quantity}"
        lines.append(f"{left:<24}{price * quantity:>12.2f}")
    lines.append("-" * width)
    lines.append(f"{'Subtotal':<24}{bill['subtotal']:>12.2f}")
    lines.append(f"{'GST ' + str(GST_PERCENT) + '%':<24}{bill['tax']:>12.2f}")
    lines.append(f"{'Tip ' + str(bill['tip_percent']) + '%':<24}{bill['tip']:>12.2f}")
    lines.append("=" * width)
    lines.append(f"{'TOTAL':<24}{bill['total']:>12.2f}")
    lines.append(f"{'Each of ' + str(bill['people']) + ' pays':<24}{bill['share']:>12}")
    if bill["extra"]:
        lines.append(f"(rounding adds Rs {bill['extra']:.2f} to the tip jar)")
    return "\n".join(lines)
