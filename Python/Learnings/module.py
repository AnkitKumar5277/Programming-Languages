radius = 2
import math
print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is -> ", area)
# 3.141592653589793
# 4.0
# Area of the circle is ->  12.566370614359172

# Program to display calendar of the given month and year
import calendar
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))
# output
#    November 2014
# Mo Tu We Th Fr Sa Su
#              1  2
# 3  4  5  6 7  8  9
# 10 11 12 13 14 15 16
# 17 18 19 20 21 22 23
# 24 25 26 27 28 29 30

import random 
print(random.randint(0,9))  #random.randint(a,b)

import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
# The solutions are (-3+0j) and (-2+0j)

import cmath  
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return [root1, root2]
