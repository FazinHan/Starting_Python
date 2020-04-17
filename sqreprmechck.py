def prme(a):
	mid = None
	if a % 2 == 0 and a != 0:
		return 'This number has a composite square root.'
	elif a ==  1 or a == 0:
		return 'That has neither a prime nor composite square root.'
	else:
		mid = int(a/2) + 1
		for b in range(2,mid):
			if a % b == 0:
				return 'This number has a composite square root.'
		else:
			return 'This number has a prime square root.'

def sqrt(a):
	if a == 1 or a == 0:
		return a
	elif a <= 0:
		print('Error.')
	else:
		for i in range(a/2):
			if i*i == a:
				return i

print('Checking if the square root of an integer is prime or not.')
check = int(input('Enter the number (should be a non-negative perfect square) \nwhose square root you want checked>>> '))
sheck = sqrt(check)
print prme(sheck)
b = input('Press enter to quit>>>')