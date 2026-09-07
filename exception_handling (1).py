try:
    n = int(input("Enter a number: "))
    n1 = int(input("Enter a number:"))
    print(n / n1)
except ValueError:
    print("Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")