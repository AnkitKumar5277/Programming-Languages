# split()
x = "this is example of split method"
a = x.split()
print(a)
# ['this', 'is', 'example', 'of', 'split', 'method']

# ✅ str.format()
name = "Alice"
age = 25
# print("My name is {} and I'm {} years old”.format(name, age))
# Output: My name is Alice and I'm 25 years old

# ✅ f-strings (Python 3.6+):
name = "Charlie"
age = 35
print(f"My name is {name} and I'm {age} years old.") 
# Output: My name is Charlie and I'm 35 years old.

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
