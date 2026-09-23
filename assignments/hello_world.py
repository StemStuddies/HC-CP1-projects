#hunter card hello world
name = input("hello what is your name? ")
print("hello " + name)

mood = input(f"well {name} how are you doing today?, good bad")
if mood == "good":
    print("thats good!")
elif mood == "bad":
    print("im sorry to hear that.")
else:
    print("i didnt understand that.")