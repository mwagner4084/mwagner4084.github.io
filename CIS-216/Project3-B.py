# Name: Marissa Wagner
# Date: 07/09/2022
# Proj: Project 3-B

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# initializing variables
costPerHour = 0.81
income = float(input('Enter your income: '))

# calculations
costPerDay = costPerHour * 24
costPerMonth = costPerDay * 30
perDay20Servers = costPerDay * 20 
perMonth20Servers = costPerMonth * 20
daysWithIncome = int(income/costPerDay)

# output calculations
print(f"The hosting provider charges ${costPerHour:.2f} per hour.")
print(f"The cost to operate one server per day is ${costPerDay:.2f}.")
print(f"The cost to operate one server per month is ${costPerMonth:.2f}.")
print(f"The cost to operate 20 servers per day is ${perDay20Servers:.2f}.")
print(f"The cost to operate 20 servers per month is ${perMonth20Servers:.2f}.")
print(f"You could operate one server for {daysWithIncome} days with ${income:.2f}.")
