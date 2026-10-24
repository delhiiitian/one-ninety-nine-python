# Project 1: Bill Splitter

Chapter 1 project of **Python in 199 Pages**. Type in what your group ordered,
and the program prints a neat receipt with GST, tip, and how much each person pays.

## Layout

```
p1_bill_splitter/
├── bill.py        # all the maths and the receipt text (no input/print)
├── main.py        # talks to the user: asks for items, prints the receipt
└── tests/
    └── test_bill.py
```

## Run it

```bash
python main.py
```

Example session:

```
item> Masala dosa, 120, 2
item> Filter coffee, 40, 3
item>
Tip percent [10]: 10
Number of people [2]: 4
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Let each person pay for only what they ate.
- Save every receipt to a text file (Chapter 6).
- Support different tax rates per item.
