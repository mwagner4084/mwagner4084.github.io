# Name: Marissa Wagner
# Date: 08/13/2022
# Proj: Project 8

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# open a new file in write mode and write three lines to it
file = open('exercise-one.txt','w')

# use write function to write lines to the file
file.write("This is the first line.\n")
file.write("This is the second line.\n")
file.write("Finally, this is the third and last line.\n")

# close the file
file.close()

# open the file in read mode using open function
file1 = open('exercise-one.txt', 'r')

# use loop to iterate each line and print the lines
for line in file1:
    print(line,end='')

# close the file
file1.close()

print()

# open the file in read mode 
file2 = open('exercise-one.txt', 'r')
n=1

# iterate each line in the file
for line in file2:
    # print line number before printing the line 
    print(n,end='')
    print(". ",line,end='')
    n+=1

# close the file
file1.close()