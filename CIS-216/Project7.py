# Name: Marissa Wagner
# Date: 08/13/2022
# Proj: Project 7

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# create list of tuple of airports and code
airport_list = [("O'Hare International Airport", "ORD"), 
                ("Los Angeles International Airport", "LAX"),
                ("Dallas/Fort Worth International Aitport", "DFW"), 
                ("Denver International Airport", "DEN")
]

# loop through list
for airport in airport_list:
    # print airport name and code
    print(f"The code for {airport[0]} is {airport[1]}.")