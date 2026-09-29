# hunter what is my grade 
grades = []
while True:
    try:
        amount = int(input("how many grades do you want: "))
    except:
        print("thats not a number")
    else:
        if 0 < amount <= 12:
            break
        else:
            print("thats not in the acceptable range! has to be 1 to 12") 
for x in range(0, amount):
    while True:
        try:
            grade = float(input("what is your grade percentage? "))
        except:
            print("thats not a number")
        else:
            if 0.00 <= grade <= 100.00:
                break
            else:
                print("thats not in a acceptable range")
    round(grade, 2)
    if grade >= 94:
        grades.append("A ") #yes I know. do not comment on this long conditional.
    elif grade >= 90:
        grades.append("A-")
    elif grade >= 87:
        grades.append("B+")
    elif grade >= 84:
        grades.append("B ")
    elif grade >= 80:
        grades.append("B-")
    elif grade >= 77:
        grades.append("C+")
    elif grade >= 74:
        grades.append("C ")
    elif grade >= 70:
        grades.append("C-")
    elif grade >= 67: 
        grades.append("D+")
    elif grade >= 64:
        grades.append("D ")
    elif grade >= 60:
        grades.append("D-")
    elif grade >= 0:
        grades.append("F ")
print(f"------you're-Grades------")
print(*grades)
