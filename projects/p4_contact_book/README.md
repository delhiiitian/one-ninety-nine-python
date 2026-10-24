# Project 4: Contact Book

Chapter 4 project of **Python in 199 Pages**. A command-driven contact book that
shows each core data structure doing the job it is best at.

| Structure | Used for |
| --- | --- |
| `dict` | the book itself (name -> contact) and each contact record |
| `list` | a contact's phone numbers, search results |
| `set` | tags such as `family` or `gym` |
| `tuple` | a birthday `(month, day)` |
| `Counter` | how often each tag is used |

## Layout

```
p4_contact_book/
├── contacts.py      # all operations on the book
├── sample_data.py   # five example contacts
├── main.py          # the command loop
└── tests/
    └── test_contacts.py
```

## Run it

```bash
python main.py
contacts> list
contacts> find ar
contacts> tag work
contacts> birthdays 10
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Save the book to JSON so contacts survive a restart (Chapter 6).
- Import contacts from a CSV export of your phone.
