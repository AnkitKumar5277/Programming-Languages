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

