import numpy as np

a = []							#placeholder
b = 0.0							#number of events
r = 500000*2					#iterations

for i in range(r):
	a = np.random.uniform(-0.5, 0.5, 2)
	d = a[0]**2 + a[1]**2
	if d <= 0.5**2:
		b += 1.0

(b/r)*4.0