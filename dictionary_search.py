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
	q = req
	a = len(q)//2
	for i in range(len(req)):
		if q[a] == n:
			return True
			break
		elif q[a] < n:
			q = q[len(q)//2:len(q)]
			a = len(q)//2
		elif q[a] > n:
			q = q[0:len(q)//2]
			a = len(q)//2
		elif len(q) == 0:
			return False
			break

p = 1000
dictionary = []

for i in range(p):
	dictionary.append(__fib__(i))

print('Welcome to the search program')
print('A certain dictionary of numbers has been determined')
query = int(input('Enter the natural number you\'d like checked>>> '))
if query > __fib__(p):
	print('That number is outside the range of the dictionary')
else:
	roger = __bisearch__(query, dictionary)
	
if roger == True:
	print('That number exists in the dictionary :-)')
else:
	print('That number does not exist in the dictionary :\'(')