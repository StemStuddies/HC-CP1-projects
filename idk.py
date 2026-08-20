import time
import turtle
import random
turt = {
    1: turtle.Turtle(),
    2: turtle.Turtle(),
    3: turtle.Turtle(),
    4: turtle.Turtle(),
}
while True:
    for y in turt:
        turt[y].forward(random.randint(0,50))
        turt[y].right(random.randint(-180,180))


