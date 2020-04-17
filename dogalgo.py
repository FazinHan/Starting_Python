age = input('Age of your dog: ')
print 
if age <= 0:
	print 'That can hardly be true!'
elif age == 1:
	print 'About 14 hooman years.'
elif age == 2:
	print 'About 22 hooman years.'
else:
	hooman = 22 + (age-2)*5
	print 'About', hooman, 'human years.'
###

raw_input('Press enter to quit>')