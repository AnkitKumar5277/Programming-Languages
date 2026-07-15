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

