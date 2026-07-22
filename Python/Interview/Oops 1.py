# class
class Number:
  def sum(self);
    return self.a + self.b
n = number() # object instantiation
n.a = 4
n.b = 6
s = n.sum()
print(s)
# 10


class RailwayForm:
  formType = "RailwayForm"
  def printData(self):
      print(f"Name is {self.name}")
      print(f"Train is {self.train}")
      
ankitApp = RailwayForm()
ankitApp.name = "ankit"
ankitApp.train = "Rajdhani Express"
ankitApp.printData() 
# Name is ankit
# Train is Rajdhani Express


# Instance variables
class Student:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
s1 = Student("Rahul", 20)
s2 = Student("Ankit", 22)
# Accessing instance variables
print(s1.name)  # Rahul
print(s2.name)  # Ankit
# Rahul
# Ankit


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
obj = Sample() # Create object (instance)
obj.name = "vikky" # Create an instance attribute (does not change the class attribute)
Sample.name = "rohit" # Change the class attribute
print("Class Attribute:", Sample.name)
print("Instance Attribute:", obj.name)
# Class Attribute: rohit
# Instance Attribute: vikky


# self
class Employee:
  company = "IBM"
  def getSalary(self):
    print(f"employee of {self.company} is {self.salary}")
ankit = Employee()
ankit.salary = 100000
ankit.getSalary() # Employee.getSalary(ankit) #print the function components
# employee of IBM is 100000


# static method
class Person:
  company = "Adobe"
  @staticmethod  # mark decorate
  def greet():
    print("Good Morining, Sir")
ankit = Person()
Person.greet() #--> this is the statice method run code
ankit.greet()
# Good Morining, Sir
# Good Morining, Sir


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

# Employee is created!
# Name    : Harry
# Salary  : 100
# Subunit : YouTube
# Company : Google

# Employee is created!
# Name    : Ankit
# Salary  : 50000
# Subunit : QA Automation
# Company : Google
