"""4.1 Lists: an ordered collection you can change.

Real-world comparison: a shopping list on the fridge. Items are in
order, you can add, cross out or change items, and the same item can
appear twice.
"""

shopping = ["milk", "eggs", "bread"]
print("List:", shopping)
print("First item:", shopping[0])
print("How many:", len(shopping))

shopping.append("butter")          # add to the end
shopping.insert(1, "coffee")       # add at position 1
print("After adding:", shopping)

shopping[0] = "oat milk"           # change an item
shopping.remove("eggs")            # remove by value
last = shopping.pop()              # remove and return the last item
print("Popped:", last)
print("Now:", shopping)

print("Is bread on the list?", "bread" in shopping)
print("Position of bread:", shopping.index("bread"))

# Lists can hold any type, even other lists.
mixed = [1, "two", 3.0, True, [5, 6]]
print("Mixed list:", mixed)

# Real use: track daily step counts and get stats.
steps = [8200, 10450, 6700, 12000, 9100]
steps.append(11300)
print(f"Days: {len(steps)}, total: {sum(steps)}, best: {max(steps)}")
print(f"Average: {sum(steps) / len(steps):.0f} steps a day")
