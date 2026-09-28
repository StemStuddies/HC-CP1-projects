while True:
    try:
        grade = int(input("what is your grade percentage? "))
    except:
        print("thats not a number")
    else:
        if 0.00 <= grade <= 100.00:
            break
        else:
            print("thats not in a acceptable range")
grades = []
while True:
    round(grade, 2)
    if grades > 94:
        grades.append("A")
    elif grades > 90:
        grades.append("A-")
    elif grades > 