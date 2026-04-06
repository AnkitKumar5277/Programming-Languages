# Python Program to Illustrate Different Set Operations
# Program to perform different set operations like in mathematics
# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};
# set union
print("Union of E and N is",E | N)
# set intersection
print("Intersection of E and N is",E & N)
# set difference
print("Difference of E and N is",E - N)
# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)
# # output
# Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}
# Intersection of E and N is {2, 4}
# Difference of E and N is {8, 0, 6}
# Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)
