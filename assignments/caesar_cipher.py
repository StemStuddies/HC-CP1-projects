#hunter card caesar cipher
import time


def encode(phrase, shift_amount): #encode function
    """"this function is for encoding things ya know. its literly the same thing """
    for x in phrase: #for x in every of input
        if x.isnumeric: #tests if its numeric
            chiper += x #automaticly adds it to disinclude numbers
        else:
            shifted = ord(x) + shift_amount #shifting it by amount
            chiper += chr( shifted % 26 + 65) #adding the shift and macking sure its acutually the letter
    return chiper
def decode(phrase, shift_amount): #Decode function using encode function but with negitive input.
    encode(phrase, -shift_amount) #using encode function but with negitive shift

print("~~~Caesar Cipher Decoder And Encoder~~~")
while True: #while loop
    what = input("Would you like to D Decode or E Encode type the letter: ").lower().strip()
    if what in ("d","e"):
        break
    else:
        print("thats not one of the options type the letter you want to do")

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


message = input("Message to encode? ").replace(" ", "").lower

if what == "e":
    print(f"encoded message {encode(message, shift)}")
elif what == "d":
    print(f"decoded message {decode(message, shift)}")
