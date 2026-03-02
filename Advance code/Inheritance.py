# INHERITENSE
# single inhertense
class Employee:
  company = "Google"
  def showDetails(self):
    print("This is an employee")
class Programmer(Employee):
  language = "Python"
  company = "Microsoft"
  def getLanguage(self):
    print(f"the language is {self.language}")
  def showDetails(self):
    print("this is an programmer")
e = Employee()
e.showDetails()
print(e.company)
p = Programmer()
p.showDetails()
print(p.company)
print(p.language)

# multiple iheritense
class Freelancer:
  company = "Fiverr"
  level = 0
  def upgradeLevel(self):
    self.level = self.level + 1
class Employee:
  company = "Visa"
  eCode = 130
class Programmer(Freelancer, Employee):
  name = "ankit"
p = Programmer()
p.upgradeLevel()
print(p.company)
print(p.eCode)

# multilevel inhertense
class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")
class Employee(Person):
    company = "Honda"
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def takeBreath(self):
        print("I am an Employee so I am luckily breathing..")
class Programmer(Employee):
    company = "Fiverr"
    def getSalary(self):
        print(f"No salary to programmers")
    def takeBreath(self):
        print("I am a Progarmmer so I am breathing++..")
p = Person()
p.takeBreath()
# print(p.company) # throws an error
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

# super method
class Person:
  country = "India"
  def __init__(self):
    print("Initializing Person ..\n")
  def takebreath(self):
    print("i am breathing")
class Employee(Person):
  company = "Honda"
  def __init__(self):
    # super().__init__()
    print("Initializing Employee..\n")
  def getSalary(self):
    print(f"salary is {self.salary}")
  def takebreath(self):
    super().takebreath()
    print("i am an employee so i am luckily breathing")
class Programmer(Employee):
  company = "Fiverr"
  def __init__(self):
    # super().__init__()
    print("Initializing Programmer..\n")
  def getSalary(self):
    print(f"No salary to programmer")
  def takebreath(self):
    super().takebreath()
    print("i am a programmer so i am breathing ++")
p = Person()
p.takebreath()
e = Employee()
e.takebreath()
pr = Programmer()
pr.takebreath()

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

# ❎ Method overloading 
# ✅ default arguments ya *args
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
c1 = Calculator()
print(c1.add(5, 3))      # 2 arguments
print(c1.add(5, 3, 2))   # 3 arguments

# class method is brother of static method
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


# property method / getter
'''
class Employee:
  company = "Bharat Gas"
  salary = 5600
  salarybonus = 400
  @property
  def totalSalary(self):
    return self.salary + self.salarybonus
 
e = Employee()
print(e.totalSalary)
# e.totalSalary = 5000 -> does not change we need to setter
'''

# setter method ->
'''
class Employee:
  company = "Bharat Gas"
  salary = 5600
  salarybonus = 400
  #totalSalary = 6100

  @property
  def totalSalary(self):
    return self.salary + self.salarybonus

  @totalSalary.setter
  def totalSalary(self,val):
    self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary) 
e.totalSalary = 5800
print(e.salary)
print(e.salarybonus)
'''

# operator overloading
'''
class Number:
  def __init__(self, num):
    self.num = num
  
  def __add__(self, num2):
    print("lets add")
    return self.num + num2.num
    
  def __mul__(self, num2):
    print("lets multiply")
    return self.num * num2.num

n1 = Number(4)
n2 = Number(6)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
'''

# other dunder method
'''
class Number:
  def __init__(self, num):
    self.num = num

  def __add__(self,num2):
    print("lets")

  def __mul__(self,num2):
    print("lets add")
    return self.num * num2.num

  def __str__(self):
    return f"Decimal Number: {self.num}"

  def __len__(self):
    return 1

n = Number(9)
print(n)
print(len(n))
 ''' 








