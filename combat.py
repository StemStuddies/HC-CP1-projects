import time
import random
def type(inn,delay = 0.1):
    for x in inn:
        print(x, end="")
        time.sleep(delay)
    print("")
type("Welcome to the battle warrior!")

name = input("what will we call you warrior?: ")

