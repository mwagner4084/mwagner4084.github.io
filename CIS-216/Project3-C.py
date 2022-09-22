# Name: Marissa Wagner
# Date: 07/09/2022
# Proj: Project 3-C

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# print even numbers
print("Even numbers in the range 0 to 20, inclusively, include: ")

# loop to iterate from 0 to 20 - 21 not included in range
for num in range (0,21):
    if (num % 2 == 0):
     print (num)

print()

# print odd numbers
print("Odd numbers in the range 0 to 20, inclusively, include: ")

# loop to iterate from 0 to 20 - 21 not included in range
for num in range (0,21):
    if (num % 2 != 0): 
     print (num)