# Project 8: Library Manager

Chapter 8 project of **Python in 199 Pages**. A library system for books, e-books
and other items that uses the features that make Python special: classes,
inheritance, dataclasses, dunder methods, properties, generators, a decorator and a
context manager.

## Layout

```
p8_library_manager/
├── library/
│   ├── __init__.py   # public API
│   ├── errors.py     # LibraryError family
│   ├── items.py      # Item -> Book -> EBook, and Member (dataclasses)
│   └── catalog.py    # Library: lending, search, reports
├── demo.py           # a scripted day at the library
└── tests/
    └── test_library.py
```

## Run it

```bash
python demo.py
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Add a `DVD` subclass with a 3-day loan and a higher late fee.
- Save the catalogue to SQLite (Chapter 9).
- Add a waiting list (a `deque`) for items with no copies left.
