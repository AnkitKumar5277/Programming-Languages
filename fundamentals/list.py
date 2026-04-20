# write a list comprehension to print a list which contains the multipication table of a user entered number
n = int(input("Enter your number : "))
table = [ n*i for i in range(1,11) ]
print(table)

# write a program to print third fifthe and seventh element from a list using enurmerate function
l = [1,2,3,4,5,6,7,8,9,10]
for index, item in enumerate(l):
  if index == 2 or index == 4 or index == 6:
     # print(index, item)
    print(f"the{index + 1}th element is {item}")

filter(function, iterable)

num = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)

words = ["apple", "banana", "cherry", "kiwi", "grape"]
long_words = list(filter(lambda word: len(word) > 5, words))
print(long_words)

strings = ["hello","", "world", " ", "python", ""]
empty = list(filter(lambda s: s.strip() != "", strings))
print(empty)

num = [-10, -5, 0, 5, 10, 15, -3, 8, -1]
pos = list(filter(lambda x: x>=0, num))
print(pos)

# lambda arguments: expression
# square = lambda x: x**2
# print(square(2))

add = lambda x, y: x + y
print(add(8, 2))

nums = [1,2,3,4]
square = list(map(lambda x: x **2, nums))
print(square)

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

pairs = [(1, 2), (4, 1), (3, 3)]
sort = sorted(pairs, key = lambda x: x[1])
print(sort)

# map function
# map(function, iterable, ...)
num = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, num)
print(list(square))

names = ['john', 'sam', 'linda']
upper_names = map(str.upper, names)
print(list(upper_names))

a = [1, 2, 3]
b = [4, 5, 6]
sum_ab = map(lambda x, y: x + y, a, b)
print(list(sum_ab))

string_numbers = ['1', '2', '3']
integers = map(int, string_numbers)
print(list(integers))

words = ["python", "data", "science", "analytics"]
lengths = map(len, words)
print(list(lengths))

from functools import reduce

# reduce(function, iterable[, initializer])
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

num = [1,2,3,4,5]
result = reduce(lambda x,y: x * y, num)
print(result)

num = [3,7,2,8,5]
max = reduce(lambda x, y: x if x > y else y, num)
print(max)

num = [1,2,3,4,5]
result = reduce(lambda x, y: x+y, num, 10)
print(result)


# Python Program to Flatten a Nested List
# Example 1: Using List Comprehension
my_list = [[1],[2,3],[4,5,6,7]]
flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]

# Example 2: Using Nested for Loops (non pythonic way)
my_list = [[1],[2,3],[4,5,6,7]]
flat_list[]
for sublist in my_list:
  for num in sublist:
    flat_list.append(num)
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]

# Python Program to Find Numbers Divisible by Another Number
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)
# Numbers divisible by 13 are [65, 39, 221]

# list comprehension
l = ["13", "16", "1", "5", "8"]
l = [int(x) for x in l] 
l.sort()                
print(l)                
# Output: [1, 5, 8, 13, 16]

# shallow copy aur deep copy ka difference
import copy
# Original list
original = [1, 2, [3, 4]]
# Shallow copy
shallow_copy = copy.copy(original)
# Deep copy
deep_copy = copy.deepcopy(original)
# Modify the nested list in the original
original[2][0] = 99
print("Original:", original)         # Output: [1, 2, [99, 4]]
print("Shallow copy:", shallow_copy) # Output: [1, 2, [99, 4]] (nested list is affected)
print("Deep copy:", deep_copy)       # Output: [1, 2, [3, 4]] (nested list is unchanged)

# map function
# Define a function to square a number
def square(num):
    return num * num
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Use map() to apply square function to each number
squared_numbers = list(map(square, numbers))
# Print the result
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0
# Use filter() to get only even numbers
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# reduce
from functools import reduce
# Example 1: Sum all numbers in a list
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 10 (1+2+3+4)
# Example 2: Multiply all numbers in a list
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24 (1*2*3*4)

# iterator concept
# Create a list (iterable)
my_list = [1, 2, 3]
# Turn list into an iterator
my_iterator = iter(my_list)
# Get elements one by one
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
# If you call next() again, it raises StopIteration (no more elements)

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False (lists are different objects in memory)
