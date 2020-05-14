import math as mt
print('Quadratic solver')
print('Of the form ax^2+bx+c=0')
a = int(input('Please input a>>>'))
b = int(input('Please input b>>>'))
c = int(input('Please input c>>>'))
D = b**2 - (4*a*c)
if D == 0:
	x = (-b)/(2*a)
	print('The roots are real, repeating and are equal to')
	print(x)
if D < 0:
	print('The roots are imaginary')
if D > 0:
	x1 = (-b + mt.sqrt(D))/(2*a)
	x2 = (-b - mt.sqrt(D))/(2*a)
	print('The roots are real, and are')
	print(x1, x2)