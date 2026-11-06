import turtle as t
import time
import random
t.forward(250)
t.left(120)
t.forward(250)
t.left(120)
t.forward(250)
for x in range(0,100):
    t.goto(random.randint(0,250),random.randint(0,250))

