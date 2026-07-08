# **kwargs → Dictionary → Keyword values

def demo(**kwargs):
    print(kwargs)

demo(name="Ram", age=20)
# {'name': 'Ram', 'age': 20}



# *args → Tuple → Positional values

def demo(*args):
    print(args)

demo(1, 2, 3)
# (1, 2, 3)



# ARGS Example 

# Example 1

def add(*numbers):
    total = 0

    for num in numbers:
        total += num

    print("Total =", total)

add(5, 10)
add(1, 2, 3, 4, 5)


# Example 2 
def names(*students):
    for student in students:
        print(student)

names("Ram", "Shyam", "Mohan")




# Kwargs Example


# Example 1

def person(**details):
    print("Name:", details["name"])
    print("Age:", details["age"])

person(name="Rahul", age=21)

# Example 2

def info(**details):
    for key, value in details.items():
        print(key, "=", value)

info(name="Aman", age=20, country="India")