students = [
    {"name": "Pooja", "marks": 85},
    {"name": "Ankita", "marks": 90},
    {"name": "Rahul", "marks": 75}
]

for student in students:
    print(student["name"], "scored", student["marks"])

highest = students[0]
lowest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

    if student["marks"] < lowest["marks"]:
        lowest = student

marks = []

for student in students:
    marks.append(student["marks"])

average = sum(marks) / len(marks)

print("Highest:", highest["name"], "-", highest["marks"])
print("Lowest:", lowest["name"], "-", lowest["marks"])
print("Average:", average)