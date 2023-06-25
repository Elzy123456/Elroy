# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)

symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", symmetric_difference_set)
