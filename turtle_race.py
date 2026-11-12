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

def fin_line (inx, ofset):
    t.penup()
    t.goto(inx, -500)
    t.shape("square")
    t.setheading(90)
    t.shapesize(2)
    t.forward(ofset)
    while t.ycor() <= 500:
        t.color(0.1,0.1,0.1)
        t.stamp()
        t.forward(40)
        t.color(0.9,0.9,0.9)
        t.stamp()
        t.forward(40)

def turtle(turt):
    for ye in range(0,6):
        if turt 

t.bgcolor(0,0,0)
t.color("black")
fin_line(500,0)
fin_line(540, 40)
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
    for x in range(0,6):
        if turtles[x]


