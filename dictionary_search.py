def __fib__(n):
	num1 = 0
	num2 = 1
	num3 = 1
	for i in range(n):
		num3 = num1 + num2		
		num1 = num2				
		num2 = num3
	return num3

def __bisearch__(n, req):
	q = len(req)
	for i in range(q):
		a = len(req)/2
		if req[a] == n:
			return True
			break
		elif req[a] > n:
			req = req[len(req)/2:len(req)]
			continue
		elif req[a] < n:
			req = req[0:len(req)/2]
			continue
		if len(req) == 0:
			return False
			break

p = 1000
roger = None
dictionary = []

for i in range(p):
	dictionary.append(fib(i))

print('Welcome to the search program')