#hunter card list manager
items = [] #items in shopping list
actions = ("1", "2", "3", "4", "add", "remove", "view", "exit") # turple for actions you can do
def listprint(table): #print function for code
    print("-----Shopping List-----")
    for x in table:
        print(x)


while True:
    while True: # stupid proof so users are not breaking things.
        action = input("What would You like to do? (1:add 2:remove 3:view 4:exit) \n")#user input with instructions
        if action in actions:
            break
        else:
            print(f"{action} is not an option. you can only pick 1 2 3 4 add remove view exit")
    if action == "1" or action == "add":
        update = input("What do you want to add to the list? \n")
        items.append(update)
    elif action == "2" or action == "remove":
        while True:
            update = input("What do you want to remove from the list? \n")
            if update in items:
                items.remove(update)
            else:
                print(f"{update} is not in the list")
    elif action == "3" or action == "view":
        print("\n")
        listprint(items)
        print("\n")
    elif action == "4" or action == "exit":
        listprint(list)
        break
    print("your list so far-", end=" ")
    print(*items)

