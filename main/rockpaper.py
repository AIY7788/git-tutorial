
import random

options = ["rock", 'paper', 'scissors']
runing = True

while runing:
    computer = random.choice(options)
    player = input("enter your chioces (rock, paper, scissors) : ")
    if player == "rock":
        print("Player : ✊")
    elif player == "paper":
        print("Player : 🫱")
    elif player == "scissors":
        print("Player : ✌️")
        

        
    if player == "rock" and computer == "scissors":
        print('Computer: ✌️')
        print("you win!")

    elif player == "paper" and computer == "rock":
        print('Computer: ✊')
        print("you win!")   

    elif player == "scissors" and computer == "paper":

        print('Computer: 🫱')
        print("you win!")  

    elif player == computer : 
        if computer == "rock":
            print('Computer: ✊')
        if computer == "paper":
            print('Computer: 🫱')
        if computer == "scissors":
            print('Computer: ✌️')
            
        print("it is tie!")
    elif player not in options:
        print("Invalid choice")
        

    else :

        if computer == "rock":
            print('Computer: ✊')
        if computer == "paper":
            print('Computer: 🫱')
        if computer == "scissors":
            print('Computer: ✌️')
        print("you lose!")

    if not input("play again? (y/n) : ").lower() == "y":
        runing = False

print("thanks for playing 😊")