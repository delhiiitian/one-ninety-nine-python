"""6.9 Command-line arguments with argparse.

Real-world comparison: ordering at a drive-through. You say
everything in one go: "a large coffee, no sugar". Command-line
arguments let people tell your script what to do when they start it:
    python 09_command_line_args.py Asha --times 3 --shout
"""

import argparse
import sys

parser = argparse.ArgumentParser(description="Greet someone from the terminal.")
parser.add_argument("name", nargs="?", default="World", help="who to greet")
parser.add_argument("--times", type=int, default=1, help="how many greetings")
parser.add_argument("--shout", action="store_true", help="use capital letters")

args = parser.parse_args()

print("Raw arguments in sys.argv:", sys.argv[1:])
message = f"Hello, {args.name}!"
if args.shout:
    message = message.upper()
for _ in range(args.times):
    print(message)

# argparse also gives you --help for free:
#   python 09_command_line_args.py --help
