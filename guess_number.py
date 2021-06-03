import random

start = int(input('you decide the begining:'))
end = int(input('you decide the end:'))

x = random.randint(start, end)
n = 0 #calculate the guess times!

print(x)

while True:
	g = int(input('enter a number:'))
	n += 1
	if g == x:
		print('you got it!')
		print('totally you guess %d times!' % n )
		break
	elif g > x and g <= end:
	
		print('guess smaller')
	elif g < x and g >= start:
	
		print('guess bigger')
	else:
		print('you just can guess the number between %d to %d' % (start, end))
	
	print('forward you guess %d times!' % n )