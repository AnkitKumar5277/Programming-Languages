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

#instance attribute & class attribute
Class Sample 
  name = "ankit"	  # class attribute
obj = Sample() 	  # objects (instances
obj.name = "vikky"	  # instance attribute / you cant change but you add instance attrubute 
sample.name = "vikky" # class attribute / you can change class attrubute 
print(sample.name) 
print(obj.name) 

# self
class Employee:
  company = "IBM"
  def getSalary(self):
    print(f"employee of {self.company} is {self.salary}")
ankit = Employee()
ankit.salary = 100000
ankit.getSalary() # Employee.getSalary(ankit) #print the function components

# static method
class Person:
  company = "Adobe"
  @staticmethod  # mark decorate
  def greet():
    print("Good Morining, Sir")
ankit = Person()
Person.greet() #--> this is the statice method run code
# or ankit.greet()

# another example
class Employee:
  company = "META"
  def getsalary(self, signature):
    print(f"salary of emoplyee {self.company} is {self.salary}\n{signature}")
  @staticmethod
  def greet():
    print("Good Morning, Sir")
  
  @staticmethod
  def time():
    print("10 am")

ankit = Employee()
ankit.salary = 100000
ankit.getsalary("Thanks") # signature passed
ankit.greet() # Employee.greet()
ankit.time()

# constructor
class Programmer:
  company = "Software X"
  def __init__(self, name, salary, pin):
      self.name = name
      self.salary = salary
      self.pin = pin
p = Programmer("Ankit", 10000, 110033)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Shyam", 12000, 24001)
print(r.name, r.salary, r.pin, r.company)

# another example
class Employee:
    company = "Google"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 
    
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        
harry = Employee("Harry", 100, "YouTube")
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
harry.getDetails()
