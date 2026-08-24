import time
import turtle
import random
turt = {
    1: turtle.Turtle(),
    2: turtle.Turtle(),
    3: turtle.Turtle(),
    4: turtle.Turtle(),
    5: turtle.Turtle(),
    6: turtle.Turtle(),
    7: turtle.Turtle(),
    8: turtle.Turtle(),
    9: turtle.Turtle(),
    10: turtle.Turtle(),
}
for y in turt:
    turt[y].forward(random.randint(0,80))
    turt[y].right(random.randint(-180,180))
while True:
        turt[random.randint(1,10)].forward(random.randint(0,80))
        turt[random.randint(1,10)].right(random.randint(-180,180))



