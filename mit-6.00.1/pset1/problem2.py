# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:06:12 2017

@author: sfk1j

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'

numOfBobs = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        numOfBobs += 1
print('Number of times bob occurs is: ' + str(numOfBobs))
