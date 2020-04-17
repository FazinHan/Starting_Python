print('This is an endeavour to find the largest of three numbers')
a = input('Enter a number')
b = input('Enter another')
c = input('One last please')
d = [a,b,c]
d.sort()
d.reverse()
print d[0]
input('Press enter to continue')