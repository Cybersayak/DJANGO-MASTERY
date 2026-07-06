# ================================
# TUPLE IN PYTHON
# ================================

# Creating an empty tuple
t = ()
print(type(t))

# Creating tuples
numbers = (10, 20, 30, 40, 50)
fruits = ("Apple", "Banana", "Mango")

print("\nOriginal Tuple:")
print(numbers)

# ------------------------------
# Accessing Elements
# ------------------------------
print("\nAccessing Elements")

print(numbers[0])      # First element
print(numbers[-1])     # Last element
print(numbers[1:4])    # Slicing

# ------------------------------
# Length
# ------------------------------
print("\nLength")
print(len(numbers))

# ------------------------------
# Membership
# ------------------------------
print("\nMembership")

print(30 in numbers)
print(100 in numbers)

# ------------------------------
# Iterating
# ------------------------------
print("\nIteration")

for item in numbers:
    print(item)

# ------------------------------
# Tuple Packing
# ------------------------------
print("\nTuple Packing")

student = ("John", 21, "CSE")
print(student)

# ------------------------------
# Tuple Unpacking
# ------------------------------
print("\nTuple Unpacking")

name, age, dept = student

print(name)
print(age)
print(dept)

# ------------------------------
# Extended Unpacking
# ------------------------------
print("\nExtended Unpacking")

data = (1, 2, 3, 4, 5)

a, *middle, b = data

print(a)
print(middle)
print(b)

# ------------------------------
# Concatenation
# ------------------------------
print("\nConcatenation")

t1 = (1, 2, 3)
t2 = (4, 5)

print(t1 + t2)

# ------------------------------
# Repetition
# ------------------------------
print("\nRepetition")

print((1, 2) * 3)

# ------------------------------
# count()
# ------------------------------
print("\ncount()")

x = (1, 2, 3, 2, 2, 5)

print(x.count(2))

# ------------------------------
# index()
# ------------------------------
print("\nindex()")

print(x.index(3))

# ------------------------------
# Nested Tuple
# ------------------------------
print("\nNested Tuple")

nested = ((1, 2), (3, 4), (5, 6))

print(nested)
print(nested[1])
print(nested[1][0])

# ------------------------------
# min(), max(), sum()
# ------------------------------
print("\nmin(), max(), sum()")

nums = (5, 8, 2, 11, 4)

print(min(nums))
print(max(nums))
print(sum(nums))

# ------------------------------
# sorted()
# ------------------------------
print("\nsorted()")

print(sorted(nums))
print(sorted(nums, reverse=True))

# ------------------------------
# tuple() Constructor
# ------------------------------
print("\ntuple() Constructor")

my_list = [100, 200, 300]

new_tuple = tuple(my_list)

print(new_tuple)

# ------------------------------
# Converting Tuple to List
# ------------------------------
print("\nTuple -> List")

temp = list(numbers)

print(temp)

temp.append(60)

numbers = tuple(temp)

print(numbers)

# ------------------------------
# Immutability
# ------------------------------
print("\nTuple Immutability")

sample = (10, 20, 30)

try:
    sample[0] = 100
except TypeError as e:
    print(e)

# ------------------------------
# Single Element Tuple
# ------------------------------
print("\nSingle Element Tuple")

a = (5)

b = (5,)

print(type(a))
print(type(b))

# ------------------------------
# Deleting Tuple
# ------------------------------
print("\nDeleting Tuple")

demo = (1, 2, 3)

print(demo)

del demo

# print(demo)   # NameError

# ======================================================
# LIST vs TUPLE vs SET
# ======================================================

print("\n==============================")
print("LIST vs TUPLE vs SET")
print("==============================")

my_list = [10, 20, 20, 30]
my_tuple = (10, 20, 20, 30)
my_set = {10, 20, 20, 30}

print("List :", my_list)
print("Tuple:", my_tuple)
print("Set  :", my_set)

# ------------------------------
# Mutable vs Immutable
# ------------------------------
print("\nMutability")

my_list[0] = 99
print("Modified List :", my_list)

try:
    my_tuple[0] = 99
except TypeError:
    print("Tuple cannot be modified")

my_set.add(40)
print("Modified Set :", my_set)

# ------------------------------
# Duplicates
# ------------------------------
print("\nDuplicates")

print("List keeps duplicates :", my_list)
print("Tuple keeps duplicates:", my_tuple)
print("Set removes duplicates:", my_set)

# ------------------------------
# Ordering
# ------------------------------
print("\nOrdering")

print("List maintains order :", my_list)
print("Tuple maintains order:", my_tuple)
print("Set order is not guaranteed:", my_set)

# ------------------------------
# Indexing
# ------------------------------
print("\nIndexing")

print(my_list[1])
print(my_tuple[1])

try:
    print(my_set[1])
except TypeError as e:
    print(e)

# ------------------------------
# Adding Elements
# ------------------------------
print("\nAdding Elements")

my_list.append(50)
print(my_list)

my_set.add(50)
print(my_set)

print("Tuple has no append() method.")

# ------------------------------
# Removing Elements
# ------------------------------
print("\nRemoving Elements")

my_list.remove(20)
print(my_list)

my_set.remove(20)
print(my_set)

print("Tuple has no remove() method.")

# ======================================================
# Important Built-in Functions
# ======================================================

print("\nImportant Built-in Functions")

marks = (80, 90, 70, 95)

print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks))
print(any(marks))
print(all(marks))

# ======================================================
# Tuple Methods (Only Two!)
# ======================================================

print("\nTuple Methods")

t = (10, 20, 20, 30, 40)

print("count:", t.count(20))
print("index:", t.index(30))

# ======================================================
# Summary
# ======================================================

print("\n========== SUMMARY ==========")

print("""
LIST
-----
✔ Mutable
✔ Ordered
✔ Allows duplicates
✔ Supports indexing
✔ Many methods

TUPLE
------
✔ Immutable
✔ Ordered
✔ Allows duplicates
✔ Supports indexing
✔ Only 2 methods:
    - count()
    - index()

SET
----
✔ Mutable
✔ Unordered
✔ No duplicates
✔ No indexing
✔ Fast searching
""")