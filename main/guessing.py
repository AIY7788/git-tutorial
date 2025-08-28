

import random

lowest = 1
highest = 100

number = random.randint(lowest, highest)
guesses = 0
runing = True

print("python guessing game ")
print(f"select a number between {lowest} to {highest} ")

while runing:

    guess = input("enter your guess : ")
    if guess.isdigit():
        guess =int(guess)
        guesses += 1

        if guess < lowest or guess > highest :
            print("number is out of range")
            print(f"select a number between {lowest} to {highest} ")
        elif guess < number:
            print("to low! try again")
            
        elif guess > number:
            print("to high! try again")
            
        else:
            print(f"CORRECT! ANSWER IS {number}")
            print(f"your guess is {guesses} times")
            runing = False
    else:
        print("invalid guess")
        print(f"select a number between {lowest} to {highest} ")