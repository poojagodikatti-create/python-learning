print("🔐 PASSWORD STRENGTH CHECKER 🔐")
print("=" * 35)

password = input("Enter a password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1


print("\n🔍 Checking password...")

if score <= 2:
    print("🔴 Strength: WEAK")
elif score <= 4:
    print("🟡 Strength: MEDIUM")
else:
    print("🟢 Strength: STRONG")

print("Score:", score, "/ 5")