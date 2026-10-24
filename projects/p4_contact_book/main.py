"""Contact Book: add, find, tag and group your contacts.

Run:  python main.py
Starts with a few sample contacts so there is something to explore.
"""

from contacts import (add_contact, all_tags, birthdays_in, by_tag, delete_contact,
                      format_contact, get_contact, grouped_by_letter, search, tag_counts)
from sample_data import sample_book

HELP = """Commands:
  list                 show everyone, grouped by first letter
  find <text>          search names, phones and emails
  add                  add a new contact
  tag <tag>            show contacts with a tag
  tags                 show all tags and how often they are used
  birthdays <month>    birthdays in a month (1-12)
  delete <name>        remove a contact
  help | quit"""


def show(contacts):
    if not contacts:
        print("  (nobody)")
    for contact in contacts:
        print("  " + format_contact(contact))


def run(book, ask=input):
    print(HELP)
    while True:
        command, _, arg = ask("\ncontacts> ").strip().partition(" ")
        command = command.lower()
        if command == "quit":
            break
        elif command == "list":
            for letter, names in grouped_by_letter(book).items():
                print(f"{letter}:")
                show([get_contact(book, n) for n in names])
        elif command == "find":
            show(search(book, arg))
        elif command == "tag":
            show(by_tag(book, arg.lower()))
        elif command == "tags":
            for tag, count in tag_counts(book).most_common():
                print(f"  {tag:<8} {count}")
        elif command == "birthdays" and arg.isdigit():
            print("  " + (", ".join(birthdays_in(book, int(arg))) or "(none)"))
        elif command == "add":
            name = ask("  Name: ")
            phone = ask("  Phone: ")
            email = ask("  Email (optional): ")
            tags = {t.strip().lower() for t in ask("  Tags, comma separated: ").split(",") if t.strip()}
            try:
                show([add_contact(book, name, phone, email, tags)])
            except ValueError as error:
                print("  ", error)
        elif command == "delete":
            try:
                print("  Deleted", delete_contact(book, arg)["name"])
            except KeyError:
                print("  No such contact")
        else:
            print(HELP)
    print(f"Goodbye! {len(book)} contacts, tags in use: {', '.join(all_tags(book))}")


if __name__ == "__main__":
    run(sample_book())
