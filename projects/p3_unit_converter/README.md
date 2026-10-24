# Project 3: Unit Converter

Chapter 3 project of **Python in 199 Pages**. Convert length, weight, volume and
temperature from a menu, or in one line from the terminal.

## Layout

```
p3_unit_converter/
├── conversions.py   # small pure functions + unit tables
├── main.py          # menu and command-line entry point
└── tests/
    └── test_conversions.py
```

## Run it

```bash
python main.py                    # menu
python main.py length 5 km mile   # one-liner
python main.py temperature 98.6 f c
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Add a currency category with rates read from a JSON file (Chapter 6).
- Add area (square metres, acres, hectares).
