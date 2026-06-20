#oops example
class Number:
  def sum(self):
    return self.a + self.b
n = Number() # object instantiation
n.a = 4
n.b = 6 
s = n.sum()
print(s)

# PascalCase
# EmployeeName # used in class

# camelCase
'''isNumeric, isFloat'''

# class
'''
class Employee:
include methods & variables'''

# object
class RailwayForm:
  formType = "RailwayForm"
  def printData(self): # using self
    print(f"Name is {self.name}")
    print(f"Train is {self.train}")
    
ankitApp = RailwayForm() # class ka object
ankitApp.name = "ankit"
ankitApp.train = "Rajdhani Express"
ankitApp.printData() # print

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

# Data abstraction 
class Car:
    def start(self):
        print("Car started")
    def drive(self):
        print("Car is driving")
my_car = Car()
my_car.start() # user use only
my_car.drive() # user use only


