import colorterminal as color
#hunter card password strength checker
print("~~~~~~~~~~~~~PASSWORD STRENGTH CHECKER~~~~~~~~~~~~~")
password = input("Password to test?: ")
strength = 0
tests = [0,0,0,0,0]
specialchar = ["~","`","!","@","#","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|",";",":","'",",","<",">",".","?","/"]
if len(password) > 7:
    strength += 1
    tests[1] = 1
for digit in password:
    if digit == digit.upper():
        strength += 1
        tests[2] = 1
for digit in password:
    if digit == digit.lower():
        strength += 1
        tests[3] = 1
for digit in password:
    if digit == int(digit):
        strength += 1
        tests[4] = 1
for digit in password:
    if digit in specialchar:
        strength += 1
        tests[5] = 1
if strength == 1:
    print("Your password is Weak")
elif strength == 2: 
    print("Your password is Kinda Weak")
elif strength == 3: 
    print("Your password is Kinda Strong")
elif strength == 4: 
    print("Your password is Strong")
elif strength == 2: 
    print("Your password is Super Strong")
print("\n ~~~~~~~~~~~~~TIPS~~~~~~~~~~~~~")
print("to make it more strong try adding....")
if tests[2] == 0 or tests[3] == 0:
    print("a combination of Uppercase and Lowercase letters.    to make it more strong")

