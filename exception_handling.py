try:
    num = int(input("Enter the number:"))
    result = 10/num
except ValidError:
    print("Error:please enter valid niteger")
except ZeroDevisionError:
    print("Error:Division by zero is not valid")
else:
    print("Success!The result:", result)
finally:
    print("This block always run(clean up)")