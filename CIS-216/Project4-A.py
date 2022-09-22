# Name: Marissa Wagner
# Date: 07/19/2022
# Proj: Project 4-A

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# prompt user for input 
noMiles = int(input("How far would you like to travel in miles? "))

# if miles is less than 2
if noMiles < 2:
    print("Plase walk.")
# miles between 2 and 200
elif noMiles > 2 and noMiles < 200:
    print("Please drive.") 
else:
    print("Please fly.")