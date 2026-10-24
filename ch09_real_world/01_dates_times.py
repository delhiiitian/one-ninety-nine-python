"""9.1 Dates and times.

Real-world comparison: a calendar and a stopwatch on your wall.
datetime knows how long months are, which years are leap years, and
how to show a date the way people in different places expect.
"""

from datetime import date, datetime, timedelta, timezone

launch = date(2026, 10, 24)
print("Launch day:", launch, "| weekday:", launch.strftime("%A"))

# Date maths with timedelta.
print("30 days later:", launch + timedelta(days=30))
print("1 week earlier:", launch - timedelta(weeks=1))
new_year = date(2027, 1, 1)
print("Days until new year:", (new_year - launch).days)

# Formatting (strftime) and parsing (strptime).
meeting = datetime(2026, 10, 24, 15, 30)
print("US style:", meeting.strftime("%m/%d/%Y %I:%M %p"))
print("Indian style:", meeting.strftime("%d-%m-%Y %H:%M"))
print("ISO 8601:", meeting.isoformat())
parsed = datetime.strptime("25/12/2026 09:00", "%d/%m/%Y %H:%M")
print("Parsed:", parsed, "| a", parsed.strftime("%A"))

# Time zones: store in UTC, show in local time.
ist = timezone(timedelta(hours=5, minutes=30))
utc_time = datetime(2026, 10, 24, 10, 0, tzinfo=timezone.utc)
print("10:00 UTC is", utc_time.astimezone(ist).strftime("%H:%M"), "in India")


# Real use: is a subscription still active, and when does it renew?
def renewal_info(start, months, today):
    end = date(start.year + (start.month - 1 + months) // 12,
               (start.month - 1 + months) % 12 + 1, start.day)
    status = "active" if today < end else "expired"
    return f"Plan {status}, ends {end:%d %b %Y} ({(end - today).days} days left)"


print(renewal_info(date(2026, 8, 15), 3, today=launch))
