Name = input("Enter your name: ")
clg = input("Enter your callege Name: ")
cors = input("Enter your course: ")
gole = input("Enter your Gole: ")
call = (input("Enter mobile No.: "))
language = input("Enter you programming language:")
daily_hourse = float(input("Enter your daily leaning hourse: "))
monthly_hourse = daily_hourse * 30
four_month = daily_hourse * 30 * 4
already_study = float(input( "How many hourse are you read?: "))
reamining_hourse = four_month - already_study
year = int(input("Enter your birth year:"))
current_year = 2026

print("*" * 30)
print("Name = ", Name)
print("College = ", clg)
print("Course = ", cors)
print("Gole = ", gole)
print("Call.No:. ", call)
print("Language:", language)
print("Reading Hourse:", monthly_hourse)
print("4 month = ", four_month)
print("Already studied", already_study)
print("Reamining:", reamining_hourse)
print("Your age is:", current_year - year)
print("*" * 30)