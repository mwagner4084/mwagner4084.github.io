# Name: Marissa Connell
# Date: 07/02/2022
# Proj: Project 2-A

# clears screen
import os
clear = lambda: os.system('clear')
clear()

# input section
animal = input ('Animal? ')
vegetable = input ('Vegetable? ')
mineral = input ('Mineral? ')

# output section
print ('\nHere is an animal, a vegetable, and a mineral.')
print ('{}\n{}\n{}'.format(animal, vegetable, mineral) )