#hunter card, turtle race

import turtle as t
import random

turtles = {
    1: t.Turtle(),
    2: t.Turtle(),
    3: t.Turtle(),
    4: t.Turtle(),
    5: t.Turtle(),
    6: t.Turtle()
}
turtles[1].color("red")
turtles[2].color("blue")
turtles[3].color("green")
turtles[4].color("yellow")
turtles[5].color("orange")
turtles[6].color("purple")
for x in turtles:
    turtles[x].shape("turtle")
    turtles[x].shapesize(2)
    turtles[x].penup()
    turtles[x].goto(-500,(x*100)-300)
    turtles[x].pendown()
while True:
    turtles[random.randint(1,6)].forward(2)
