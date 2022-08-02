import random

answer = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if 0 < guess < 11:
            if guess == answer:
                print("Good job!")
                break
            else:
                print("Try again")
                continue
        else:
            print("Hey, the number needs to be from 1 to 10")

    except ValueError:
        print("Please enter a number")
        continue
