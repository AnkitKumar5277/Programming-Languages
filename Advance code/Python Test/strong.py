print("Pramod", 123, "Amit", "John", sep='*',end="      ")
print("Pramod", 123, "Amit", "John", sep='*')

a, b, c = 45, 54, 67
print(a)
print(b)
print(c)
print(a,b,c,sep=" | ")

import keyword
print(keyword.kwlist)

_ = 12
print(_)

a = 10
_ = 45
_ = _+1 
print(_)

abc123 = 78
_pramod = "amit"
_abc = 23
# &123 = 23   x

pi = 3.14
name = "Pramod"
isMale = True

print(type(pi))
print(type(isMale))
print(type(name))

# # Complex numbers - Python - iota
# # i - root to per -1

complex_number = 2 + 3j
print(complex_number.real)
print(complex_number.imag)

b = abs(-10) # Return the absolute value of the argument.
print(b)
c =abs(-9)
print(c)
# 10
# 9

name = "This is a Big line"
print(type(name))
name = name + str(1)  # can only concatenate str (not "int") to str
print(name)

first_name = "Pramod"
last_name = "Dutta"
full_name = first_name + " " + last_name
print(full_name)
print(type(full_name))

a = "ankit"
b = "kumar"
c = a + " "+ b
print(c)

dir = r'C:\pramod\n.txt'
print(dir)

dir = r"C:\pramod\t.txt"
print(dir)

dir = "C:\pramod\t.txt"
print(dir)

print(5 % 2) # Modules
print(5 // 2)

# 2 | 5 | 2 - Quotient
#   | 4 |
# --------
#     1 - Remainder

print(13 // 2)
print(13 % 2)

q, r = divmod(5, 2)
print(q)
print(r)

radius = 2
import math
print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius, 2)
print("Area of the circle is -> ", area)

def greet():
    print("Hello, Welcome to Python World!")
    
greet()
greet()
greet()

print("dasdadads")
greet()

def _123():  # identifier rule is failed
    print("Hi1")


def _():
    print("Hi")


_()
_123()


def pramod123():
    print("Hello")


def h():
    print("hello")
    print("I am part of h function ?")

print("Not a Part of Functions")

def first_part_last_name():
    pass  # # in future i will complete this functions


def greet_to_all_of_you():
    print("Hello, Everyone")


def greet():
    print("Yes")
    greet_to_all_of_you()

greet()

def greet_by_name(name):
    print("Hello,", name)
    print(f"Hello, {name}")

greet_by_name("Pramod")
greet_by_name(123)
greet_by_name(3.14)



def say_hello_user(name):
    print("Hello,", name)
user_name = input("Enter the name : \n")
say_hello_user(user_name)


def print_mul_arguments(*args):
    # *args -> List
    for i in args:
        print(i)
print_mul_arguments("pramod1\n")
print_mul_arguments("pramod", "amit", "lucky")
print_mul_arguments("amit", 10, True, False, "PRAMOD")


def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)
pramod = make_pizza("tomato","olives")
jayati = make_pizza("pineapple","olives","corn","paneer")
vinay = make_pizza("tomato")


def max(*args):
    for i in args:
        print(i)
r1 = max(1, 2, 3, 4, 6)
r2 = max(1, 2, 3)
r2 = max(2, 3)

def outer_function():
    var1 = 30 # local

    def inner_function():
        var2 = 90
        print(var1)

    def inner_function2():
        print(var1)

    inner_function()
    inner_function2()
    # print(var2)

outer_function()
# inner_function()

def add_before_ui_after_ui(func):
     def wrapper():
         print("Before the running UI TC")
         print("Start the Browser ")
         func()
         print("Ending the running UI TC")
         print("Quit the Browser!")
     return wrapper()

@add_before_ui_after_ui
def test_ui():
     print(">> I will Test the UI")


