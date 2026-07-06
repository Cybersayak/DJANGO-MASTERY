# ==========================================================
# PYTHON STRING OPERATIONS - COMPLETE BEGINNER GUIDE
# ==========================================================

quote = "I am enough prepared in water to beat a Shark in a Water forget Humans"

# ----------------------------------------------------------
# 1. Convert to UPPERCASE
# ----------------------------------------------------------
print("1. UPPERCASE")
print(quote.upper())
print()


# ----------------------------------------------------------
# 2. Convert to lowercase
# ----------------------------------------------------------
print("2. LOWERCASE")
print(quote.lower())
print()


# ----------------------------------------------------------
# 3. Title Case
# Makes the first letter of every word capital.
# ----------------------------------------------------------
print("3. TITLE CASE")
print(quote.title())
print()


# ----------------------------------------------------------
# 4. Capitalize
# Makes only the first letter of the sentence capital.
# ----------------------------------------------------------
print("4. CAPITALIZE")
print(quote.capitalize())
print()


# ----------------------------------------------------------
# 5. Swap Case
# Uppercase becomes lowercase and vice versa.
# ----------------------------------------------------------
print("5. SWAP CASE")
print(quote.swapcase())
print()


# ----------------------------------------------------------
# 6. String Length
# Counts every character including spaces.
# ----------------------------------------------------------
print("6. LENGTH")
print(len(quote))
print()


# ----------------------------------------------------------
# 7. Count Occurrences
# Counts how many times a word appears.
# ----------------------------------------------------------
print("7. COUNT")
print("Water:", quote.count("Water"))
print("Shark:", quote.count("Shark"))
print()


# ----------------------------------------------------------
# 8. Find
# Returns index of first occurrence.
# Returns -1 if not found.
# ----------------------------------------------------------
print("8. FIND")
print(quote.find("Shark"))
print(quote.find("Tiger"))
print()


# ----------------------------------------------------------
# 9. Index
# Similar to find() but raises an error if not found.
# ----------------------------------------------------------
print("9. INDEX")
print(quote.index("prepared"))
print()


# ----------------------------------------------------------
# 10. Replace
# Replaces one word with another.
# ----------------------------------------------------------
print("10. REPLACE")
print(quote.replace("Shark", "Whale"))
print()


# ----------------------------------------------------------
# 11. Startswith
# Checks if string starts with given text.
# ----------------------------------------------------------
print("11. STARTSWITH")
print(quote.startswith("I"))
print()


# ----------------------------------------------------------
# 12. Endswith
# Checks if string ends with given text.
# ----------------------------------------------------------
print("12. ENDSWITH")
print(quote.endswith("Humans"))
print()


# ----------------------------------------------------------
# 13. Split
# Converts string into a list.
# ----------------------------------------------------------
print("13. SPLIT")
words = quote.split()
print(words)
print()


# ----------------------------------------------------------
# 14. Join
# Joins list elements into one string.
# ----------------------------------------------------------
print("14. JOIN")

languages = ["Python", "Java", "C++", "Go"]

print(", ".join(languages))
print(" | ".join(languages))
print()


# ----------------------------------------------------------
# 15. Strip
# Removes extra spaces from both ends.
# ----------------------------------------------------------
print("15. STRIP")

text = "      Hello Python      "

print(text.strip())
print()


# ----------------------------------------------------------
# 16. Left Strip
# Removes spaces only from left side.
# ----------------------------------------------------------
print("16. LSTRIP")
print(text.lstrip())
print()


# ----------------------------------------------------------
# 17. Right Strip
# Removes spaces only from right side.
# ----------------------------------------------------------
print("17. RSTRIP")
print(text.rstrip())
print()


# ----------------------------------------------------------
# 18. Is Alpha
# Returns True if all characters are letters.
# ----------------------------------------------------------
print("18. ISALPHA")
print("Python".isalpha())
print("Python3".isalpha())
print()


# ----------------------------------------------------------
# 19. Is Digit
# Returns True if every character is a digit.
# ----------------------------------------------------------
print("19. ISDIGIT")
print("12345".isdigit())
print("12A45".isdigit())
print()


# ----------------------------------------------------------
# 20. Is Alphanumeric
# Letters + Numbers only.
# ----------------------------------------------------------
print("20. ISALNUM")
print("Python123".isalnum())
print("Python 123".isalnum())
print()


# ----------------------------------------------------------
# 21. Is Lower
# ----------------------------------------------------------
print("21. ISLOWER")
print("python".islower())
print("Python".islower())
print()


# ----------------------------------------------------------
# 22. Is Upper
# ----------------------------------------------------------
print("22. ISUPPER")
print("PYTHON".isupper())
print("Python".isupper())
print()


# ----------------------------------------------------------
# 23. Is Space
# Checks if string contains only whitespace.
# ----------------------------------------------------------
print("23. ISSPACE")
print("     ".isspace())
print("Hello".isspace())
print()


# ----------------------------------------------------------
# 24. Center
# Centers the text using a fill character.
# ----------------------------------------------------------
print("24. CENTER")
print("Python".center(30, "-"))
print()


# ----------------------------------------------------------
# 25. Left Justify
# Aligns text to the left.
# ----------------------------------------------------------
print("25. LJUST")
print("Python".ljust(20, "."))
print()


# ----------------------------------------------------------
# 26. Right Justify
# Aligns text to the right.
# ----------------------------------------------------------
print("26. RJUST")
print("Python".rjust(20, "."))
print()


# ----------------------------------------------------------
# 27. Zero Fill
# Adds zeros before the number.
# ----------------------------------------------------------
print("27. ZFILL")
print("25".zfill(6))
print()


# ----------------------------------------------------------
# 28. Partition
# Splits string into three parts:
# before separator, separator, after separator.
# ----------------------------------------------------------
print("28. PARTITION")
print(quote.partition("Shark"))
print()


# ----------------------------------------------------------
# 29. RFind
# Searches from the right.
# ----------------------------------------------------------
print("29. RFIND")
print(quote.rfind("Water"))
print()


# ----------------------------------------------------------
# 30. Encode
# Converts string into bytes.
# ----------------------------------------------------------
print("30. ENCODE")
print(quote.encode())
print()


# ----------------------------------------------------------
# 31. String Formatting - format()
# ----------------------------------------------------------
print("31. FORMAT")

name = "Alex"
age = 22

print("My name is {} and I am {} years old.".format(name, age))
print()


# ----------------------------------------------------------
# 32. f-Strings (Recommended)
# Modern and most readable way to format strings.
# ----------------------------------------------------------
print("32. F-STRING")

language = "Python"
version = 3.12

print(f"I love {language} {version}")
print()


# ----------------------------------------------------------
# 33. String Slicing
# Syntax:
# string[start:stop:step]
# ----------------------------------------------------------
print("33. SLICING")

print(quote[:10])      # First 10 characters
print(quote[5:20])     # Characters 5 to 19
print(quote[-6:])      # Last 6 characters
print(quote[::-1])     # Reverse string
print()


# ----------------------------------------------------------
# 34. Membership Operators
# ----------------------------------------------------------
print("34. MEMBERSHIP")

print("Shark" in quote)
print("Tiger" in quote)
print("Tiger" not in quote)
print()


# ----------------------------------------------------------
# 35. Escape Characters
# ----------------------------------------------------------
print("35. ESCAPE CHARACTERS")

print("Hello\nWorld")
print("Python\tProgramming")
print("She said \"Hello\"")
print('It\'s Python')
print()

# ----------------------------------------------------------
# 36. Replace Method
# ----------------------------------------------------------

quote = "I am enough prepared in water to beat a Shark in a Water forget Humans"
new_quote = quote.replace("Shark", "Whale")
print(new_quote)

# ==========================================================
# END OF STRING OPERATIONS
# ==========================================================