import random
import os
import time
# TERMINAL FUNCTIONS
def rgb(r, g, b): #function to set color. using werid string thingys that im going to ignore :)       took me way to long to get the symbols to work.
    return f"\033[38;2;{r};{g};{b}m"
def clear(): #for clearing the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
reset = "\033[0m"
print(f" {reset}")

print(f"{rgb(255,0,0)} wow this text is in red! {reset}")
print(f"{rgb(255,255,0)} wow this text is in yellow! {reset}")
print(f"{rgb(0,255,0)} wow this text is in green! {reset}")
print(f"{rgb(0,255,255)} wow this text is in Cyan! {reset}")
print(f"{rgb(0,0,255)} wow this text is in blue! {reset}")
#print(f"{rgb(255, 0, 0)}Red{RESET} {rgb(0, 255, 0)}Green{RESET} {rgb(0, 0, 255)}Blue{RESET}")
#print(f"{rgb(255, 50, 150)}Custom Neon Pink{RESET}")
#print(f"{rgb(255,10,0)} custom COLOR AAAAa {RESET}")
red = 255
green = 0
blue = 0
delay = 0.01
runpar = 0
terlimit = 100
colors = []
print("\n")
whatred = input("what color do you want to look for? red value: ")
whatgreen = input("what color do you want to look for? green value: ")
whatblue = input("what color do you want to look for? blue value: ")
print(f"{rgb(whatred,whatgreen,whatblue)} this is the color your looking for.")
time.sleep(3)
while (whatred == red and whatgreen == green and whatblue == blue) == False:
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    while colors == f"{red} {green} {blue}":
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
    print(f"{rgb(red,green,blue)}this is a random color! red = {red} green = {green} blue = {blue} {reset}")
    colors.append(f"{red} {green} {blue}")
    time.sleep(0.1)
    runpar += 1
    if runpar >= terlimit:
        clear()
        runpar = 0

print("found your color")
print(f"{rgb(red,green,blue)}this is a random color! red = {red} green = {green} blue = {blue} {reset}")




