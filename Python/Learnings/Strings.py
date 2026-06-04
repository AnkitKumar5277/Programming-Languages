name = "This is a Big line"
print(type(name))
name = name + str(1)  # can only concatenate str (not "int") to str
print(name)
# This is a Big line1

a = "ankit"
b = "kumar"
c = a + " "+ b
print(c)
# ankit kumar

print("Pramod", 123, "Amit", "John", sep='*',end="      ")
print("Pramod", 123, "Amit", "John", sep='*')
# Pramod*123*Amit*John      Pramod*123*Amit*John

# Program to find the ASCII value of the given character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
