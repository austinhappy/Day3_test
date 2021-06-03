import random

x = random.randint(1, 100)

while True:
	g = int(input('enter a number:'))
	if g == x:
		print('you got it!')
		break
	elif g > x and g <= 100:
		print('guess smaller')
	elif g < x and g >= 1:
		print('guess bigger')
	else:
		print('you just can guess the number between 1 to 100')