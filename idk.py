
try:
    with open("data.txt", "r") as file:
        count = int(file.read())
except:
    count = 0
count += 1
print(f"This program has run {count} times.")
with open("data.txt", "w") as file:
    file.write(str(count))
