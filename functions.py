#vl functions
attempts = 0

def birthday(name,age):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")
    print(f"{name} is now {age} years old!")


birthday("Alice", 30)

def stupid_proof(user_answer, correct):
    done = False
    user_answer = user_answer.strip()
    if user_answer in correct:
        return True, user_answer, attempts + 1
    else:
        return False, user_answer, attempts + 1

while True:
    capital = input("what is the capital of Utah ")
    correct, capital, attempts = stupid_proof(capital, ["SLC"])
    if correct:
        print(f"Good job {capital} is the capital of utah!")
        break
    else:
        print(f"Try again. {capital} is not the capital of Utah. you have tried {attempts} times")
quiz = input("is the beehive the capital of utah?")

