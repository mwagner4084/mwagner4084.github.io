# Name: Marissa Wagner
# Date: 08/06/2022
# Proj: Project 7

# clear the screen
import os
clear = lambda: os.system('clear')
clear()

people = {
	'Travis': 'he hates wet socks.',
	'Maggie': 'she can not pronounce the word szechuan.',
	'Zoey': 'she dips hot cheetos in peanut butter.'
}

for name, fact in people.items():
	print("An interesting fact about " + name + " is that " + fact)

print()

people['Gabe'] = 'he enjoys natural ice beer.'
people['Travis'] = 'he eats cold soup from the can.'

for name, fact in people.items():
	print("An interesting fact about " + name + " is that " + fact)