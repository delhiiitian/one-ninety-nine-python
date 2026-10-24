"""An in-memory contact book built from dicts, lists, sets and tuples.

Shape of the data:
    book = {
        "asha rao": {                       # dict key: lower-case name
            "name": "Asha Rao",             # str
            "phones": ["98100 11111"],      # list: order matters, repeats allowed
            "email": "asha@example.com",
            "tags": {"family", "pune"},     # set: unique labels
            "birthday": (3, 14),            # tuple: (month, day), never changes
        },
    }
"""

from collections import Counter


def new_book():
    return {}


def _key(name):
    return " ".join(name.lower().split())


def add_contact(book, name, phone, email="", tags=(), birthday=None):
    key = _key(name)
    if key in book:
        raise ValueError(f"{name} already exists")
    book[key] = {
        "name": name.strip(),
        "phones": [phone],
        "email": email,
        "tags": set(tags),
        "birthday": birthday,
    }
    return book[key]


def add_phone(book, name, phone):
    contact = get_contact(book, name)
    if phone not in contact["phones"]:
        contact["phones"].append(phone)
    return contact


def get_contact(book, name):
    try:
        return book[_key(name)]
    except KeyError:
        raise KeyError(f"no contact called {name!r}") from None


def delete_contact(book, name):
    return book.pop(_key(name))


def search(book, text):
    """Match part of a name, a phone number or an email."""
    text = text.lower()
    digits = "".join(ch for ch in text if ch.isdigit())
    found = []
    for contact in book.values():
        phones = ["".join(ch for ch in p if ch.isdigit()) for p in contact["phones"]]
        if (text in contact["name"].lower()
                or text in contact["email"].lower()
                or (digits and any(digits in p for p in phones))):
            found.append(contact)
    return sorted(found, key=lambda c: c["name"])


def by_tag(book, tag):
    return sorted((c for c in book.values() if tag in c["tags"]), key=lambda c: c["name"])


def all_tags(book):
    tags = set()
    for contact in book.values():
        tags |= contact["tags"]
    return sorted(tags)


def tag_counts(book):
    return Counter(tag for c in book.values() for tag in c["tags"])


def birthdays_in(book, month):
    people = [(c["birthday"][1], c["name"]) for c in book.values()
              if c["birthday"] and c["birthday"][0] == month]
    return [name for day, name in sorted(people)]


def grouped_by_letter(book):
    groups = {}
    for contact in sorted(book.values(), key=lambda c: c["name"]):
        groups.setdefault(contact["name"][0].upper(), []).append(contact["name"])
    return groups


def format_contact(contact):
    tags = ", ".join(sorted(contact["tags"])) or "-"
    phones = ", ".join(contact["phones"])
    return f"{contact['name']:<14} {phones:<28} {contact['email'] or '-':<22} [{tags}]"
