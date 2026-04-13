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


# Write a function to check if a number is divisible by five.
# Return True if the number is divisible by 5. Otherwise, return False.
def is_divisible_by_five(number):
    return number % 5 == 0
# Example usage
print(is_divisible_by_five(10))  # True
print(is_divisible_by_five(12))  # False
print(is_divisible_by_five(0))   # True
print(is_divisible_by_five(-15)) # True

# Write a function to find the sum of first N natural numbers.
# Hint: The formula for the sum of the first N natural numbers is N*(N+1)/2.
# For example, for input 5, the outout should be 15.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2  # Using integer division for an exact result
number = 5
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}.")

#challenge
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
# Example usage:
number = 12345
result = sum_of_digits(number)
print(result)  # Output: 15


# The L.C.M. is 216
# Number1 * Number2 = L.C.M. * G.C.D.
# Program to Compute LCM Using GCD
# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
num1 = 54
num2 = 24 
print("The L.C.M. is", compute_lcm(num1, num2))

# Function definition
def greet():
    print("Hello! Welcome to Python functions.")

# Function call
greet()

# 🧱 9️⃣ Base Condition in Recursion
# Concept: Recursion me base condition stopping point hota hai.
def countdown(n):
    if n==0:
        print("Time's up!")
    else:
        print(n)
        countdown(n-1)
countdown(5)

# 🔁 8️⃣ Recursion (Function Calling Itself)
# Concept: Jab ek function apne aap ko call karta hai.
# Example – Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
print("factorial of 5 is:", factorial(5))

# 🧠 7️⃣ Return Statement
# Concept: Function se value return karne ke liye use hota hai.
def square(num):
    return num * num
result = square(6)
print("Square is:", result)

# area_of_triangle
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return round(area, 2)
base = 3
height = 4
print(area_of_triangle(base, height))

# Python Program to Convert Decimal to Binary Using Recursion
def converttobinary(n):
  if n > 1:
    converttobinary(n//2)
  print(n%2, end = '')
dec = 34
converttobinary(dec)
print()
# 100010

# current Python file ke saare global variables aur functions ka dictionary print karta hai.
a = 10
b = 20
print(globals())
