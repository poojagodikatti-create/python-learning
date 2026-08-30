print("🧠 TEXT ANALYZER")
print("=" * 35)

text = input("Enter your text: ")

characters = len(text)
words = len(text.split())

vowels = 0
digits = 0
uppercase = 0
lowercase = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1

    if char.isdigit():
        digits += 1

    if char.isupper():
        uppercase += 1

    if char.islower():
        lowercase += 1

print("\n📊 RESULTS")
print("=" * 35)

print("🔤 Characters:", characters)
print("📝 Words:", words)
print("🗣️ Vowels:", vowels)
print("🔢 Digits:", digits)
print("🔠 Uppercase:", uppercase)
print("🔡 Lowercase:", lowercase)

print("=" * 35)
print("🐍 Day 27/100 COMPLETE!")