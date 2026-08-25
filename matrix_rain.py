import random
import time
import os

characters = "01"

try:
    while True:
        line = ""

        for i in range(60):
            line += random.choice(characters)

        print(line)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\n\n🛑 Matrix stopped!")