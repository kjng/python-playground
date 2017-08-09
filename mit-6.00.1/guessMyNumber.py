# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:55:06 2017

@author: sfk1j

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!
"""

guess = 50
low = 0
high = 100

print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number ' + str(guess) + '?')
    result = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if result == 'h':
        high = guess
        guess = int((low + high) / 2)
    elif result == 'l':
        low = guess
        guess = int((low + high) / 2)
    elif result == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    else:
        print('Sorry, I did not understand your input.')
