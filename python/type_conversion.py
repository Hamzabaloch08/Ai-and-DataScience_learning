# Type Conversion

# 1. type conversion 2. type casting

# conversion => python interpreter do automatically

a = 2  # => type int
b = 4.25  # => type float

# Python automatically converts 'a' to a float when adding or multiplying with 'b' (float)
sum = a + b  # 2.0 + 4.25 => 6.25


print(sum)  # 6.25 (float)


# casting => manually

c = "2"
print(type(c), "string")
c = int(c)
print(c + a)
print(type(c), "intiger")
