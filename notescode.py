"""
letter = input("give me a letter ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"your letter was {letter} now its {new_letter}")
"""
"""
import random
ducks = random.randint(1,10)
print(f"There are {ducks} ducks!")

percent = random.random()
better = percent * 100
print(f"your random grade is {round(better, 2)}%")
while True: """
"""
win = True
age = 35
if 18 < age:
    print("you are an adult")
prin"""
age = 10
if age >= 18 :
    print("You are an adult and can vote!")
elif age >= 15:
    print("you can Drive if you have the right paperwork.")
else:
    print("you are to young for driving")

win = False
hp = 25

if win or hp < 1:
    print("Game Over")
    if hp > 0:
        pass
    else:
        print("you lost :(")
else:
    print("game is still running.")


