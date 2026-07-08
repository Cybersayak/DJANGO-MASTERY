# Scope of variables in Python

## 1. Global Scope - A variable declared **outside** any function is called a **global variable**. 
# It can be accessed from anywhere in the program.

# Global variable
name = "Alice"

def greet():
    print("Hello,", name)

greet()

print("Name is:", name)

# Output:
# Hello, Alice
# Name is: Alice


## 2. Local Scope - A variable declared **inside** a function is called a **local variable**. It can only be used inside that function.


def student():
    age = 20   # Local variable
    print("Age:", age)

student()

# print(age)   # Error! age is local to the function


# **Output:**


# Age: 20


# If you uncomment the last line:

# print(age)


# You will get:


# NameError: name 'age' is not defined




## 3. Global and Local Variables Together


city = "Kolkata"   # Global variable

def show():
    country = "India"   # Local variable

    print("City:", city)
    print("Country:", country)

show()

print("City:", city)
# print(country)   # Error


# Output:


# City: Kolkata
# Country: India
# City: Kolkata



## 4. Modifying a Global Variable (`global` Keyword)

# Normally, you **cannot change** a global variable inside a function unless you use the `global` keyword.


count = 10

def increase():
    global count
    count = count + 5

increase()

print(count)


# Output:15



## 5. Without `global` Keyword (Error)


count = 10

def increase():
    count = count + 5   # Error
    print(count)

increase()


# Output:
# UnboundLocalError:
# local variable 'count' referenced before assignment



## Summary

# | Scope            | Defined Where        | Accessible Where                   |
# | ---------------- | -------------------- | ---------------------------------- |
# | Global           | Outside any function | Anywhere in the program            |
# | Local            | Inside a function    | Only inside that function          |
# | `global` keyword | Inside a function    | Allows modifying a global variable |

# ### Easy Rule to Remember

# * 🌍 **Global variable** → Created outside a function → Can be read almost everywhere.
# * 🏠 **Local variable** → Created inside a function → Exists only while that function runs.
# * 🔑 **`global` keyword** → Needed when you want to **modify** a global variable from inside a function.


