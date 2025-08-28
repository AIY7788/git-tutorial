

import random

from listw import word , hangman_art 

def display_man (wrong_guesses):
    print("##########")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("##########")

def display_hint (hint):
    print(" ".join(hint))

def display_answer (answer):
    print(" ".join(answer))

def main ():
    answer = random.choice(word)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guesses_letters = set()
    running = True

    while running : 
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("enter the letter : ").lower()

        if len(guess) != 1 or not guess.isalpha():
        
            print("invalid input")
            continue

        if guess in guesses_letters:
            
            print(f"{guess} is already guessed ")
            continue

        guesses_letters.add(guess)

        if guess in answer :
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint :
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            running = False
        elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            running = False

if __name__ == "__main__":
    main()