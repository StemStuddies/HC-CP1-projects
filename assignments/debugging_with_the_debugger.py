#hunter card, debuging with the debugger
# Ravager Snack Bar
import random

pirate_name = input("What's your name, pirate? ")
snack_name = input("What snack do you want? ")

price = random.randint(2, 8)  # random price in credits
quantity = int(input("How many would you like? ")) #it was a string needed to be a integer so added int()

total = price * quantity

discounted_total = total - total * 0.10 #discounted is calcualated by taking total - total * discount percent fixed it to be that.

tax_rate = 0.08
total_with_tax = discounted_total + (discounted_total * tax_rate)

print("Hello, " + pirate_name + "! Here's your order summary:")
print("Snack: " + snack_name) #varibal name was off fixed so that varibal is the varibal name.
print("Price per snack: " + str(price) + " credits")
print("Total before tax: " + str(total)) # changed it to total instead of price
print("Total with tax: " + str(round(total_with_tax, 2)) + " credits") #end parenthesis was missing added the end parenthesis