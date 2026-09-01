#hunter card, average grade
while True:
    try:
        classes = int(input("how many classes do you have? \n")) #asking how many classes you have
    except:
        print("thats not a number")
    else:
        break
grades = [] #used for a list of grades
for clas in range(classes): #loops for how many classes you have
    while True: #testing for errors so and if they dont enter in a number it will ask again/
        try:
            grades.append(int(input(f"Whats youre grade in your {clas + 1} periode: "))) #addes grades to a list
        except:
            print("thats not a number")
        else:
            break    
print("\n") #new line added for neatness.
print(f"your average grade is {round(sum(grades)/classes, 2)} %") #calculates and prints the average grade.


    