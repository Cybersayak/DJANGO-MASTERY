# ==========================================================
# PYTHON FUNCTIONS 
# ==========================================================

# ----------------------------------------------------------
# 1. Simple Function
# ----------------------------------------------------------

def mahamantra():
    print("Hare Krishna Hare Krishna Krishna Krishna Hare Hare")

mahamantra()


# ----------------------------------------------------------
# 2. Function with Parameters
# ----------------------------------------------------------

def chant(name):
    print(f"{name} chants Hare Krishna!")

chant("Arjuna")
chant("Radha")


# ----------------------------------------------------------
# 3. Function with Return Value
# ----------------------------------------------------------

def add(a, b):
    return a + b

result = add(10, 20)
print("Addition:", result)


# ----------------------------------------------------------
# 4. Default Parameters
# ----------------------------------------------------------

def greet(name="Devotee"):
    print(f"Welcome, {name}")

greet()
greet("Krishna")


# ----------------------------------------------------------
# 5. Keyword Arguments
# ----------------------------------------------------------

def student(name, age):
    print(name, age)

student(age=22, name="Rohan")


# ----------------------------------------------------------
# 6. Positional Arguments
# ----------------------------------------------------------

student("Rahul", 19)


# ----------------------------------------------------------
# 7. Variable Length Arguments (*args)
# ----------------------------------------------------------

def total(*numbers):
    print("Numbers:", numbers)
    print("Sum:", sum(numbers))

total(1, 2, 3)
total(10, 20, 30, 40)


# ----------------------------------------------------------
# 8. Keyword Variable Arguments (**kwargs)
# ----------------------------------------------------------

def details(**info):
    print(info)

details(name="Krishna", age=5000, city="Vrindavan")


# ----------------------------------------------------------
# 9. Combination of Parameters
# ----------------------------------------------------------

def example(a, b=5, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

example(1, 2, 3, 4, x=100, y=200)


# ----------------------------------------------------------
# 10. Returning Multiple Values
# ----------------------------------------------------------

def calculation(a, b):
    return a+b, a-b, a*b

x, y, z = calculation(10, 5)

print(x)
print(y)
print(z)


# ----------------------------------------------------------
# 11. Recursive Function
# ----------------------------------------------------------

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("Factorial:", factorial(5))


# ----------------------------------------------------------
# 12. Lambda Function
# ----------------------------------------------------------

square = lambda x: x*x

print(square(5))


# ----------------------------------------------------------
# 13. Function Assigned to Variable
# ----------------------------------------------------------

def hello():
    print("Hello")

greeting = hello

greeting()


# ----------------------------------------------------------
# 14. Function Inside Function (Nested)
# ----------------------------------------------------------

def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()


# ----------------------------------------------------------
# 15. Returning a Function
# ----------------------------------------------------------

def outer():

    def inner():
        print("Returned Function")

    return inner

f = outer()
f()


# ----------------------------------------------------------
# 16. Passing Function as Argument
# ----------------------------------------------------------

def display(func):
    func()

display(mahamantra)


# ----------------------------------------------------------
# 17. Anonymous Function with map()
# ----------------------------------------------------------

numbers = [1,2,3,4,5]

squares = list(map(lambda x:x*x, numbers))

print(squares)


# ----------------------------------------------------------
# 18. filter()
# ----------------------------------------------------------

evens = list(filter(lambda x:x%2==0, numbers))

print(evens)


# ----------------------------------------------------------
# 19. sorted() with key
# ----------------------------------------------------------

students = [
    ("Ram",25),
    ("Krishna",18),
    ("Arjuna",22)
]

print(sorted(students, key=lambda x:x[1]))


# ----------------------------------------------------------
# 20. Recursive Fibonacci
# ----------------------------------------------------------

def fibonacci(n):

    if n<=1:
        return n

    return fibonacci(n-1)+fibonacci(n-2)

for i in range(8):
    print(fibonacci(i), end=" ")

print()


# ----------------------------------------------------------
# 21. Generator Function (yield)
# ----------------------------------------------------------

def count():

    for i in range(5):
        yield i

for value in count():
    print(value)


# ----------------------------------------------------------
# 22. Generator Expression
# ----------------------------------------------------------

gen = (x*x for x in range(5))

for i in gen:
    print(i)


# ----------------------------------------------------------
# 23. Decorator
# ----------------------------------------------------------

def decorator(func):

    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper


@decorator
def say_hi():
    print("Hi")

say_hi()


# ----------------------------------------------------------
# 24. Function Annotations
# ----------------------------------------------------------

def multiply(a:int, b:int) -> int:
    return a*b

print(multiply(5,6))


# ----------------------------------------------------------
# 25. Docstring
# ----------------------------------------------------------

def divide(a,b):
    """
    Returns division.
    """
    return a/b

print(divide.__doc__)


# ----------------------------------------------------------
# 26. Local vs Global Variable
# ----------------------------------------------------------

x = 100

def test():
    x = 10
    print("Local:", x)

test()

print("Global:", x)


# ----------------------------------------------------------
# 27. global Keyword
# ----------------------------------------------------------

count = 0

def increment():
    global count
    count += 1

increment()
increment()

print(count)


# ----------------------------------------------------------
# 28. nonlocal Keyword
# ----------------------------------------------------------

def outer():

    x = 10

    def inner():
        nonlocal x
        x += 5

    inner()

    print(x)

outer()


# ----------------------------------------------------------
# 29. __name__
# ----------------------------------------------------------

def demo():
    print("Executed")

if __name__ == "__main__":
    demo()


# ----------------------------------------------------------
# 30. Method inside Class
# ----------------------------------------------------------

class Devotee:

    def chant(self):
        print("Hare Krishna!")

d = Devotee()
d.chant()


# ----------------------------------------------------------
# 31. Static Method
# ----------------------------------------------------------

class Math:

    @staticmethod
    def add(a,b):
        return a+b

print(Math.add(3,4))


# ----------------------------------------------------------
# 32. Class Method
# ----------------------------------------------------------

class Person:

    company = "ISKCON"

    @classmethod
    def info(cls):
        print(cls.company)

Person.info()


# ----------------------------------------------------------
# 33. Callable Object
# ----------------------------------------------------------

class Prayer:

    def __call__(self):
        print("Prayer Called")

p = Prayer()

p()


# ----------------------------------------------------------
# 34. Partial Function
# ----------------------------------------------------------

from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)

print(square(9))


# ----------------------------------------------------------
# 35. reduce()
# ----------------------------------------------------------

from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda x,y:x+y, numbers)

print(result)


# ----------------------------------------------------------
# 36. zip() with Function
# ----------------------------------------------------------

names = ["A","B","C"]
ages = [20,21,22]

for name, age in zip(names, ages):
    print(name, age)


# ----------------------------------------------------------
# 37. enumerate()
# ----------------------------------------------------------

for index, value in enumerate(names, start=1):
    print(index, value)


# ----------------------------------------------------------
# 38. Higher Order Function
# ----------------------------------------------------------

def apply(func, value):
    return func(value)

print(apply(square, 7))


# ----------------------------------------------------------
# 39. Function Attributes
# ----------------------------------------------------------

def sample():
    pass

sample.version = "1.0"

print(sample.version)


# ----------------------------------------------------------
# 40. Async Function
# ----------------------------------------------------------

import asyncio

async def async_hello():
    print("Hello Async")

asyncio.run(async_hello())


# ==========================================================
# END OF FUNCTION DEMONSTRATION
# ==========================================================