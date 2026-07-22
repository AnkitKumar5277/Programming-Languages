# map function 
def square(num):
    return num * num
numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))
# [1, 4, 9, 16, 25]

# filter function
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# reduce functoin
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)
# 10

# Generator function
def numbers():
    yield 1
    yield 2
    yield 3
gen = numbers()
print(next(gen))   # 1
print(next(gen))   # 2
print(next(gen))   # 3

# iterator
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30

# Positional Arguments
def greet(name, age):
    print(name, age)
greet("Ankit", 22)
# Ankit 22

# Keyword Arguments
def greet(name, age):
    print(name, age)
greet(age=22, name="Ankit")

# Default Arguments
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Ankit")
# Hello Guest
# Hello Ankit

# Variable Length Arguments (*args)
def add(*args):
    print(sum(args))
add(10, 20)
add(10, 20, 30, 40)

# Variable Length Keyword Arguments (**kwargs)
def student(**kwargs):
    print(kwargs)
student(name="Ankit", age=22, city="Delhi")
{'name': 'Ankit', 'age': 22, 'city': 'Delhi'}


