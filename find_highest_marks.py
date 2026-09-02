students = [
    {"name": "Pooja", "marks": 85},
    {"name": "Ankita", "marks": 90},
    {"name": "Rahul", "marks": 75}
]

for student in students:
    print(student["name"], "scored", student["marks"])
    
highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("Highest marks:", highest["marks"])
print("Student name:", highest["name"])