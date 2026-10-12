#hunter card escape room
import random
import time
codes = ("THISISTHECODE") 
code = "abcdefghijklmnopqrstuvwxyz"
chiper = ""
shift = random.randint(1,26)
guess = 1
count = 0

shift = 2

for x in code:
    chiper += chr(ord(x)+shift % 26 - 1)
print(chiper)


print("you are trapped in a dark room theres a door leading out, but you need a code. \n the code is a random chipher you need to convert it back to the code.")
while code != guess:
    guess = input("whats the code? ")
    if guess == code:
        print("------ACESS-GRANTED------")
    else:
        print("------ACESS-DENIED-------")
        count += 1
        print(f"secret chipher{chiper}")
    
print("\n \n YOU ESCAPED GOOD JOB \n")
