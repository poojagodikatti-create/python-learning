student = { 
    "name" : "Pooja",
    "course" : "BCA",
    "python": 85,
    "maths": 78,
    "computer": 92
    }

for key, value in student.items():
    print(key, ":", value)
    
marks = [85, 78, 92]

total_marks = sum(marks)
print("Total Marks:", total_marks)

avg_marks = (total_marks/300)*100
print("Average Marks:", avg_marks)
print("Highest Marks:",max(marks))
print("Lowest Marks:", min(marks))
