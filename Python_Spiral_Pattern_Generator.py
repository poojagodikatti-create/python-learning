import math

print("🌀 PYTHON SPIRAL GENERATOR 🌀")
print("=" * 35)

width = 60
height = 25

for y in range(height):
    line = ""

    for x in range(width):
        dx = x - width / 2
        dy = y - height / 2

        distance = math.sqrt(dx * dx + dy * dy)
        angle = math.atan2(dy, dx)

        value = int(distance + angle * 5)

        if value % 7 == 0:
            line += "█"
        else:
            line += " "

    print(line)