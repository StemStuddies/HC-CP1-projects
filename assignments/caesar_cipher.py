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


message = input("Message to encode? ").strip()

for x in message:
    if x.isnumeric:
        chiper += x
    else:
        shifted = ord(x) + shift
        chiper += chr( shifted % 26 + 65)
print("encoded message")
print(chiper)