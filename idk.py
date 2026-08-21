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
while True:
    for y in turt:
        turt[1].forward(random.randint(0,80))
        turt[1].right(random.randint(-180,180))



