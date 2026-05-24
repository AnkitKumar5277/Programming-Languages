# input function
def say_hello_user(name):
    print("Hello,", name)
user_name = input("Enter the name : \n")
say_hello_user(user_name)

# global & local variable
a = 4 # global variable
def func1():
  global a
  print(f"Print statement 1: {a}")
  a = 8 # local variable if global keyword is not used
  print(f"print statement 2: {a}")
func1()
print(f"print statement 3: {a}")

# lambda function
def func(a):
  return a+5
x = 4
print(func(x))
# another method
func = lambda a: a + 8
square = lambda x: x*x
sum = lambda a, b, c: a+b+c
x = 2
print(func(x))
print(square(x))
print(sum(x,1,3))
 
# args = toppings
def make_pizza(*toppings):
    print(toppings)
    for i in toppings:
        print(i)
pramod = make_pizza("tomato","olives", "\n")
jayati = make_pizza("pineapple","olives","corn","paneer", "\n")
vinay = make_pizza("tomato")

# decorator
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
