import keyboard
import time

while True:
    if keyboard.is_pressed('a'):
        print("you pressed the letter a")
        time.sleep(0.1)
