# Name: Marissa Wagner
# Date: 07/25/2022
# Proj: Project 5

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# define functions
def calcAverage (score1, score2, score3, score4, score5):
    return round(float((score1 + score2 + score3 + score4 + score5) / 5))

def determineGrade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def printColumnHeader():
    print("SCORE GRADE")

# get input / return output
if __name__ == "__main__":
    print("Please enter five test scores: ")
    score1 = int(input())
    score2 = int(input())
    score3 = int(input())
    score4 = int(input())
    score5 = int(input())
    print()
    printColumnHeader()
    print(str(score1).ljust(7), determineGrade(score1))
    print(str(score2).ljust(7), determineGrade(score2))
    print(str(score3).ljust(7), determineGrade(score3))
    print(str(score4).ljust(7), determineGrade(score4))
    print(str(score5).ljust(7), determineGrade(score5))
    print("AVERAGE SCORE: ", calcAverage(score1, score2, score3, score4, score5))