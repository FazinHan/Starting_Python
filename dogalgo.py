age = int(input('Age of your dog: '))
print 
if age <= 0:
	print('That can hardly be true!')
elif age == 1:
	print('About 14 hooman years.')
elif age == 2:
	print('About 22 hooman years.')
else:
	hooman = 22 + (age-2)*5
	print(f'About {hooman} human years.')
###

inrd = input('Press enter to quit>')