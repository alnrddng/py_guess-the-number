# !/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Name: Guess the Number
Purpose: A fun number guessing program to try and outsmart the machine.
Version: 20230413
License: MIT

Developer(s): Alan Redding (GitHub: alnrddng)
'''

import random


def main(upper_limit):
    ''' get the computer to guess our number '''

    lower_limit = 1
    feedback = ''
    count = 0

    while feedback != 'c':

        if lower_limit != upper_limit:
            guess = random.randint(lower_limit, upper_limit)
        else:
            guess = lower_limit

        if count == 11:
            print(
                f"The computer couldn't get it right. It's next guess would have been {guess}")
            return

        feedback = input(
            f"Is {guess} too high (H) too low (L) or correct (C)?: ").lower()

        if feedback == 'h':
            upper_limit = guess - 1
        elif feedback == 'l':
            lower_limit = guess + 1

        count += 1

    print(f"Yay! The computer got it right with {guess}!")


if __name__ == "__main__":
    upper_limit = int(input("What is the biggest possible number?: "))
    main(upper_limit)
