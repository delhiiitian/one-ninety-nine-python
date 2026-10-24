"""7.7 if __name__ == "__main__": run or import?

Real-world comparison: a chef's recipe book that can also be a cooking
show. When you read it at home (import), you just get the recipes.
When it is the show itself (run directly), the chef also cooks live.
"""


def make_sandwich(filling):
    return f"Bread + {filling} + bread"


def main():
    print("Running the cooking show!")
    for filling in ["cheese", "egg", "paneer"]:
        print(make_sandwich(filling))


print("__name__ is:", __name__)

if __name__ == "__main__":
    # Only runs with: python 07_main_guard.py
    # Not when another file does: import ...
    main()
