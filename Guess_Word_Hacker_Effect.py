import random
import string
import time

secret = "PYTHON"

print("💻 SYSTEM STARTING...")
time.sleep(1)

print("🔐 SECRET WORD: ******")
print("⚡ CRACKING PASSWORD...\n")

for correct in range(len(secret)):
    while True:
        guess = random.choice(string.ascii_uppercase)

        print("Trying:", guess, end="\r")
        time.sleep(0.03)

        if guess == secret[correct]:
            print("Found:", guess, "✅")
            break

print("\n🔓 SECRET WORD CRACKED!")
print("🎯 WORD:", secret)
print("🐍 Python wins!")