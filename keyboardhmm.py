import keyboard
import time
import turtle

while True:
    if keyboard.is_pressed('up'):
        turtle.left(10)
    if keyboard.is_pressed('down'):
        turtle.right(10)
    if keyboard.is_pressed('right'):
        turtle.forward(10)
    turtle.pendown()
