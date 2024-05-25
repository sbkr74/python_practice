# set operations
a = {0,2,4,6,8}
b = {1,2,3,5,4}
all = a.union(b)
print(all)
common = a.intersection(b)
print(common)

# Difference
diff = a.difference(b)
print(diff)

# symmetric difference
symm_diff = a.symmetric_difference(b)
print(symm_diff)