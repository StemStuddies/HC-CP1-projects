"""
letter = input("give me a letter ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"your letter was {letter} now its {new_letter}")
"""
import random
ducks = random.randint(1,10)
print(f"There are {ducks} ducks!")

percent = random.random()
better = percent * 100
print(f"your random grade is {round(better, 2)}%")
while True:
    