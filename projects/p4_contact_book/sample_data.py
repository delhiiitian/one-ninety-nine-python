from contacts import add_contact, add_phone, new_book


def sample_book():
    book = new_book()
    add_contact(book, "Asha Rao", "98100 11111", "asha@example.com", {"family", "pune"}, (3, 14))
    add_contact(book, "Ben Thomas", "98200 22222", "ben@work.com", {"work"}, (10, 2))
    add_contact(book, "Chen Li", "98300 33333", "chen@example.com", {"work", "gym"}, (10, 28))
    add_contact(book, "Divya Nair", "98400 44444", "", {"family"}, None)
    add_contact(book, "Arjun Mehta", "98500 55555", "arjun@club.in", {"gym", "pune"}, (7, 9))
    add_phone(book, "asha rao", "020 2555 0000")
    return book
