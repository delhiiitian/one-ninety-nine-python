# Project 5: ATM Simulator

Chapter 5 project of **Python in 199 Pages**. A cash machine where every way things
can go wrong (wrong PIN, blocked card, not enough money, daily limit, ATM out of cash)
is its own exception, handled without ever crashing.

## Layout

```
p5_atm_simulator/
├── errors.py   # the exception family (ATMError and its children)
├── atm.py      # Account and ATM classes: rules, notes, logging
├── main.py     # the screen: menus, input, friendly messages
└── tests/
    └── test_atm.py
```

## Run it

```bash
python main.py
```

Demo cards: `1111` with PIN `1234` (Asha, Rs 15,000) and `2222` with PIN `4321` (Ben, Rs 3,000).
Every action is logged to `atm.log`.

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Save balances to a JSON file between runs (Chapter 6).
- Add a "change PIN" option that validates the new PIN.
