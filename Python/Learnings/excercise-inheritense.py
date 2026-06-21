# create a class 2-d vector and use it to create another class representing a 3-d vector
class v2:
  def __init__(self,i,j):
    self.i = i
    self.j = j
  def __str__(self):
    return f"{self.i}i + {self.j}j"
class v3(v2):
  def __init__(self, i, j, k):
    super().__init__(i,j)
    self.k = k
  def __str__(self):
    return f"{self.i}i + {self.j}j + {self.k}k"
v2d = v2(1,2)
v3d = v3(3,2,1)
print(v2d)
print(v3d)

# create a class pets from a class animal and further create dog from pets add a method bark to class dog.
class Animals:
  animalType = "Mammal"
class Pets:
  color = "White"
class Dog:
  @staticmethod
  def bark(): #method
    print("Bow Bow")
d = Dog()
d.bark()

# create a class employee and add salary and increment properties to it.
class Employee:
  salary = 1000
  increment = 1.5
  @property
  def salaryAfterIncrement(self):
    return self.salary * self.increment
  @salaryAfterIncrement.setter
  def salaryAfterIncrement(self,sai):
    self.increment = sai / self.salary
e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 2000
print(e.increment)
