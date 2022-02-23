# !/usr/bin/env python3
#  Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'


def loop():
    lives = 4
    pw = ''
    while pw != secret:
        pw = input("What's the secret word? ")
        lives -= 1
        print(f"You have {lives} lives left")


loop()
