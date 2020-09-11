# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 09:13:16 2020

@author: exebu
"""

from random import choice
from string import ascii_lowercase
print("H A N G M A N")

while True:
    user_action = input('Type "play" to play the game, "exit" to quit: ')
    if user_action == "play":
        correct_word = list(choice(['python', 'java', 'kotlin', 'javascript']))
        hidden = list("-"*len(correct_word))
        guessed = list()
        lifes = 0
        while lifes < 8:
            print()
            print("".join(hidden))
            user_guess = input("Input a letter: ")
            if len(user_guess) != 1:
                print("You should input a single letter")
            elif user_guess not in ascii_lowercase:
                print("It is not an ASCII lowercase letter")
            elif user_guess in guessed:
                print("You already typed this letter")
            elif user_guess in correct_word:
                guessed.append(user_guess)
                for i, value in enumerate(correct_word):
                    if user_guess == value:
                        hidden[i] = user_guess
            else:
                guessed.append(user_guess)
                print("No such letter in the word")
                lifes += 1

            if "".join(hidden) == correct_word:
                print(f"You guessed the word {correct_word}!")
                print("You survived!\n")
                break
        else:
            print("You are hanged!")
    elif user_action == "exit":
        break