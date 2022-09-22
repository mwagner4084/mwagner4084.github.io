# Name: Marissa Wagner
# Date: 07/09/2022
# Proj: Project 3-A

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# initializing variables
costPerHour = 0.81

# calculations 
costPerDay = costPerHour*24
costPerMonth = costPerDay*30

# output calculations
print(f"The hosting provider charges ${costPerHour:.2f} per hour.")
print(f"The cost to operate one server per day is ${costPerDay:.2f}.")
print(f"The cost to operate one server per month is ${costPerMonth:.2f}.")
