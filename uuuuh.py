import random
import time
while True:
    char = chr(random.randint(0,127))
    print(f"{char}", end="")
    time.sleep(0.01)
for x in range(0,1000):
    print(2**x)
    time.sleep(0.05)