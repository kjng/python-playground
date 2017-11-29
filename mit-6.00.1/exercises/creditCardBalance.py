# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:49:10 2017

@author: sfk1j
"""

"""
Calculates and prints the credit card balance after one year if a person only pays the minimum monthly payment

Inputs:
    balance = outstanding balance on the card
    annualInterestRate = annual interest rate as a decimal
    monthlyPaymentRate = minimum monthly payment rate as a decimal
"""
def creditCardBalance(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    unpaidBalance = balance
    
    for i in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * unpaidBalance
        unpaidBalance = unpaidBalance - minimumMonthlyPayment
        unpaidBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)
    
    print('Remaining balance: ' + str(round(unpaidBalance, 2)))

creditCardBalance(42, 0.2, 0.04)
