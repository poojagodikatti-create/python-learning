import time

print("⌨️ PYTHON TYPING SPEED TEST")
print("=" * 35)

text = "Python makes learning programming fun"

print("\nType this sentence:")
print(text)

input("\nPress Enter when you are ready...")

start = time.time()

user_text = input("\nType here: ")

end = time.time()

time_taken = end - start

words = len(user_text.split())
speed = words / (time_taken / 60)

print("\n" + "=" * 35)
print("⏱️ Time:", round(time_taken, 2), "seconds")
print("📝 Words:", words)
print("⚡ Speed:", round(speed, 2), "WPM")

if user_text == text:
    print("🎯 Accuracy: 100%")
else:
    print("❌ Accuracy: Not 100%")

print("=" * 35)
print("🐍 Day 25/100 COMPLETE!")