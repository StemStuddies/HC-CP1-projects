#hunter card crew share's
import random as rand #me being lazy.
while True: 
    try:
        pirates = int(input("how many pirates/crew are on board? "))
    except:
        print("thats not a number.")
    else:
        break
startunits = rand.randint(500, 1000) #its just one line of code?
units = startunits # seting to make sure it stays the same.
units = startunits - pirates * 3 #minuses crew 3 from start DOSENT ADD
yondu = units * 0.13
units -= round(yondu, 2) #rounding to nearest hundredth
peter = units * 0.11
units -= round(peter, 2)
crew = units / (pirates + 2) #find out the crew share before the 3 to use as how much everyone gets
yondu += crew
peter += crew
crew = crew + 3 #adds the 3 that they got for the iorn locaus.

print(f"Starting units: {round(startunits, 2)}") # display output
print(f"Yondu's Share: {round(yondu, 2)}")
print(f"Peter's Share: {round(peter, 2)}")
print(f"Crew's Share: {round(crew, 2)}")

