# Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))

# Python Program to Convert Decimal to Binary, Octal and Hexadecimal
# Python program to convert decimal into other number systems
dec = int(input("Enter No."))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

a = 10          # int
b = 3.14        # float
c = "Ankit"     # string
d = [1, 2, 3]   # list
e = (4, 5, 6)   # tuple
f = {7, 8, 9}   # set
g = {'name': 'John', 'age': 20}  # dict
h = True        # boolean
i = None        # none

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

celsius = float(input("Enter: "))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))



num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

a = 10
b = 10
print(a is b)  # Output: True (because small integers share the same memory in Python)

x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)



name = "Hello"
print("H" in name)  # Output: True

# Valid identifiers
my_name = "John"
_age = 20
marks1 = 88

#Addition and Subtraction
x = x + y
y = x - y
x = x - y
#Multiplication and Division
x = x * y
y = x / y
x = x / y
XOR swap

#This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y

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
