import matplotlib.pyplot as plt
import numpy as np

print('Quadratic solver')
print('Of the form ax^2+bx+c=0')
a = int(input('Please input a>>>'))
b = int(input('Please input b>>>'))
c = int(input('Please input c>>>'))
D = b**2 - (4*a*c)

if a != 0:
    min_at = -b/(2*a)
    x = np.linspace(min_at-b,min_at+b,700)
else:
    x = np.linspace(-10,10)

y1 = a*(x**2)+b*x+c

if a > 0:
    X = np.linspace(-y1[0],y1[0],2)
elif a == 0:
	if b > 0:
		X = np.linspace(y1[0],y1[-1],2)
	else:
		X = np.linspace(-y1[0],-y1[-1],2)
else:
    X = np.linspace(y1[0],-y1[0],2)
y = np.linspace(0,0,2)

if a != 0:
    if D == 0:
        x = (-b)/(2*a)
        print('The roots are real, repeating and are equal to')
        print(x)
    elif D < 0:
        print('The roots are imaginary')
    else:
        x1 = (-b + (D**0.5))/(2*a)
        x2 = (-b - (D**0.5))/(2*a)
        print('The roots are real, and are')
        print(x1, x2)
else:
    print('This is a linear equation')

plt.plot(X,y,color='grey')		#plots x axis
plt.plot(y,X,color='grey')		#plots y axis
plt.plot(x,y1,color='magenta')
plt.show()