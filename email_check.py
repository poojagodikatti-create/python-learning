import re

email = input("Enter your email address:")
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern,email):
    print("valid Address")
else:
    print("Invalid Address")