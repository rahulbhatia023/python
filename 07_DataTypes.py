# None
# The None keyword is used to define a null value, or no value at all.
x = None
print(x)
# None

null_variable = None
not_null_variable = 'Hello There!'

# The is keyword
if null_variable is None:
    print('null_variable is None')
else:
    print('null_variable is not None')
# null_variable is None

if not_null_variable is None:
    print('not_null_variable is None')
else:
    print('not_null_variable is not None')
# not_null_variable is not None

#######################################################################

# Numeric
# There are four different numerical types in Python:

# 1. int (plain integers): They are often called just integers or ints. They are positive or negative whole numbers
# with no decimal point. Integers in Python 3 are of unlimited size. Python 2 has two integer types - int and long.
# There is no 'long integer' in Python 3 anymore.
print(type(5))
print(type(-5))
# <class 'int'>

# 2. float (floating point real values): floats represent real numbers, but are written with decimal points.
print(type(2.5))
print(type(-2.5))
# <class 'float'>

# 3. complex (complex numbers): represented by the formula a + bJ, where a and b are floats, and J is the square root
# of -1 (the result of which is an imaginary number). Complex numbers are used sparingly in Python.
print(type(2 + 5j))
# <class 'complex'>

print(int(5.8))
# 5

print(float(5))
# 5.0

print(complex(2, 5))
# (2+5j)

#######################################################################

# Boolean
# Python 3 provides a Boolean data type. Objects of Boolean type may have one of two values, True or False

a = True
print(type(a))
# <class 'bool'>

print(type(False))
# <class 'bool'>

print(int(True))
# 1

print(int(False))
# 0

#######################################################################

# Sequence
# Sequences allow you to store multiple values in an organized and efficient fashion.

# 1. List
nums = [25, 12, 36, 95, 14]
print(type(nums))
# <class 'list'>

# 2. Set
nums = {25, 12, 36, 95, 14}
print(type(nums))
# <class 'set'>

# 3. Tuple
nums = (25, 12, 36, 95, 14)
print(type(nums))
# <class 'tuple'>

# 4. String
s = 'rahul'
print(type(s))
# <class 'str'>

c = 'r'
print(type(c))
# <class 'str'>
# There is no such thing as char in python

# 5. Range
# The range() type returns an immutable sequence of numbers between the given start integer to the stop integer.
# range(stop): Returns a sequence of numbers starting from 0 to stop - 1. Returns an empty sequence if stop is negative or 0.

print(range(10))
# range(0, 10)

print(type(range(10)))
# <class 'range'>

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range(start, stop[, step]): The return value is calculated by the following formula with the given constraints:
#
# r[n] = start + step*n (for both positive and negative step)
# where, n >=0 and r[n] < stop (for positive step)
# where, n >= 0 and r[n] > stop (for negative step)

print(list(range(0, 12, 2)))
# [0, 2, 4, 6, 8, 10]

# 6. Dictionary
# Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike
# other Data Types that hold only single value as an element, Dictionary holds key:value pair. Each key-value pair in a
# Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’. Keys of a Dictionary must be unique
# and of immutable data type such as Strings, Integers and tuples, but the key-values can be repeated and be of any type.

d = {1: 'Geeks', 2: 'For', 'other': 'Geeks'}
print(d)
# {1: 'Geeks', 2: 'For', 'other': 'Geeks'}

print(type(d))
# <class 'dict'>

print(d.keys())
# dict_keys([1, 2, 'other'])

print(d.values())
# dict_values(['Geeks', 'For', 'Geeks'])

print(d['other'])
# Geeks

print(d.get('other'))
# Geeks
