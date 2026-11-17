#hunter card order up
import time

#stupid proof function
def noinput(message, awnsers, invmessage = "Thats not an acceptable input!"):
        awnser = input(str(message))
        if awnser in awnsers:
            return awnser
        else:
            print(invmessage)

#main dish dictonary with prices
maindish = {
    "hamburger": 4.95,
    "chicken tenders": 3.99
}
#side dish dictonary with prices
sidedish = {
    "fries": 1.99,
    "salad": 2.50
    ""
}

#menu terminal art with stuff.
print("""
    _______MAIN_DISH_______        _______SIDE_DISH_______
    hamburger 4.95$
    chicken nuggets 3.99$  
      
      
      
      """)
