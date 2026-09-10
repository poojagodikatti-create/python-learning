print("🕵️ PYTHON SECRET DETECTIVE")
print("=" * 35)

suspects = {
    "Alex": {"age": 20, "color": "red", "pet": "dog"},
    "Sam": {"age": 22, "color": "blue", "pet": "cat"},
    "Jordan": {"age": 21, "color": "green", "pet": "dog"},
    "Taylor": {"age": 22, "color": "red", "pet": "cat"}
}

print("\n🔎 CLUES:")
print("1. The person is 22 years old.")
print("2. Their favorite color is blue.")
print("3. They have a cat.")

print("\n🧠 Investigating...")

for name, details in suspects.items():
    if (
        details["age"] == 22
        and details["color"] == "blue"
        and details["pet"] == "cat"
    ):
        print("\n🚨 MYSTERY SOLVED!")
        print("🎯 Suspect:", name)