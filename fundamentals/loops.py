n = 10
n0 = 0
n1 = 1
x = 0
if n <= 0:
  print("enter positive integer:"n,":")
  print(n0)
else:
  print("number in fibonacci sequence upto", n,":")
  while x < n:
    print(n0, end = ',')
    nth = n0 + n1
    n0 = n1
    n1 = nth
    x += 1
  # output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# Define a generator function
def even_numbers():
    num = 0
    while num <= 10:
        yield num  # Pauses here and returns num, then resumes next time
        num += 2
# Use the generator
evens = even_numbers()  # This doesn't run the function yet
# Get values one by one
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
# ... and so on
# Or loop through all
for even in even_numbers():
    print(even)
# Output: 0 2 4 6 8 10

# range vs xrange
numbers = range(1, 6)  # Creates a list: [1, 2, 3, 4, 5]
print("Using range():", list(numbers))  # Prints the full list
print("Memory used by range:", numbers.__sizeof__())  # Shows memory size
numbers_gen = range(1, 6)  # Acts like a generator in Python 3
print("Using xrange-like:", list(numbers_gen))  # Prints: [1, 2, 3, 4, 5]
print("Memory used by xrange-like:", numbers_gen.__sizeof__())  # Less memory

# Python Program to Find Armstrong Number in an Interval
# Program to check Armstrong numbers in a certain interval
lower = 100
upper = 2000
for num in range(lower, upper + 1):
   order = len(str(num))
   # initialize sum
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
   if num == sum:
       print(num)
# #output
# 153
# 370
# 371
# 407
# 1634

while True:
  n1 = int(input("enter: "))
  n2 = int(input("enter: "))
  print(n1 + n2)

# Python Program to Display the multiplication Table
num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
# output
# 12 x 1 = 12
# 12 x 2 = 24
# 12 x 3 = 36
# 12 x 4 = 48
# 12 x 5 = 60
# 12 x 6 = 72
# 12 x 7 = 84
# 12 x 8 = 96
# 12 x 9 = 108
# 12 x 10 = 120

# Python Program to Find HCF or GCD
def compute_hcf(x,y):
  if x>y:
    smaller = y
  else:
    smaller = x
  for i in range(1, smaller+1):
    if((x%i==0) and (y%i==0)):
      hcf = i
      return hcf
num1 = 54
num2 = 24
print("the h.c.f. is", compute_hcf(num1, num2))
# output
# The H.C.F. is 6

# Source Code: Using the Euclidean Algorithm
def compute_hcf(x,y):
  while(y):
    x,y = x&y
  return x
hcf = compute_hcf(300, 400)
print("the hcf is", hcf)
# The HCF is 100



