import colorterminal as color
#hunter card password strength checker
print("~~~~~~~~PASSWORD STRENGTH CHECKER~~~~~~~~")
password = input("Password to test?: ")
strength = 0
tests = [0,0,0,0]
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
        strength +=
