"""4.9 Choosing the right structure: stacks, queues and more.

Real-world comparison: a stack of plates (last in, first out) and a
queue at a ticket counter (first in, first out). Choosing the right
container makes the job easy, just like choosing a bag, a box or a
filing cabinet.
"""

from collections import Counter, deque

# Stack: undo history in a text editor. A list works well.
undo_stack = []
for action in ["type 'Hi'", "bold", "type '!'"]:
    undo_stack.append(action)
print("Undo:", undo_stack.pop())
print("Undo:", undo_stack.pop())
print("Left on the stack:", undo_stack)

# Queue: customers served in order. deque is fast at both ends.
counter = deque(["Asha", "Ben"])
counter.append("Chen")            # join the back
served = counter.popleft()        # serve the front
print("Served:", served, "| Waiting:", list(counter))

# Counter: tally things quickly.
votes = ["tea", "coffee", "tea", "juice", "tea", "coffee"]
tally = Counter(votes)
print("Votes:", dict(tally))
print("Winner:", tally.most_common(1)[0])

# Quick guide:
guide = [
    ("list", "ordered, changeable", "to-do items, scores"),
    ("tuple", "ordered, fixed", "coordinates, dates"),
    ("dict", "key -> value lookup", "contacts, settings"),
    ("set", "unique, fast 'in' check", "tags, visited pages"),
    ("deque", "fast add/remove at ends", "queues, recent history"),
]
for name, trait, example in guide:
    print(f"{name:6} {trait:26} e.g. {example}")
