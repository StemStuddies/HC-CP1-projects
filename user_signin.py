#hunter card user sign in
while True:
    username = input("Whats the username: ")
    if username == "TheCoolGuy":
        password = input("whats the password: ")
        if password == "M3ntT0b5":
            print("----ACCESS GRANTED----")
            print("Welcome to the program TheCoolGuy")
            break
        else:
            print("----ACCESS DENIED----")
    else:
        print("User not found")
