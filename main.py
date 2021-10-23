import random

for i in range(100000):
    n = random.randint(0, 9)
    style = random.randint(0, 5)
    textcolor = random.randint(30, 37)
    bgcolor = random.randint(40, 47)
    print(f"\033[{style};{textcolor};{bgcolor}m{n}", end="")

