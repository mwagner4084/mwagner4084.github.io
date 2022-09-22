# Name: Marissa Connell
# Date: 07/02/2022
# Proj: Project 2-B

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

# input section
asciiCode = input ('Enter an ASCII code: ')

# output section
print ('\nThe character for ASCII Code ', end='')
print ('{} is "{}".'.format(asciiCode,chr(int(asciiCode))))
