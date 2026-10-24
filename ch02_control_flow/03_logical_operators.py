"""2.3 Combining conditions with and, or, not.

Real-world comparison: a bank loan officer. You get the loan if you
have a job AND a good credit score. A cinema lets you in if you have
a ticket OR a pass. NOT flips a yes into a no.
"""

has_job = True
credit_score = 720
if has_job and credit_score >= 700:
    print("Loan approved")
else:
    print("Loan rejected")

has_ticket = False
has_pass = True
if has_ticket or has_pass:
    print("Welcome to the cinema")

is_holiday = False
if not is_holiday:
    print("Office is open today")

# Short-circuit: Python stops as soon as the answer is known.
# Here, len(name) is never checked when name is empty.
name = ""
if name and len(name) > 3:
    print("Long name")
else:
    print("Name is empty or short")

# Real use: a login check with a lockout.
username_ok = True
password_ok = True
attempts = 2
MAX_ATTEMPTS = 3
if username_ok and password_ok and attempts < MAX_ATTEMPTS:
    print("Logged in")
elif attempts >= MAX_ATTEMPTS:
    print("Account locked")
else:
    print("Wrong username or password")
