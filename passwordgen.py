import random

print('Welcome to the password generator.')
leng = int(input('Enter the desired length for a password>>> '))
pw = ''

for i in range(leng):
	k = random.randint(33, 126)
	pw += chr(k)
	
if leng <= 8:
	print 'This will be a weak password'
elif leng > 8 and leng <= 14:
	print 'This will be a strong password'
else:
	print 'This will be a very strong password'
	
pw