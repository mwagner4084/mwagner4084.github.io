# Name: Marissa Connell
# Date: 04/14/2022
# Proj: Project 8

# use this to get date time from system
from datetime import date 
# create variable named today and assign date to it
today = date.today()

import os 
# clear the screen
clear = lambda: os.system('clear')
clear()

def userPick(userChoice):
    # userpick function has menu and branches out depending on user input
    while (userChoice != "A" or userChoice != "B" or userChoice != "C"):
        # print out menu for user
        print("")
        print("Choose a method to display the date:")
        print("   A. month-day-year as in the United States.")
        print("   B. day-month-year as in the United Kingdom.")
        print("   C. year-month-day, the international standard.")
        print("   X. Exit the program.\n")

        # get the users choice
        userChoice = input("How would you like the date to appear? ").upper()

        # branch depending on users choice
        if userChoice == "A" :
            print("")
            userChoice = monthDayYear(today.strftime("%d"),
                today.strftime("%m"), today.strftime("%y"))
        if userChoice == "B" :
            print("")
            userChoice = dayMonthYear(today.strftime("%d"),
                today.strftime("%m"), today.strftime("%y"))
        if userChoice == "C" :
            print("")
            userChoice = yearMonthDay(today.strftime("%d"),
                today.strftime("%m"), today.strftime("%y"))
        else:
            return userChoice

def monthDayYear(day, month, year):
    # print month day year format
    print(month + "-" + day + "-" + year)
    return "Z"

def dayMonthYear(day, month, year):
    # print day month year format
    print(day + "-" + month + "-" + year)
    return "Z"

def yearMonthDay(day, month, year):
    # print year month day format
    print(year + "-" + month + "-" + day)
    return "Z"

# set priming variable equal to z
userChoice = "Z"

# while the users choice isn't x
while (userChoice != "X"):
    userChoice = userPick(userChoice)

# print at end of program
print("\n\n\nThank you for using our date formatter. Have a great day! \n\n\n")