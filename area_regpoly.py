import math

print("I find the area of a regular polygon of a defined size")

n = float(input('Enter number of sides of regular polygon>>> '))
l = float(input('Enter side length of regular polygon in units>>> '))
central_angle = (math.pi*2)/n                       #360/n
s_central_angle = math.sin(central_angle)           #sin(360/n)
isoceles_angle = (math.pi - central_angle)/2        #(180 - 360/n)/2 because isoceles
s_isoceles_angle = math.sin(isoceles_angle)         #sine of isoceles angle
d = l * (s_isoceles_angle / s_central_angle)        #sine rule
area = n * (0.5 * (d**2) * s_central_angle)

print(area)

end = input('Press enter to quit')