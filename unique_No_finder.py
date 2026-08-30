numbers = set()

def num(n):
    numbers.add(n)

num(10)
num(20)
num(30)
num(20)
num(10)

print("Unique numbers:", numbers)

if 30 in numbers:
    print("Found")
else:
    print("Not found")