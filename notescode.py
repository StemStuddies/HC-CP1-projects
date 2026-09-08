letter = input("give me a letter ")
letter = letter[0].lower()
number_value = ord(letter)
number_value += 2
new_letter = chr(number_value)
print(f"your letter was {letter} now its {new_letter}")