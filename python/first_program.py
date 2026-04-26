# Simple program to print messages

print("hello world")
print("hello world", "How are you")
print("hello world", 123)
print(10 + 37)

# Variables
# = Assigment operator

name = "hamza"
age = 18
price = 35.99

fullname = name + " Baloch"

print("My name is ", name)
print("My age is ", age)
print(fullname)

# Rules of Indentifiers
# a-z A-Z 0-9
# we cant use special symbols like !@#$%^&* etc.
# variable1 is valid, 1variable is not valid.
# identifier can be of any lenght.

# DATA TYPES

# - intiger (-values, +values, 0) => (-25, +25, 0)
# - String ("hamza",'hamza','"hamza"')
# - Float any decimal value like 23.99 34.85
# - Boolean True / False
# - None: This is a special constant in Python that represents the absence of a value or a null value. It is used when a variable is declared but not assigned any value yet.

# checking variable Types

print(type(age), "int")
print(type(name), "string")
print(type(price), "float")
a = True
b = False
c = None
print(a, "boolean")
print(b, "boolean")
print(c, "None")
