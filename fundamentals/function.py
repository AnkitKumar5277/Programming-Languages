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
