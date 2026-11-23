#hunter card, flexible calculator
import math

def calc(*numbers, oper="sum"):
    if oper == "sum":
        return(sum(*numbers))
    elif oper == "average":
        return(sum(*numbers)/len(*numbers))
    elif oper == "max":
        return(max(*numbers))
    elif oper == "min":
        return(min(*numbers))
    elif oper == "product":
        return(math.prod(*numbers))

numberlist = []
userin = 0
invalid = False
print("what numbers would you like to preform with? \n type done when done.")
while userin != "done":
    while True:
        userin = input("type a number: ")
        if userin == "done":
            break
        try:
            int(userin)
        except:
            print("thats not a number!")
        else:
            break
    if userin != "done":
        numberlist.append(userin) 
    
                    
            