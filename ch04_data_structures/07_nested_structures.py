"""4.7 Nested data: lists and dictionaries inside each other.

Real-world comparison: a school. The school has classes, each class
has students, and each student has marks. Real data (like JSON from a
website) is almost always shaped like this.
"""

school = {
    "name": "Green Valley School",
    "classes": [
        {"grade": 5, "students": [
            {"name": "Asha", "marks": [88, 92, 79]},
            {"name": "Ben", "marks": [65, 70, 72]},
        ]},
        {"grade": 6, "students": [
            {"name": "Chen", "marks": [95, 98, 91]},
        ]},
    ],
}

# Reach in step by step: dict -> list -> dict -> list -> dict.
first_student = school["classes"][0]["students"][0]
print("First student:", first_student["name"])
print("Their second mark:", first_student["marks"][1])

# Loop through every level.
for cls in school["classes"]:
    print(f"Grade {cls['grade']}:")
    for student in cls["students"]:
        avg = sum(student["marks"]) / len(student["marks"])
        print(f"  {student['name']:5} average {avg:.1f}")

# Add data deep inside.
school["classes"][1]["students"].append({"name": "Divya", "marks": [80, 85, 90]})

# Real use: find the top student in the whole school.
everyone = [s for c in school["classes"] for s in c["students"]]
top = max(everyone, key=lambda s: sum(s["marks"]))
print("Top student:", top["name"])

# A grid (list of lists), like a tic-tac-toe board.
board = [["X", "O", "X"], [" ", "X", "O"], ["O", " ", "X"]]
for row in board:
    print(" | ".join(row))
