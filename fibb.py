def fib(n):
	num1 = 0
	num2 = 1
	num3 = 1
	for i in range(n):
		print num3
		num3 = num1 + num2		#new number becomes previous plus current number
		num1 = num2				#previous number becomes current number
		num2 = num3				#current number becomes new number

a = input('Enter the number of positions \nto which Fibonacci numbers \nshould be displayed: ')
fib(a)