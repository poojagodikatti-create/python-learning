try:
    age = int(input("Enter yourage: "))
except ValueError:
    print("Please enter a number.")
else:
    print("You age is", age)
finally:
    print("This block is always run (cleanup).")