#hunter card, flexible calculator
import math

def calc(*numbers, oper="sum"):
    print(numbers)
    if oper == "sum":
        return(sum(numbers(1)))
    elif oper == "average":
        return(sum(numbers(1))/len(numbers[1]))
    elif oper == "max":
        return(max(numbers(1)))
    elif oper == "min":
        return(min(numbers(1)))
    elif oper == "product":
        return(math.prod(numbers(1)))

calc([1,2,3,4,5], "sum")

numberlist = []
userin = 0
invalid = False
while True:
    print("what numbers would you like to preform with? \n type done when done.")
    while userin != "done":
        while True:
            userin = input("enter number?: ")
            if userin == "done":
                break
            try:
                int(userin)
            except:
                print("thats not a number!")
            else:
                break
        if userin != "done":
            userin = int(userin)
            numberlist.append(userin) 

    print("_____Your list of numbers____")
    print(numberlist)
    while True:
        do = input("what would you like to do? type the word sum, average, max, min, product \n")
        if do in ("sum", "average", "max", "min", "product"):
            break
        else:
            print("thats not one of the options")

    print(f"_____Result of {do}_____")
    print(*calc(numberlist, do))
    print("\n")
    while not do in ("y", "n"):
        do = input("would you like to preform a nother calculation y or n: ")
    if do == "y":
        print("\n")
    elif do == "n":
        break
    else:
        print("didnt know what you wanted so exited")
        break


                    
            