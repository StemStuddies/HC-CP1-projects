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
t.color("black")
t.penup()
t.goto(500, -400)
t.shape("square")
t.left(90)
t.shapesize(2)
while t.ycor() <= 500:
    t.color(0,0,0)
    t.stamp()
    t.forward(40)
    t.color("grey")
    t.stamp()
    t.forward(40)
turtles[1].color("red")
turtles[5].color("blue")
turtles[4].color("green")
turtles[3].color("yellow")
turtles[2].color("orange")
turtles[6].color("purple")
for x in turtles:
    turtles[x].shape("turtle")
    turtles[x].shapesize(2)
    turtles[x].penup()
    turtles[x].goto(-500,(x*100)-300)
    turtles[x].pendown()
while True:
    turtles[random.randint(1,6)].forward(3)
    turtles[random.randint(1,6)].speed(random.randint(2,4))


