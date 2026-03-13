# Create a dictionary
my_dict = {"name": "Amit", "age": 20}
# 1. Add new key-value pair
my_dict["city"] = "Delhi"  # New element added
print(my_dict)  # Output: {'name': 'Amit', 'age': 20, 'city': 'Delhi'}
# 2. Update existing key with new value
my_dict["age"] = 21  # Age overwritten
print(my_dict)  # Output: {'name': 'Amit', 'age': 21, 'city': 'Delhi'}
# 3. Add multiple key-value pairs using update()
my_dict.update({"job": "Student", "hobby": "Reading"})
print(my_dict)  # Output: {'name': 'Amit', 'age': 21, 'city': 'Delhi', 'job': 'Student', 'hobby': 'Reading'}

