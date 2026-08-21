import os
import time
# TERMINAL FUNCTIONS
def rgb(r, g, b): #function to set color. using werid string thingys that im going to ignore :)       took me way to long to get the symbols to work.
    return f"\033[38;2;{r};{g};{b}m"
def clear(): #for clearing the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
RESET = "\033[0m"
print(f" {RESET}")

print(f"{rgb(255,0,0)} wow this text is in red! {RESET}")
print(f"{rgb(255,255,0)} wow this text is in yellow! {RESET}")
print(f"{rgb(0,255,0)} wow this text is in green! {RESET}")
print(f"{rgb(0,255,255)} wow this text is in Cyan! {RESET}")
print(f"{rgb(0,0,255)} wow this text is in blue! {RESET}")
#print(f"{rgb(255, 0, 0)}Red{RESET} {rgb(0, 255, 0)}Green{RESET} {rgb(0, 0, 255)}Blue{RESET}")
#print(f"{rgb(255, 50, 150)}Custom Neon Pink{RESET}")
#print(f"{rgb(255,10,0)} custom COLOR AAAAa {RESET}")

