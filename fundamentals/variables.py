a = 10
b = 10
print(a is b)  # Output: True (because small integers share the same memory in Python)

name = "Hello"
print("H" in name)  # Output: True

# Valid identifiers
my_name = "John"
_age = 20
marks1 = 88

# Find square root of real or complex numbers
import cmath
num = 1+2j
num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# Python Program to find the area of triangle
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
