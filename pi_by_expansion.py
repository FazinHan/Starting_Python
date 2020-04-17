#pi
#will run for a few seconds

t = 100000000
a = 0.0

for i in range(1, t + 1):
	a += (1.0/(2.0*i-1.0))*((-1)**(i+1))
		
4*a