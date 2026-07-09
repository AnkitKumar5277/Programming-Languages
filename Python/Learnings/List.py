# enumerate function
list = [2,3,9,3,1]
index = 0 
for item in list:
  print(item, index)
  index += 1
# 2 0
# 3 1
# 9 2
# 3 3
# 1 4

# another second method enumerate function
list = [9,7,4,2]
for index, item in enumerate(list):
  print(item, index)
# 9 0
# 7 1
# 4 2
# 2 3

# comprehension
a = [1,8,3,2,9]
b = []
for item in a:
  if item % 2 == 0:
    b.append(item)
print(b)    
# [8, 2]

# another second method of comprehension
a = [3,9,2,8]
b = [i for i in a if i%2 == 0]
print(b) 
# [2, 8]

# set comprehension
s = [2,9,9,2,4,2,0]
r = {i for i in s}
print(r)
# {0, 9, 2, 4}

# join in list and tuple() and iterate
l = ["Camera", "Laptop", "Phone", "ipad", "Hard disk"]
sentence = " and ".join(l)
print(sentence)
print(" or ".join(l))
print("\n".join(l))
print(type(sentence))
# Camera and Laptop and Phone and ipad and Hard disk
# Camera or Laptop or Phone or ipad or Hard disk
# Camera
# Laptop
# Phone
# ipad
# Hard disk
# <class 'str'>

# reduce
from functools import reduce
sum = lambda a, b: a+b
l = [1,2,3,4]
val = reduce(sum,l)
print(val)
# 10

l = [2,4,6,8,10]
ak = lambda num: num > 7
print(list(filter(ak,l)))
# [8, 10]

# filter
# list(filter(function,l))
def greater_than_5(num):
  if num >5:
    return True
  else:
    return False
l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(greater_than_5,l)))
# [6, 7, 8, 9, 10]

# another method
def square(num):
  return num * num
l = [1,2,4]
print(list(map(square,l)))
# [1, 4, 16]

# map
def square(num):
  return num * num
l = [1,2,4]
l2 = []
for item in l:
  l2.append(square(item))
print(l2)
# [1, 4, 16]

l = [str(i*7) for i in range(1,11)]
print(l)
verticalTable = "\n".join(l)
print(verticalTable)
print("\n".join(l)) # direct method
# ['7', '14', '21', '28', '35', '42', '49', '56', '63', '70']
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70
# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 70

# Create a list
my_list = ["apple", "banana", "orange", "grape"]
# Accessing elements using index
print("First element:", my_list[0])  # Output: apple
print("Last element:", my_list[-1])   # Output: grape (negative index for last element)
# Accessing a range of elements (slicing)
print("First two elements:", my_list[0:2])  # Output: ['apple', 'banana']

# Create an empty list
my_list = []
# Add elements to the list using append()
my_list.append("Apple")
print(my_list)

# write a list comprehension to print a list which contains the multipication table of a user entered number
n = int(input("Enter your number : "))
table = [ n*i for i in range(1,11) ]
print(table)

num = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print(even_numbers)
# [2, 4, 6, 8, 10]

add = lambda x, y: x + y
print(add(8, 2))
# 10

nums = [1,2,3,4]
square = list(map(lambda x: x **2, nums))
print(square)
# [1, 4, 9, 16]

nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
# [2, 4, 6]

pairs = [(1, 2), (4, 1), (3, 3)]
sort = sorted(pairs, key = lambda x: x[1])
print(sort)
# [(4, 1), (1, 2), (3, 3)]

# map function
num = [1, 2, 3, 4, 5]
square = map(lambda x: x**2, num)
print(list(square))
# [1, 4, 9, 16, 25]

names = ['john', 'sam', 'linda']
upper_names = map(str.upper, names)
print(list(upper_names))
# ['JOHN', 'SAM', 'LINDA']

a = [1, 2, 3]
b = [4, 5, 6]
sum_ab = map(lambda x, y: x + y, a, b)
print(list(sum_ab))
# [5, 7, 9]
