# Input in Python
# input() statement is used to accept values (using keyboard) from user

# input() # result for input() is always a str
# int(input()) # int
# float(input()) # float

name = input("Enter your name: ")
# Use type casting to convert input values, because input() returns a string by default.
age = int(input("Enter your age: "))

print(type(name))
print(type(age))

print(f"Hi, I am {name} and I am {age} years old.")


