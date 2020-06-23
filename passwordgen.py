import random

print('Welcome to the password generator.')
print('WARNING: UNSUITABLE FOR USE AS A SOURCE OF SECURE PASSWORDS \nDUE TO PSEUDO-RANDOM NUMBER GENERATOR USED')
leng = int(input('Enter the desired length for a password>>> '))
pw = ''

for i in range(leng):
	k = random.randint(33, 126)
	pw += chr(k)
	
if leng <= 8:
	print('This will be a weak password')
elif leng > 8 and leng <= 14:
	print('This will be a strong password')
elif leng >= 100 and leng < 500:
	print('You\'re crazy. You can\'t possibly remember that')
elif leng >= 500:
	print('You son of a gun (or daughter, I hold no biases)')
else:
	print('This will be a very strong password')
	
pw