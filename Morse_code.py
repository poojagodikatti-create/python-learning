morse = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

reverse_morse = {value: key for key, value in morse.items()}

print("🔐 MORSE CODE TRANSLATOR")
print("=" * 35)

message = input("Enter your message: ")

result = []

for char in message.upper():
    if char == " ":
        result.append("/")
    elif char in morse:
        result.append(morse[char])

print("\n📡 Morse Code:")
print(" ".join(result))

# Decode it again
decoded = []

for code in result:
    if code == "/":
        decoded.append(" ")
    elif code in reverse_morse:
        decoded.append(reverse_morse[code])

print("\n🔓 Decoded:")
print("".join(decoded))