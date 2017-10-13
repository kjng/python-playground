# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:04:20 2017

@author: sfk1j

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""

s = 'azcbobobegghakl'

numOfVowels = 0
for c in s:
    if (c == 'a') or (c == 'e') or (c == 'i') or (c == 'o') or (c == 'u'):
        numOfVowels += 1
print('Number of vowels: ' + str(numOfVowels))
