# Hunter Card Dice Roller
import random
import time
dice_rolls = [] #keeps track of the dice rolls you made
dice_roll = 0 # for current roll to print and append.
choice = "" #users choice to roll again or not.
dice = 1
while True: #stupid proof. 
    try:
        dice_type = int(input("What dice do you want? D4 D6 D8 D10 D12 D20. only put the number! D"))
    except:
        print("thats not a number! ")
        time.sleep(1)
    else:
        if 3 <= dice_type <= 20 and dice_type % 2 == 0: 
            break
        else:
            print("thats not one of the options")
            time.sleep(1)
while True: #stupid proof. 
    try:
        dice = int(input("how many times do you want to roll? 1 to 100"))
    except:
        print("thats not a number! ")
    else:
        if 1 <= dice <= 100: 
            break
        else:
            print("not in the range!")
for x in range(0, dice): #
    dice_roll = random.randint(1, dice_type) #rolling dice
    print(f"you rolled a {dice_roll}!") #showing user what they rolled
    dice_rolls.append(dice_roll) # add the current roll to the total rolls the user made.
    time.sleep(0.05)
print("number | total amount of times you rolled it")
for num in range(1,dice_type + 1): #for loop to print every number possible in dice to display total number of times that dice was rolled.
    print(f"     {num} | {dice_rolls.count(int(num))} times") #prints the total amount of nums you rolled.