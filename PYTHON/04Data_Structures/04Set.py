# Original Code
list1 = [1, 2, 3, 1, 4, 2, 3, 5, 4, 6]

set1 = set()

for i in list1:
    set1.add(i)

print("Original Set :", set1)
print("As List :", list(set1))

# ==========================================
# Another Set
# ==========================================

set2 = {4, 5, 6, 7, 8, 9}

print("\nSet1 :", set1)
print("Set2 :", set2)

# ==========================================
# 1. add()
# Adds one element
# ==========================================

set1.add(10)
print("\nAfter add(10):", set1)

# ==========================================
# 2. update()
# Adds multiple elements
# ==========================================

set1.update([11, 12, 13])
print("After update([11,12,13]):", set1)

# ==========================================
# 3. remove()
# Removes an element
# Raises KeyError if element doesn't exist
# ==========================================

set1.remove(13)
print("After remove(13):", set1)

# ==========================================
# 4. discard()
# Removes element if present
# Does NOT raise error if absent
# ==========================================

set1.discard(100)
print("After discard(100):", set1)

# ==========================================
# 5. pop()
# Removes a random element
# ==========================================

removed = set1.pop()
print("Popped Element:", removed)
print("After pop():", set1)

# ==========================================
# 6. copy()
# ==========================================

copy_set = set1.copy()
print("\nCopied Set:", copy_set)

# ==========================================
# 7. clear()
# Removes everything
# ==========================================

temp = copy_set.copy()
temp.clear()
print("After clear():", temp)

# ==========================================
# 8. union()
# Combines both sets
# ==========================================

print("\nUnion:")
print(set1.union(set2))
print(set1 | set2)

# ==========================================
# 9. intersection()
# Common elements
# ==========================================

print("\nIntersection:")
print(set1.intersection(set2))
print(set1 & set2)

# ==========================================
# 10. difference()
# Elements only in first set
# ==========================================

print("\nDifference:")
print(set1.difference(set2))
print(set1 - set2)

# ==========================================
# 11. symmetric_difference()
# Elements not common
# ==========================================

print("\nSymmetric Difference:")
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

# ==========================================
# 12. intersection_update()
# Updates original set
# ==========================================

temp = set1.copy()
temp.intersection_update(set2)
print("\nintersection_update():", temp)

# ==========================================
# 13. difference_update()
# ==========================================

temp = set1.copy()
temp.difference_update(set2)
print("difference_update():", temp)

# ==========================================
# 14. symmetric_difference_update()
# ==========================================

temp = set1.copy()
temp.symmetric_difference_update(set2)
print("symmetric_difference_update():", temp)

# ==========================================
# 15. isdisjoint()
# True if no common elements
# ==========================================

print("\nisdisjoint():")
print(set1.isdisjoint(set2))

# ==========================================
# 16. issubset()
# ==========================================

small = {4, 5}
print("\nissubset():")
print(small.issubset(set2))
print(small <= set2)

# ==========================================
# 17. issuperset()
# ==========================================

print("\nissuperset():")
print(set2.issuperset(small))
print(set2 >= small)

# ==========================================
# 18. Membership
# ==========================================

print("\nMembership:")
print(5 in set1)
print(20 in set1)
print(100 not in set1)

# ==========================================
# 19. Length
# ==========================================

print("\nLength:")
print(len(set1))

# ==========================================
# 20. Looping
# ==========================================

print("\nLooping through set:")
for item in set1:
    print(item)

# ==========================================
# 21. Creating sets from different iterables
# ==========================================

numbers = set([1, 2, 2, 3, 3])
letters = set("banana")

print("\nFrom List:", numbers)
print("From String:", letters)

# ==========================================
# 22. Frozen Set (Immutable Set)
# ==========================================

frozen = frozenset([1, 2, 3, 4])

print("\nFrozen Set:", frozen)

# frozen.add(5)   # Error
# frozen.remove(1) # Error

# ==========================================
# 23. Set Comprehension
# ==========================================

square_set = {x * x for x in range(1, 6)}

print("\nSet Comprehension:")
print(square_set)

# ==========================================
# 24. Removing duplicates from a list
# ==========================================

list2 = [1, 2, 2, 3, 3, 4, 5, 5]
unique = list(set(list2))

print("\nUnique List:")
print(unique)