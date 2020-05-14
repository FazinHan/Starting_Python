n = input('What\'s your desired maximal number?>>> ')
n = int(n) + 1
for a in range(1,n):
	for b in range(a,n):
		c_square = a**2 + b**2
		c = int((c_square)**0.5)
		if c > n-1:
			continue
		if ((c_square - c**2) == 0):
			print(a, b, c)
input('Press enter to quit>')