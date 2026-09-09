class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

    def introduction(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)

student1 = Student("Pooja", "BCA", 85)
student1.introduction()