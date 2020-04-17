def ndesc(a):
	if a % 2 == 1:
		for i in range(a, 0, -2):
			print(i)
	else:
		for i in range(a-1, 0, -2):
			print(i)

b = int(input('Enter a number '))
ndesc(b)

c = input('Press enter to continue')