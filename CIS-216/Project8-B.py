# Name: Marissa Wagner
# Date: 08/13/2022
# Proj: Project 8

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

items=["ORD\n","LAX\n","SDF\n","AZO\n","GRR\n"]

# open a new file in write mode 
file1 = open("exercise-airports.txt", "w") 

# use write function to write lines to the file
file1.writelines(items)

# close the file
file1.close()


# open the file in read mode using open function
file2 = open("exercise-airports.txt", "r") 

# use loop to iterate each line and print the lines
a =[]
for i in file2.readlines():
 a.append(i)
 print(i[:-1])

# close the file
file2.close()

# sort items and write back 
a=sorted(a)
file3 = open("exercise-airports.txt", "w") 

# use write function to write sorted lines to the file
file3.writelines(a)

# close the file
file3.close()

print()

# open the file in read mode using open function
file3 = open("exercise-airports.txt", "r") 

# use loop to iterate each line and print the lines
a =[]
for i in file3.readlines():
 a.append(i)
 print(i[:-1])

# close the file
file3.close()
