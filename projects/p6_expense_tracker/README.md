# Project 6: Expense Tracker

Chapter 6 project of **Python in 199 Pages**. A command-line tool that stores every
expense in a CSV file you can also open in Excel, prints monthly reports with bar
charts, warns when you go over budget, and exports to JSON.

## Layout

```
p6_expense_tracker/
├── data/
│   └── expenses.csv   # sample data (your own entries are added here)
├── storage.py         # the ONLY code that reads or writes files
├── reports.py         # summaries and budget checks, no file access
├── tracker.py         # argparse commands: add, list, report, export
└── tests/
    └── test_tracker.py
```

## Run it

```bash
python tracker.py report 2026-10 --budget groceries=5000
python tracker.py add 450 food "Pizza night"
python tracker.py list --last 5
python tracker.py export expenses.json
python tracker.py --help
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

Tests write to a temporary folder, so your real `expenses.csv` is never touched.

## Ideas to extend

- Add a `delete` command.
- Read budgets from a `budgets.json` file.
- Draw a real chart with matplotlib (`pip install matplotlib`).
