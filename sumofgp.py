ser = 0
a = input('Enter base number(x) ')
b = int(input('Enter number of terms(n) '))
for i in range(b+1):
	ser += a**i
print('The sum of this series, x^0 + x^1 + x^2 + ... + x^n is...')
print ser

c = input('Press enter to exit')