def __conv(a, b, n):
	a = str(a)
	s = int(a, b)
	if n == 10:
		return s
	else:	
		res = []
		p = ''
		d = s 
		while d > 0:
			e = d%n
			d /= n
			if e > 9:
				e += 55
				e = chr(e)
				res += [e]
			else:
				res += [e]
		res.reverse()
		for j in range(len(res)):
			p += str(res[j])
		return p

for r in range(15):
	print('I convert numbers into different forms')
	inp = str(raw_input('Please enter the number you want converted>>> '))
	bas = int(raw_input('Please enter the base of the number entered>>> '))
	req = int(input('Enter the base you want it converted to:\n(between 2 and 90, and 0 to re-enter values)>>> '))
	if (req < 2 or req > 90) and req != 0:
		print 'Please recheck the desired base'
		break
	elif req == 0:
		pseudo = 1
	else:
		print __conv(inp, bas, req)
		break
qwe = input('Press enter to continue')