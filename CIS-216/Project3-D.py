# Name: Marissa Wagner
# Date: 07/09/2022
# Proj: Project 3-D

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# input first and second number
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

# modulus finds remainder when on number divided by other
if (number1 % number2 == 0):
    # if divisible
    print ("First number is perfectly divisible by the second number.")
else:
    # if not divisible
    print ("First number is NOT perfectly divisible by the second number.")
