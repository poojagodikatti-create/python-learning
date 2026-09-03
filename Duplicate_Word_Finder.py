print("🔍 DUPLICATE WORD FINDER")
print("=" * 35)

text = input("Enter a sentence: ")

words = text.lower().split()

duplicates = []

for word in words:
    if words.count(word) > 1 and word not in duplicates:
        duplicates.append(word)

print("\n📊 RESULT")
print("=" * 35)

if duplicates:
    print("🔁 Duplicate words:")
    
    for word in duplicates:
        print("👉", word, "-", words.count(word), "times")
else:
    print("✅ No duplicate words found!")

print("=" * 35)