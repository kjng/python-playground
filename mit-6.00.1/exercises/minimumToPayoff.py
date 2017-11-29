# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:07:34 2017

@author: sfk1j
"""

"""
Calculates and prints the minimum payment in order to pay off a credit card balance in a year
The minimum payment is a multiple of 10

Inputs:
    balance = outstanding balance on a credit card
    annualInterestRate = annual interest rate as a decimal
"""
def minimumToPayOff(balance, annualInterestRate): 
    monthlyInterestRate = annualInterestRate / 12.0
    unpaidBalance = balance
    lowestPayment = 10
    
    def resetBalance(balance):
        nonlocal unpaidBalance
        unpaidBalance = balance
        
    def incrementPayment():
        nonlocal lowestPayment
        lowestPayment += 10
    
    def tryAmount(monthlyPayment):
        for i in range(12):
            nonlocal unpaidBalance
            unpaidBalance -= monthlyPayment
            unpaidBalance += monthlyInterestRate * unpaidBalance
    
    while True:
        tryAmount(lowestPayment)
        if unpaidBalance <= 0:
            break
        else:
            resetBalance(balance)
            incrementPayment()
            
    
    print('Lowest Payment: ' + str(lowestPayment))
