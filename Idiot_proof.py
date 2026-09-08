#hunter card idiot proof
name = input("Whats your name? ").capitalize().strip()
while True:
    try:
        phone_number = int(input("What is your phone number? "))
    except:
        print("Thats not a valid phone number? ")
    else:
        phone_number = int(phone_number)
        break
while True:
    try:
        gpa = float(input("What is your GPA? "))
    except:
        print("Thats not a number.")
    else:
        if 0<= gpa <= 4:  #makes sure its inbetween acceptable gpa ranges
            gpa = str(gpa)
            break
        else:
            print("thats not a valid GPA")
print(f"name: {name} \nphone number: {phone_number} \nGPA: {gpa}")


