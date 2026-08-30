num_students = int(input("Enter numbers of students:"))
attendance = {}

for i in range(num_students):
    name = input(f"\nEnter name of student{i+1}:")
    status = input(f"Is {name} present?(yes/no):").strip().lower()
    
    if status == "yes":
        attendance[name] = "Present"
    elif status == "no":
        attendance[name] = "Absent"
    else:
        print("\n Invalid input.Making a Absent by default")
        attendance[name] = "Absent"
        
print("\n-----Attendance Record-----")

for student,status in attendance.items():
    print(f"{student}:{status}")