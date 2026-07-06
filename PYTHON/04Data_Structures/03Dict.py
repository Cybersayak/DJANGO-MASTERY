product = {
    "name": "Laptop",
    "brand": "Dell",
    "price": 1200,
    "specs": {
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "512GB"
    }
}

print(product["price"])
print(product["specs"]["ram"])

for key, value in product.items():
    print(key, value)

print(product.values())

print(product.get("gpu"))   # None (safe)

# ==========================================
# 1. Accessing Values
# ==========================================

print("\nAccessing Values")
print(product["name"])
print(product.get("brand"))
print(product.get("gpu", "Not Available"))

# ==========================================
# 2. Adding New Key
# ==========================================

product["color"] = "Silver"

print("\nAfter Adding color")
print(product)

# ==========================================
# 3. Updating Existing Value
# ==========================================

product["price"] = 1300

print("\nAfter Updating price")
print(product)

# ==========================================
# 4. update()
# Add or update multiple keys
# ==========================================

product.update({
    "price": 1400,
    "stock": 25,
    "discount": 10
})

print("\nAfter update()")
print(product)

# ==========================================
# 5. keys()
# ==========================================

print("\nKeys")
print(product.keys())

# ==========================================
# 6. values()
# ==========================================

print("\nValues")
print(product.values())

# ==========================================
# 7. items()
# ==========================================

print("\nItems")
print(product.items())

# ==========================================
# 8. Loop through keys
# ==========================================

print("\nLooping Keys")

for key in product:
    print(key)

# ==========================================
# 9. Loop through values
# ==========================================

print("\nLooping Values")

for value in product.values():
    print(value)

# ==========================================
# 10. Loop through key-value pairs
# ==========================================

print("\nLooping Items")

for key, value in product.items():
    print(key, ":", value)

# ==========================================
# 11. pop()
# Removes specified key
# ==========================================

discount = product.pop("discount")

print("\nRemoved Discount:", discount)
print(product)

# ==========================================
# 12. popitem()
# Removes last inserted key-value pair
# ==========================================

last = product.popitem()

print("\nPopitem:", last)
print(product)

# ==========================================
# 13. del
# ==========================================

del product["color"]

print("\nAfter del color")
print(product)

# ==========================================
# 14. copy()
# ==========================================

product_copy = product.copy()

print("\nCopied Dictionary")
print(product_copy)

# ==========================================
# 15. clear()
# ==========================================

temp = product.copy()

temp.clear()

print("\nAfter clear()")
print(temp)

# ==========================================
# 16. Check if key exists
# ==========================================

print("\nMembership")

print("price" in product)
print("gpu" in product)
print("gpu" not in product)

# ==========================================
# 17. Length
# ==========================================

print("\nLength")

print(len(product))

# ==========================================
# 18. Nested Dictionary
# ==========================================

print("\nNested Dictionary")

print(product["specs"]["processor"])

product["specs"]["ram"] = "32GB"

print(product["specs"])

# ==========================================
# 19. setdefault()
# Adds key only if absent
# ==========================================

product.setdefault("warranty", "1 Year")
product.setdefault("price", 5000)

print("\nAfter setdefault()")
print(product)

# ==========================================
# 20. fromkeys()
# ==========================================

keys = ["Math", "Physics", "Chemistry"]

marks = dict.fromkeys(keys, 0)

print("\nfromkeys()")
print(marks)

# ==========================================
# 21. Dictionary Comprehension
# ==========================================

squares = {x: x*x for x in range(1, 6)}

print("\nDictionary Comprehension")
print(squares)

# ==========================================
# 22. Merge Dictionaries (Python 3.9+)
# ==========================================

dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}

merged = dict1 | dict2

print("\nMerged Dictionary")
print(merged)

# ==========================================
# 23. Merge using update()
# ==========================================

dict1.update(dict2)

print("\nAfter update() Merge")
print(dict1)

# ==========================================
# 24. Sorting Dictionary
# ==========================================

students = {
    "John": 90,
    "Alice": 95,
    "Bob": 80,
    "David": 87
}

print("\nSorted by Keys")

for key in sorted(students):
    print(key, students[key])

print("\nSorted by Values")

for key, value in sorted(students.items(), key=lambda item: item[1]):
    print(key, value)

# ==========================================
# 25. Maximum & Minimum Value
# ==========================================

print("\nHighest Marks")
print(max(students, key=students.get))

print("Lowest Marks")
print(min(students, key=students.get))

# ==========================================
# 26. Dictionary inside List
# ==========================================

employees = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

print("\nEmployees")

for emp in employees:
    print(emp["id"], emp["name"])

# ==========================================
# 27. List inside Dictionary
# ==========================================

student = {
    "name": "Rahul",
    "marks": [80, 90, 95]
}

print("\nList Inside Dictionary")

print(student["marks"][1])

# ==========================================
# 28. Using get() Safely
# ==========================================

print("\nSafe Access")

print(product.get("specs", {}).get("gpu", "GPU Not Found"))

# ==========================================
# 29. Removing all keys one by one
# ==========================================

temp = product.copy()

while temp:
    print("Removed:", temp.popitem())

print("Final:", temp)