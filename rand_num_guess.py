#!/usr/bin/env python3
# Created By: Kaylee Ralejoe
# Date: 15,10,2026
# The program generates a random
# number from a range of numbers and creates
# a guessing game for the user to
# guess what the number may be.

import random


def main():
    # generate a random number
    random_variable = random.randint(0, 9)

    # get the user to guess the random number
    user_guess = int(input("Guess a number from 0-9: "))

    # check if user's guess is correct
    if user_guess == random_variable:
        print("You have guessed correctly!")
    else:
        print("Incorrect. The correct answer is {} ".format(random_variable))


if __name__ == "__main__":
    main()
