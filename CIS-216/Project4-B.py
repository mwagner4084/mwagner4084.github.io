# Name: Marissa Wagner
# Date: 07/19/2022
# Proj: Project 4-B

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# define function
def main():

    # initializing variables
    weight = int(input("Please enter the weight of the package: "))
    rate = 0

    # if statements
    if weight <= 3:
        rate = weight * 1.25
    elif weight > 3 and weight <= 7:
        rate = weight * 2.25
    elif weight > 7 and weight <= 11:
        rate = weight * 3.50
    elif weight > 11:
        rate = weight * 4.00
    return (f"The shipping charge is: ${rate:.2f}") 

print(main())