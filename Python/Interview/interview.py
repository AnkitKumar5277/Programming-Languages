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

