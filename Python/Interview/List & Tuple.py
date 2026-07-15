# *List - [ ]
my_list = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, [4, 5, 6]]
print(my_list[0])  # prints 1
my_list.append(7)  
my_list[1] = 6   # change element

# LIST COMPREHENSIONS
# [expression for item in list]
numbers = [1, 2, 3, 4, 5]
squares = [n*n for n in numbers]
print(squares)

# Tuple - ()
my_tuple = (1, 2, 3, "four")
print(my_tuple[0])  # 1
my_tuple[1] = 5     # ❌ Error (tuple change nahi hota)

