message = input("give me a message to encode ")
codedlet = []
for x in message:
    codedlet.append(ord(x))
message = ""
for x in codedlet:
    message += chr(x + 2)
print(message)