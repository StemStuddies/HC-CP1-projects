#hunter card escape room
import random
import time
import os
codes = ("THISISTHECODE") 
code = "wowzania"
chiper = ""
shift = random.randint(1,26)
guess = 1
count = 0

for x in code:
    shifted = ord(x) + shift
    chiper += chr( shifted % 26 + 65)
print(chiper)


print("you are trapped in a dark room theres a door leading out, but you need a code. \n the code is a random chipher you need to convert it back to the code.")
while code != guess or count >= 6:
    if count == 3:
        print(f"you have 3 guesses left!!! heres a hint \n the chipher is shifted by {shift}")
        time.sleep(1)
    guess = input("whats the code? ").lower()
    if guess == code:
        print("------ACESS-GRANTED------")
    else:
        print("------ACESS-DENIED-------")
        count += 1
        print(f"secret chipher {chiper}")
    
    
print("\n \n YOU ESCAPED GOOD JOB \n")
