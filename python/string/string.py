# Strings
# String is a data type that stores a sequence of characters.

# str = 'This is string'
# str2 = "This is string"
str3 = """This is string"""

paragraph = """This is a multi-line string in Python.
It can span multiple lines using triple quotes.
This is very useful for long paragraphs or documentation."""

print(paragraph)

# escape sequence character

# \n next line
# \t tabspace

str1 = "this is string. \nwe are creating in \t python."
print(str1)

# Basic Operations

# Concatenation

a = "hello"
b = "world"
print(a, b)
print(a + " " + b)

# length of str

print(len(a))

# Indexing

print(a[0] + a[4])

# practice

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name[0] + last_name[0])
