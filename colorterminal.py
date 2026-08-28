import os
# TERMINAL FUNCTIONS
def rgb(red, green, blue): #function to set color. using werid string thingys that im going to ignore :)       took me way to long to get the symbols to work.
    """
keyword to change color of the text in the terminal 
using red green blue values 0 to 255. 
has to be used inside f string when using print!
reset can also be used in an fsting to reset color.
ex f"{rgb(255,0,0)} this text is in red! {reset}"
    """
    return f"\033[38;2;{red};{green};{blue}m"
def clear(): #for clearing the terminal
    """
for clearing the terminal
    """
    os.system('cls' if os.name == 'nt' else 'clear')
reset = "\033[0m"
print(f" {reset}")

#print(f"{rgb(255, 0, 0)}Red{RESET} {rgb(0, 255, 0)}Green{RESET} {rgb(0, 0, 255)}Blue{RESET}")
#print(f"{rgb(255, 50, 150)}Custom Neon Pink{RESET}")
#print(f"{rgb(255,10,0)} custom COLOR AAAAa {RESET}")

