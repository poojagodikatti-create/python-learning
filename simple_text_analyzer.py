text = input("Enter a sentence: ")

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Number of characters:", len(text))

if "python" in text.lower():
    print("Python is present!")
else:
    print("Python is not present!")