#hunter card, factorial 
import math
numbers = [] # numbers
fact_numbers = [] # factorial numbers
display = [] #list for displaying the list
while True: #stupid proof
    try:
        times = int(input("how many times do you want to do factorial? ")) #numb for number,
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
print(fact_numbers)
for iter in len(numbers)
map(print())