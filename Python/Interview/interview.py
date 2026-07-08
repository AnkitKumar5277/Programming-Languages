# String ko reverse kaise karte hain?
text = "Python"
print(text[::-1])
nohtyP

# Instance variables
class Student:
def __init__(self, name, age):
  self.name = name # instance variable
  self.age = age # instance variable
s1 = Student("Rahul", 20)
s2 = Student("Ankit", 22)
print(s1.name) # Rahul
print(s2.name) # Ankit

# Encapsulation 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # Private
    def show_marks(self):
        print("Marks:", self.__marks)
s1 = Student("Ankit", 90)
print(s1.name)      # Allowed
s1.show_marks()     # Allowed
# Ankit
# Marks: 90

# Data abstraction
class Car:
    def start(self):
        print("Car started")
    def drive(self):
        print("Car is driving")
my_car = Car()
my_car.start() # user use only
my_car.drive() # user use only
# Car started
# Car is driving

# Polymorphism
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d = Dog()
c = Cat()
d.sound()
c.sound()
# Dog barks
# Cat meows

# class attribute / instance attribute
class Sample:
    name = "ankit"   # Class attribute
# Create object (instance)
obj = Sample()
# Create an instance attribute (does not change the class attribute)
obj.name = "vikky"
# Change the class attribute
Sample.name = "rohit"
print("Class Attribute:", Sample.name)
print("Instance Attribute:", obj.name)
# Class Attribute: rohit
# Instance Attribute: vikky

class Employee:
  company = "IBM"
  def getSalary(self):
    print(f"employee of {self.company} is {self.salary}")
ankit = Employee()
ankit.salary = 100000
ankit.getSalary() # Employee.getSalary(ankit) #print the function components
# employee of IBM is 100000

# constructor \ dunder method
class Employee:
    company = "Google"   # Class attribute
    def __init__(self, name, salary, subunit):
        self.name = name          # Instance attribute
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
    def getDetails(self):
        print(f"Name    : {self.name}")
        print(f"Salary  : {self.salary}")
        print(f"Subunit : {self.subunit}")
        print(f"Company : {self.company}")
# Creating objects
emp1 = Employee("Harry", 100, "YouTube")
emp1.getDetails()
print()
emp2 = Employee("Ankit", 50000, "QA Automation")
emp2.getDetails()

# Single inheritence
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")
d = Dog()
d.sound()  # Inherited method
d.bark()   # Dog's own method

# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):   # Same method name and parameters
        print("Dog barks")  # Different behavior
a = Animal()
d = Dog()
a.sound()   
d.sound() 

# Method overloading
# ❎ Method overloading 
# ✅ default arguments ya *args
class Calculator:
    def add(self, a, b=0):
        return a + b
c = Calculator()
print(c.add(10))      # One argument
print(c.add(10, 20))  # Two arguments

# super() method 
super().__init__()
# __init__() Calls constructor of the base class

# Example 1: Parent Constructor Call 
class Animal:
    def __init__(self):
        print("Animal Constructor")
class Dog(Animal):
    def __init__(self):
        super().__init__()   # Parent constructor call
        print("Dog Constructor")
d = Dog()
# Example 2: Parent Method Call
class Animal:
   def sound(self):
       print("Animal makes a sound")
class Dog(Animal):
   def sound(self):
       super().sound()      # Parent method call
       print("Dog barks")
d = Dog()
d.sound()

# CLASS METHOD
class Student:
    school = "ABC School"   # class attribute
    @classmethod
    def changeSchool(cls, new_school):
        cls.school = new_school
# Before change
print(Student.school)
# Change using class method
Student.changeSchool("XYZ School")
# After change
print(Student.school)
# ABC School
# XYZ School

# *Decorator
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper
# function to decorate
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

# exception handling
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
def greet():
    print("Hello Ankit!")

# IF __NAME__== ‘__MAIN__’ 
def greet():
    print("Hello Ankit!")
if __name__ == "__main__":
    greet()


# LOCAL VARIABLE
def display():
    name = "Ankit"   # Local variable
    print(name)
display()
# print(name)   # Error: name is not defined


# Global variable
name = "Ankit"   # Global variable
def display():
    print(name)
display()
print(name)


# Lambda function
square = lambda x: x*x
print(square(5)) # 25


import copy
list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)   # Shallow Copy
list2[0][0] = 100
print("Original:", list1)
print("Copy:", list2)

# map function
nums = [1,2,3]
print(list(map(lambda x:x*2, nums))) 
# [2, 4, 6]


# generator 
def num():
    yield 1
    yield 2
for i in num():
    print(i)
# 1
# 2

# iterator
numbers = [10, 20, 30]
itr = iter(numbers)
print(next(itr)) # 10
print(next(itr)) # 20
print(next(itr)) # 30 


# *args` aur `**kwargs
def add(*args):
   print(args)
add(1,2,3)
def user(**kwargs):
   print(kwargs)
user(name="Ankit", age=22)
# (1, 2, 3)
# {'name': 'Ankit', 'age': 22}
