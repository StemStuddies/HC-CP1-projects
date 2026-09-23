#hunter card crew share's
import random as rand
while True:
    try:
        pirates = int(input("how many pirates/crew are on board?"))
    except:
        print("thats not a number.")
    else:
        break
startunits = rand.randint(500, 1000)
units = startunits - pirates * 3
yondu = round(units * 0.13, 2)
units -= round(units * 0.13, 2)
peter = round(units * 0.11, 2)
units -= round(units * 0.11, 2)
crew = units / (pirates + 2)
yondu += round(crew, 2)
peter += round(crew, 2)
crew = round(crew, 2) + 3

print(f"Starting units: {startunits}")
print(f"Yondu's Share: {yondu}")
print(f"Peter's Share: {peter}")
print(f"Crew's Share: {crew}")
