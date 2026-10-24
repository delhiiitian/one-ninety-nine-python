"""Command-line entry point.

    python -m textkit report sample.txt
    python -m textkit top sample.txt -n 10
    python -m textkit slug "My Blog Post Title!"
    echo "some text" | python -m textkit report -
"""

import argparse
import sys
from pathlib import Path

from . import __version__
from .readability import describe, flesch_reading_ease, reading_time_minutes
from .clean import slugify
from .stats import sentence_count, top_words, word_count


def read_source(source: str) -> str:
    if source == "-":
        return sys.stdin.read()
    return Path(source).read_text(encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="textkit", description="Analyse plain text.")
    parser.add_argument("--version", action="version", version=f"textkit {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    report = sub.add_parser("report", help="words, sentences, reading time, readability")
    report.add_argument("source", help="a file path, or - for standard input")

    top = sub.add_parser("top", help="most common words")
    top.add_argument("source")
    top.add_argument("-n", type=int, default=5)

    slug = sub.add_parser("slug", help="turn a title into a URL slug")
    slug.add_argument("title")

    args = parser.parse_args(argv)

    if args.command == "slug":
        print(slugify(args.title))
        return 0

    try:
        text = read_source(args.source)
    except FileNotFoundError:
        print(f"textkit: no such file: {args.source}", file=sys.stderr)
        return 1

    if args.command == "report":
        score = flesch_reading_ease(text)
        print(f"Words:        {word_count(text)}")
        print(f"Sentences:    {sentence_count(text)}")
        print(f"Reading time: {reading_time_minutes(text)} min")
        print(f"Readability:  {score} ({describe(score)})")
    else:
        for word, count in top_words(text, args.n):
            print(f"{word:<15}{count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
