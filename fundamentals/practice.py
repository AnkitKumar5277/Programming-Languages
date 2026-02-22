# Python Program to Count the Number of Each Vowel
# Program to count the number of each vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in
      count[char] += 1
print(count)
# output
# {'a': 2, 'e': 5, 'i': 3, 'o': 5, 'u': 3}

# Write a function to return the first N vowels from a given string.
# Return the first N vowels from the string. If there are fewer than N vowels in the string, return "Not found".
# For example, for input "Hello World", the output should be 'e', 'o', 'o'.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(rows):
  for j in range(i + 1);
    print(j + 1, end = " ")
  print()

# A
# B B
# C C C
# D D D D
# E E E E E
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
  for j in range(i+1):
    alphabet = chr(ascii_value)
    print(alphabet, end=" ")
  ascii_value += 1
  print()

# Programs to print inverted half pyramid using * and numbers
# Example 4: Inverted half pyramid using *
# * * * * *
# * * * *
# * * *
# * *
# *
input = int(input("Enter")
for i in range(input, 0, -1)
  for j in range(0, i):
    print("* ", end = " ")

  print()
