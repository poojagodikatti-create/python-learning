import random
import time

width = 60
height = 20

stars = []

for i in range(40):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    stars.append([x, y])

print("🌌 PYTHON STARFIELD 🌌")
time.sleep(1)

while True:
    print("\033[H\033[J", end="")

    screen = [[" " for _ in range(width)] for _ in range(height)]

    for star in stars:
        x, y = star

        if 0 <= y < height:
            screen[y][x] = "*"

        star[1] += 1

        if star[1] >= height:
            star[1] = 0
            star[0] = random.randint(0, width - 1)

    for row in screen:
        print("".join(row))

    time.sleep(0.1)