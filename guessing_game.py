"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    count = 0

    def welcome_message():
        print(""" 
 _____ _        _  _            _              ___                _            ___                
|_   _| |_  ___| \| |_  _ _ __ | |__  ___ _ _ / __|_  _ ___ _____(_)_ _  __ _ / __|__ _ _ __  ___ 
  | | | ' \/ -_) .` | || | '  \| '_ \/ -_) '_| (_ | || / -_|_-<_-< | ' \/ _` | (_ / _` | '  \/ -_)
  |_| |_||_\___|_|\_|\_,_|_|_|_|_.__/\___|_|  \___|\_,_\___/__/__/_|_||_\__, |\___\__,_|_|_|_\___|
                                                                        |___/  
        """)
        print("Press [q/Q] to quit")

    def random_number():
        number = random.randint(1, 20)
        return number

    def guess(count, number):
        while True:
            try:
                the_guess = input('Guess a number between 1 and 20: ')
                if the_guess == "q" or the_guess == "Q":
                    print("Thank you for playing!")
                    print("Goodbye!")
                    exit()
                if not the_guess.isdigit():
                    raise ValueError("The guess needs to be a digit, please try again.")
                the_guess = int(the_guess)
                if the_guess > 20 or the_guess < 1:
                    raise ValueError("The guess is out of the specified range for the game.  Please try again.")
            except ValueError as error:
                print("There has been an error.  Your error is: {}".format(error))
            else:
                count += 1
                if the_guess == number:
                    print("You guessed the right number!  It took you {} attempts to guess.".format(count))
                    play_again()
                if the_guess > number:
                    print("The number is lower than that, please try again.")
                if the_guess < number:
                    print("The number is higher than that, please try again.")


    def play_again(count):
        while True:
            try:
                play_again = input("Do you want to play again?  [y/yes] or [n/no]").lower()
                if play_again not in ("y", "yes", "n", "no", "q"):
                    raise ValueError("Please enter [y or yes] or [n or no]")
            except ValueError as error:
                print("There has been an error.  Your error is: {}".format(error))
            else:
                if play_again == "y" or play_again == "yes":
                    count = 0
                    number = random_number()
                    guess(count, number)


    welcome_message()
    number = random_number()
    guess(count, number)

if __name__ == '__main__':
    start_game()