#hunter card, average grade

classes = int(input("how many classes do you have? \n")) #asking how many classes you have
grades = [] #used for a list of grades
for clas in range(classes): #loops for how many classes you have
    grades.append(int(input(f"Whats youre grade in your {clas + 1} periode: "))) #addes grades to a list 
print("\n") #new line added for neatness.
print(f"your average grade is {round(sum(grades)/classes, 2)} %") #calculates and prints the average grade.


    