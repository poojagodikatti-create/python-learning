import random
import time

print("🎵 PYTHON BEAT VISUALIZER 🎵")
print("=" * 35)

bars = 8

for i in range(60):
    print("\033[H\033[J", end="")

    print("🎵 BEAT VISUALIZER 🎵\n")

    for j in range(bars):
        height = random.randint(1, 15)
        print("█" * height)

    print("\n🔥 DAY 30/100 🔥")

    time.sleep(0.15)