import time
import random
def typew(inputy): #type writter function
    for x in inputy:
        print(x, end= "")
        time.sleep(0.1)
sentence = "the quick brown fox jumps over the lazy dog"
start = sentence.find("brown")

print(sentence[start:start+5])
typew("hello there im a sliding text >:)")

        

