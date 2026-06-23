
# PascalCase
# EmployeeName # used in class

# camelCase
'''isNumeric, isFloat'''

# class
'''
class Employee:
include methods & variables'''

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


