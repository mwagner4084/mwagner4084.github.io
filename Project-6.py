# Name: Marissa Connell
# Date: 04/09/2022
# Proj: Project 6

import csv  # to work with comma seperated values files
import os  # to work with the operating system

def printPageHeader(pageNumber):
    # this prints the page header
    print("\n\n\n                                             STUDENT GRADE POINT REPORT: ", pageNumber)
    print("                                                       By:  Marissa Connell", "\n")

def printColumnHeader():
    # this prints the column header
    print("STUDENT NAME  COURSE ID #1  CR. HOURS  GRADE  GRADE PTS  GRADE PT AVG  COURSE ID #2  CR. HOURS  GRADE  GRADE PTS  GRADE PT AVG \n")

def printReportFooter(totalNumberOfStudents, totalCreditHours, totalGradePoints, totalGradePointAverage):
    # this prints the report footer
    print ("\n\n\nTotal Number of Students ", totalNumberOfStudents,"\n")
    print ("Total of all Credit Hours",  totalCreditHours,"\n")
    print ("Total of all Earned Grade Points", totalGradePoints ,"\n")
    print ("Final Grade Point Average",  totalGradePointAverage,"\n")

def calcGradePoints(num1, num2, num3):
    # this calculates and returns the grade points and rounds it to two decimal
    return round(num1 + num2 + num3, 2)

def calcCreditHours(num1, num2, num3):
    # this calculates the credit hours rounded to one decimal 
    return round(num1 + num2 + num3, 0)

def calcGradePointAvg(num3, num2):
    # this calculates the gpa rounded to three decimal
    return round(num3 / num2, 3)

def calcCourse1Pts(num1, num2):
    # this calculates and returns course 1 grade points and rounds it to two decimal
    return round(num1 * num2, 2)

def calcCourse2Pts(num1, num2):
    # this calculates and returns course 2 grade points and rounds it to two decimal
    return round(num1 * num2, 2)

def calcCourse1GPA(num1, num2):
    # this calculates and returns course 1 gpa and rounds it to one decimal
    return round(num1 / num2, 1)

def calcCourse2GPA(num1, num2):
    # this calculates and returns course 2 gpa and rounds it to one decimal
    return round(num1 / num2, 1)

# this clears the screen
def clear(): return os.system('clear')  # on windows
clear()

# set up the accumulators (counters)
totalNumberOfStudents = 0
totalCreditHours = 0 
totalGradePoints = 0
totalGradePointAverage = 0
pageNumber = 1

# open a file for reading
f = open('/Users/marissaconnell/Desktop/CIS 150/Project 6/GradePtsFile.csv', 'r')

# check to see if the file ACTUALLY opened
if f.mode == 'r':

    printPageHeader(pageNumber)
    printColumnHeader()
    # # go through each row of data in the file
    for row in csv.reader(f):
        # put the data into an array

        studentName = row[0]
        courseID1 = row[1]
        course1CreditHours = float(row[2])
        course1Grade = float(row[3])
        course1GradePoints = 0
        course1GradePtAvg = 0
        courseID2 = row[4]
        course2CreditHours = float(row[5])
        course2Grade = float(row[6])
        course2GradePoints = 0
        course2GradePtAvg = 0

        if (course1Grade > 0 and course2Grade > 0):

        # calculations ----------------------------------------------

             # add one to the accumulator for divers
            totalNumberOfStudents = totalNumberOfStudents + 1

            # calculate credit hours
            totalCreditHours = calcCreditHours(totalCreditHours, course1CreditHours, course2CreditHours)

            # calculate course 1 points
            course1GradePoints = calcCourse1Pts(course1CreditHours, course1Grade)

            # calculate course 2 points
            course2GradePoints = calcCourse2Pts(course2CreditHours, course2Grade)

            # calculate the grade points
            totalGradePoints = calcGradePoints(totalGradePoints, course1GradePoints, course2GradePoints)

            # calculate the gpa
            totalGradePointAverage = calcGradePointAvg(totalGradePoints, totalCreditHours)

            # calculate course 1 gpa
            course1GradePtAvg = calcCourse1GPA(course1GradePoints, course1CreditHours)

            #calculate course 2 gpa
            course2GradePtAvg = calcCourse2GPA(course2GradePoints, course2CreditHours)


        # output to the console
        print(studentName.ljust(15), end='  ')
        print(courseID1.ljust(6), end='  ')
        print(str(course1CreditHours).rjust(9), end='')
        print(str(course1Grade).rjust(9), end='')
        print(str(course1GradePoints).rjust(8), end='  ')
        print(str(course1GradePtAvg).rjust(10), "        ", end='')
        print(courseID2.ljust(9), end='')
        print(str(course2CreditHours).rjust(10), end='')
        print(str(course2Grade).rjust(10), end='')
        print(str(course2GradePoints).rjust(8), end='  ')
        print(str(course2GradePtAvg).rjust(10), "     ", end='')
        print('')

        # put in a page break for every twenty records
        if (totalNumberOfStudents % 20 == 0):
            pageNumber = pageNumber + 1
            printPageHeader(pageNumber)
            printColumnHeader()

# print the report footer    
printReportFooter(totalNumberOfStudents, totalCreditHours, totalGradePoints, totalGradePointAverage)
