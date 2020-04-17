def lp(a):
	if a % 4 == 0 and a % 400 != 0:
		print a, "is a leap year"
	else:
		print a, "is not a leap year"