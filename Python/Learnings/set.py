
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

print("Union of E and N is",E | N)
# Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8}

print("Intersection of E and N is",E & N)
# Intersection of E and N is {2, 4}

print("Difference of E and N is",E - N)
# Difference of E and N is {8, 0, 6}

print("Symmetric difference of E and N is",E ^ N)
# Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
