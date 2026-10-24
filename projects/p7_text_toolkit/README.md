# Project 7: textkit, a Text Analysis Toolkit

Chapter 7 project of **Python in 199 Pages**. A real, installable Python package
with modules, a command-line interface, a `pyproject.toml` and a test suite.
It counts words and sentences, finds the most common words, estimates reading
time and scores readability.

## Layout

```
p7_text_toolkit/
├── pyproject.toml        # package name, version, the `textkit` command
├── sample.txt
├── textkit/              # the package
│   ├── __init__.py       # public API and version
│   ├── __main__.py       # CLI: python -m textkit ...
│   ├── clean.py          # whitespace, punctuation, slugs
│   ├── stats.py          # words, sentences, top words
│   └── readability.py    # reading time, Flesch score
└── tests/
    └── test_textkit.py
```

## Run it

```bash
python -m textkit report sample.txt
python -m textkit top sample.txt -n 5
python -m textkit slug "My First Blog Post!"
```

## Install it as a command

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
textkit report sample.txt
```

## Test it

```bash
python -m unittest discover -s tests -t . -v
```

## Ideas to extend

- Add a `compare` command that shows which of two files is easier to read.
- Publish it to TestPyPI with `python -m build` and `twine upload`.
