


'''

# 4. write a class complex to represent complex numbers along with overload operators + and * which adds and multiples then.

# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
'''
class Complex:
    def __init__(self, r, i):
        self.real = r 
        self.imaginary = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        mulReal =  self.real*c.real - self.imaginary*c.imaginary
        mulImg =  self.real*c.imaginary + self.imaginary*c.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"
c1 = Complex(1, -4)
c2 = Complex(331, -37)
print(c1 + c2)
print(c1 * c2)
'''

# 5. write a class complex to represent complex numbers, along with overloaded operators + and * which adds and multiplies them
'''
class Vector:
  def __init__(self, vec):
     self.vec = vec

  def __str__(self):
    str1 = ""
    index = 0
    for i in self.vec:
      str1 += f"{i}a{index} +"
      index += 1
    return str1[:-1]
  def __add__(self,vec2):
    newList = []
    for i in range(len(self.vec)):
      newList.append(self.vec[i] + vec2.vec[i])
    return Vector(newList)

  def __mul__(self, vec2):
    sum = 0
    for i in range(len(self.vec)):
      sum += self.vec[i] * vec2.vec[i]
    return sum

v1 = Vector([1,4,6])
v2 = Vector([1,6,9])
print(v1 + v2)
print(v1 * v2)
 '''

# 6.write __str__() method to print the vector as follows:
# 7i cap + 8j cap + 10k cap
# assume vector of dimension 3 for this problem
'''
class Vector:
  def __init__(self,vec):
    self.vec = vec

  def __str__(self):
    return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
    
v1 = Vector([1,4,6])
v2 = Vector([1,6,9])
print(v1)
print(v2)
'''

# 7. overide the __len__() method on vector of problem 5 to display the dimension of the vector.
'''
class Vector:
    def __init__(self, vec):
       self.vec = vec
  
    def __str__(self):
        str1 = "" 
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
      
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 6])
v2 = Vector([1, 6, 9])
print(len(v1))
print(len(v2))
'''
