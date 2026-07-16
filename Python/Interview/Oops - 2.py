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

# Multiple inheritance
class Father:
    def father_method(self):
        print("this is father's method")
class Mother:
    def mother_method(self):
        print("this is mothers method")
class Child(Father, Mother):
    def child_method(self):
        print("this is child's method")
c = Child()
c.father_method()
c.mother_method()
c.child_method()

# Hybrid
class GrandParent:
    def grandparent_method(self):
        print("GrandParent Method")
class Parent1(GrandParent):   # Hierarchical Inheritance
    def parent1_method(self):
        print("Parent1 Method")
class Parent2(GrandParent):   # Hierarchical Inheritance
    def parent2_method(self):
        print("Parent2 Method")
class Child(Parent1, Parent2):   # Multiple Inheritance
    def child_method(self):
        print("Child Method")
obj = Child()
obj.grandparent_method()
obj.parent1_method()
obj.parent2_method()
obj.child_method()

# Multi level inheritance
class Grandfather:
    def show_grandfather(self):
        print("I am Grandfather")
class Father(Grandfather):
    def show_father(self):
        print("I am Father")
class Son(Father):
    def show_son(self):
        print("I am Son")
s = Son()
s.show_grandfather()
s.show_father()
s.show_son()

# Hierarchical Inheritance
class Parent:
    def show_parent(self):
        print("I am Parent")
class Child1(Parent):
    def show_child1(self):
        print("I am Child1")
class Child2(Parent):
    def show_child2(self):
        print("I am Child2")
c1 = Child1()
c2 = Child2()
c1.show_parent()
c1.show_child1()
c2.show_parent()
c2.show_child2()

