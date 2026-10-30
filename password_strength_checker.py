#hunter card password strength checker

import os

print("~~~~~~~~~~~~~PASSWORD STRENGTH CHECKER~~~~~~~~~~~~~")
password = input("Password to test?: ")

strength = 0
tests = [0,0,0,0,0]
specialchar = ["~","`","!","@","#","#","$","%","^","&","*","(",")","-","_","+","=","{","}","[","]","|",";",":","'",",","<",">",".","?","/"]

if len(password) > 7: #testing if password length is greater then 7
    strength += 1
    tests[0] = 1
for digit in password: #testing for uppercase
    if digit.isupper():
        strength += 1
        tests[1] = 1
        break
for digit in password: #testing for lowercase 
    if digit.islower():
        strength += 1
        tests[2] = 1
        break
for digit in password: #testing for numbers in password
    if digit.isnumeric(): #<-- this keyword we literly learned as a class so dont flag this
        strength += 1
        tests[3] = 1
        break
for digit in password:  #testing if there is any special charecters in password.
    if digit in specialchar: 
        strength += 1
        tests[4] = 1
        break

if strength == 1: #telling user how strong there password is.
    print("Your password is Weak")
elif strength == 2: 
    print("Your password is Kinda Weak")
elif strength == 3: 
    print("Your password is Kinda Strong")
elif strength == 4: 
    print("Your password is Strong")
elif strength == 5: 
    print("Your password is Super Strong")


print("\n ~~~~~~~~~~~~~TIPS~~~~~~~~~~~~~") #tips menu showing what user sould add to there password
print("To make you're password more strong. \ntry adding... ")
if tests[1] == 0 or tests[2] == 0:
    print(" A combination of Uppercase and Lowercase letters. ")
if tests[0] == 0:
    print(" At least 8 digits or longer. ")
if tests[3] == 0:
    print(" Numbers to your password. ")
if tests[4] == 0:
    print(" special charecters to your password. ")
if all(tests) == 1: #tests for every value at once
    print(" nothing your password looks great!")

