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
    "salad": 2.50,
    "fruit bowl": 1.49
}

#menu terminal art with stuff.
print("""
    ______________________________________________________
    _______SIDE_DISH_______        _______MAIN_DISH_______
    fries 1.99$                hamburger 4.95$
    salad 2.50$                    chicken nuggets 3.99$
      
      
      
      """)


