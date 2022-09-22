# Name: Marissa Connell
# Date: 07/02/2022
# Proj: Project 2-B

# clear the screen
from codecs import unicode_escape_decode
import os
clear = lambda: os.system('clear')
clear()

# input section
character = input ('Character? ')
uniCode = ord(character) 

# output section
print ('\nThe unicode character for ', end = '')
print ('"{}" is {}.'.format(character, int(uniCode)))
