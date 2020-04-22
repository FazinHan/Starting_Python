def __conv(a, b, n):
	if n == 10:
		p = str(int(a, b))
		return p
	else:	
		s = int(a, b)
		res = []
		p = ''
		d = s 
		while d > 0:
			e = d%n
			d /= n
			if e > 9:
				e += 55
				e = chr(e)
				res.append(e)
			else:
				res.append(e)
		for j in range(len(str(d))):
			p += str(res[j])
		return p

for r in range(15):
	print('I convert numbers into different forms')
	inp_ = raw_input('Please enter the number you want converted>>> ')
	inp = str(inp_)
	bas_ = raw_input('Please enter the base of the number entered>>> ')
	bas = int(bas_)
	req_ = int(input('Enter the base you want it converted to:\n(between 2 and 90, and 0 to re-enter values)>>> '))
	if (req_ < 2 or req_ > 90) and req_ != 0:
		print 'Please recheck the desired base'
		break
	elif req_ == 0:
		pseudo = 1
	else:
		q = __conv(inp, bas, req_)
		print q
		break