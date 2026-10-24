"""4.4 Dictionaries: look things up by key.

Real-world comparison: a phone contact list. You look up a NAME
(the key) to find a NUMBER (the value). You never search by position.
"""

contacts = {"Mom": "98100 11111", "Office": "022 4000 0000"}
print("Mom's number:", contacts["Mom"])

contacts["Doctor"] = "98200 22222"        # add
contacts["Office"] = "022 4000 1234"      # update
del contacts["Doctor"]                    # delete
print("Contacts:", contacts)

# get() avoids an error when the key is missing.
print("Plumber:", contacts.get("Plumber", "not saved"))

# Looping over keys and values.
for name, number in contacts.items():
    print(f"{name:7} {number}")

print("Keys:", list(contacts.keys()))
print("Values:", list(contacts.values()))
print("Has Mom?", "Mom" in contacts)

# Real use: count how often each word appears.
text = "the cat sat on the mat the end"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print("Word counts:", counts)

# A dictionary that describes one thing (like a JSON record).
user = {"id": 7, "name": "Priya", "skills": ["python", "sql"], "active": True}
print(f"{user['name']} knows {', '.join(user['skills'])}")
