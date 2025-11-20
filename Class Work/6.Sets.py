# -------------------------------------------------------
#               PYTHON SETS – FULL DEMONSTRATION
# -------------------------------------------------------

# 1. Creating Sets
print("1. SET CREATION")
my_set = {1, 2, 3, 4}
empty_set = set()      # {} creates dictionary, so use set()
duplicate_set = {1, 2, 2, 3, 4}

print("Original Set:", my_set)
print("Empty Set:", empty_set)
print("Duplicate Removed Set:", duplicate_set)
print("-" * 50)


# 2. Membership Testing
print("2. MEMBERSHIP TESTING")
print("Is 3 in my_set?", 3 in my_set)
print("Is 5 not in my_set?", 5 not in my_set)
print("-" * 50)


# 3. Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("3. SET OPERATIONS")
print("Set 1:", set1)
print("Set 2:", set2)

# Union
print("Union (set1 | set2):", set1 | set2)

# Intersection
print("Intersection (set1 & set2):", set1 & set2)

# Difference
print("Difference (set1 - set2):", set1 - set2)

# Symmetric Difference
print("Symmetric Difference (set1 ^ set2):", set1 ^ set2)

print("-" * 50)


# 4. Relations Between Sets
print("4. SET RELATION OPERATIONS")

subset_a = {1, 2}
superset_b = {1, 2, 3}

print("Is subset_a subset of superset_b?", subset_a.issubset(superset_b))
print("Is superset_b superset of subset_a?", superset_b.issuperset(subset_a))

# Disjoint
print("Are {1,2,3} and {4,5,6} disjoint?",
      {1, 2, 3}.isdisjoint({4, 5, 6}))

print("-" * 50)


# 5. Built-in Set Methods
print("5. BUILT-IN METHODS")

myset = {1, 2, 3}

myset.add(4)
print("After add(4):", myset)

myset.discard(2)
print("After discard(2):", myset)

removed_item = myset.pop()
print("Random element removed using pop():", removed_item)
print("Set after pop():", myset)

myset.update({10, 20})
print("After update({10,20}):", myset)

temp1 = {1, 2, 3}
temp1.intersection_update({2, 3, 4})
print("After intersection_update():", temp1)

temp2 = {1, 2, 3}
temp2.difference_update({2})
print("After difference_update():", temp2)

temp3 = {1, 2}
temp3.symmetric_difference_update({2, 3})
print("After symmetric_difference_update():", temp3)

print("Copy of myset:", myset.copy())
print("-" * 50)


# 6. Built-in Functions
print("6. BUILT-IN FUNCTIONS")

num_set = {10, 20, 30}
print("len(num_set):", len(num_set))
print("max(num_set):", max(num_set))
print("min(num_set):", min(num_set))
print("sum(num_set):", sum(num_set))
print("sorted(num_set):", sorted(num_set))

print("-" * 50)


# 7. Frozenset (Immutable Set)
print("7. FROZENSET (IMMUTABLE SET)")

frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)

# frozen.add(4)  # This will give error (cannot modify)
print("-" * 50)

print("PROGRAM COMPLETED SUCCESSFULLY!")