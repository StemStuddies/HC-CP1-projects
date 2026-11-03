#hunter card caesar cipher
import time
chiper = ""
print("~~~Caesar Cipher Decoder And Encoder~~~")
while True:
    try:
        shift = int(input("Shift of message? "))
    except:
        print("Thats not a number")
    else:
        if 0 <= shift <= 25:
            break
        else:
            print("Out of range Shift can only be between 0 and 25")
            time.sleep(1)

while True:
    message = str(input("Message to encode? "))
    if any(x.isnumeric() for x in message): #any function allows you to use for loops to construct a boolean statement all on the same line.
        print("that contains numbers wich is not allowed")
        time.sleep(1)
    else:
        break

for x in message:
    shifted = ord(x) + shift
    chiper += chr( shifted % 26 + 65)
print("encoded message")
print(chiper)