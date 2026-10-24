"""2.7 break and continue: leaving a loop early or skipping a turn.

Real-world comparison: searching your bag for your keys. Once you
find them, you stop searching (break). If you pull out a receipt,
you ignore it and keep going (continue).
"""

bag = ["wallet", "receipt", "pen", "keys", "phone"]
for item in bag:
    if item == "receipt":
        continue          # skip this one, go to the next item
    if item == "keys":
        print("Found the keys!")
        break             # stop the loop completely
    print("Checked:", item)

# Skip odd numbers.
for number in range(1, 11):
    if number % 2 == 1:
        continue
    print(number, end=" ")
print()

# for ... else: the else runs only if the loop did NOT break.
emails = ["a@x.com", "b@x.com", "c@x.com"]
wanted = "z@x.com"
for email in emails:
    if email == wanted:
        print("User found")
        break
else:
    print("User not found")

# Real use: stop reading sensor values at the first dangerous one.
readings = [21, 23, 22, 87, 24]
for minute, value in enumerate(readings):
    if value > 60:
        print(f"Alarm! {value} degrees at minute {minute}")
        break
