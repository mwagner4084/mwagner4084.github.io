# Name: Marissa Connell
# Date: 04/14/2022
# Proj: Project 7

import random # random number generator
import os 
# clear the screen
clear = lambda: os.system('clear')
clear()

# create array of random objects
itemArray = ["rock","paper","scissors","lizard","spock"]

# generate randomly selected computer choice
cChoice = random.randint(0,4)

# -------------- FUNCTION DEFINITIONS START HERE ------------------
def getInput():
    # function to get user input
    print("User options are: Rock, Paper, Scissors, Lizard, or Spock.")
    userChoice = input("Your pick? ").lower()
    return userChoice

def validateInput(uChoice):
    # function to validate users choice
    if uChoice == "rock" or uChoice == "paper" or uChoice == "scissors" or uChoice == "lizard" or uChoice == "spock":
        return True
    else:
        return False

def determineWinner(cChoice, uChoice):
    # function to determine winner
    if uChoice == cChoice:
        return "computer and you have tied. Play again to see who"
    if uChoice == "scissors":
        if cChoice == "paper" or cChoice == "lizard":
            return "user"
    if uChoice == "paper":
        if cChoice == "rock" or cChoice == "spock":
            return "user"
    if uChoice == "rock":
        if cChoice == "scissors" or cChoice == "lizard":
            return "user"
    if uChoice == "lizard":
        if cChoice == "spock" or cChoice == "paper":
            return "user"
    if uChoice == "spock":
        if cChoice == "rock" or cChoice == "scissors":
            return "user"
    else:
        return "computer"

def outputToUser(userChoice, cChoice):
    # function for output
    print("\n\n The computer played ", end='' )
    print("\033[31m" + itemArray[cChoice] + "\033[0m", end='')
    print(" and you played ", end='')
    print("\033[31m" + userChoice + "\033[0m", ".")
    print(" The " + determineWinner(itemArray[cChoice], userChoice) + " wins this round.")

#  --------------- PROGRAM STARTS HERE ---------------------

# get input from user
userChoice = getInput()

# see if it is a valid choice
while (validateInput(userChoice) !=True):
    # get user input
    userChoice = getInput()

if (validateInput(userChoice) == True):
    # see if there is a winner
    determineWinner(itemArray[cChoice], userChoice)
    # output the finish statement
    outputToUser(userChoice, cChoice)            
            