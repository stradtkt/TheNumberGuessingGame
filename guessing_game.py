"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    play = True
    while play:
        random_number = random.randint(1, 20)
        guess = int(input("Enter an integer from 1 to 20: "))
        while random_number != "guess":
            if guess < random_number:
                try:
                    print("Guess is too low!")
                    guess = int(input("Enter an integer from 1 to 20: "))
                except (SyntaxError, ValueError):
                    print('Sorry you need to put in a number for your guess!  Please try again!  ')
            elif guess > random_number:
                print("Guess is too high!")
                guess = int(input("Enter an integer from 1 to 20: "))
            else:
                print("you guessed it!")
                break
        again = str(input('Wanna play again? (yes/no)'))
        if again == 'no':
            play = False
            break
        elif again == 'yes':
            play = True


# Kick off the program by calling the start_game function.
start_game()