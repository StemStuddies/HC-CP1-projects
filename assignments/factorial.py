#hunter card, factorial 
import math
def equation(inn): # equation generator for factorials exp 3 x 2 x 1
    return f"{inn} x"
numbers = [] # numbers
fact_numbers = [] # factorial numbers
display = [] #list for displaying the list
while True: #stupid proof.
    try:
        times = int(input("how many number calculations do you want to preform? 1-10 \n")) #how many times they want to calculate.
    except:
        print(" Thats not a number")
    else:
        if 1 <= times <= 10:
            break
        else:
            print("thats not in acceptable range")
for x in range(0, times):
    while True: #stupid proof
        try:
            numb = int(input("what number do you want to take the factorial of? ")) #numb for number,
        except:
            print(" Thats not a number")
        else:
            if 0 <= numb:
                break
            else:
                    print("thats a negitive number!")
    numbers.append(numb)
fact_numbers = list(map(math.factorial, numbers)) #appending then adding the factorial numb
print("___factorial calculator___")
for y in range(0,len(numbers)): #looping for every calculation that will happen
    print(f"{numbers[y]}! = {fact_numbers[y]} =", end=" ") #printing awnser and number
    display = list(map(equation, range(numbers[y], 1, -1))) #printing the product equation exp 3 x 2 x 1
    print(*display, end="") #makeing sure it dosent go to new line
    print(" 1") #adding the one at the end.

# I DID IT AND IS BEUTIFUL IM PRoUD I THOUGHT IT WAS GOING TO BE REAL HARD.