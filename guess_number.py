import random

x = random.randint(1, 100)
n = 0 #calculate the guess times!

print(x)

while True:
	g = int(input('enter a number:'))
	if g == x:
		n += 1
		print('you got it!')
		print('forward you guess %d times!' % n )
		break
	elif g > x and g <= 100:
		n += 1
		print('guess smaller')
	elif g < x and g >= 1:
		n += 1
		print('guess bigger')
	else:
		print('you just can guess the number between 1 to 100')
	
	print('forward you guess %d times!' % n )