print(3 + 9)
# 12

x = 3

print(x + 9)
# 12

y = 9

print(x + y)
# 12

x = 10

print(x + y)
# 19

z = 'rahul'

print(z + ' bhatia')
# rahul bhatia

print(id(x))
# 140722730361968
# The id() function returns identity of the object. This is an integer which is unique for the given object and remains
# constant during its lifetime.
# Is it the same with memory addresses in C? Conceptually, yes, in that they are both guaranteed to be unique in their
# universe during their lifetime. And in one particular implementation of Python, it actually is the memory address of
# the corresponding C object.

print('id of 5 =', id(5))
# id of 5 = 140722730361808

a = 5
print('id of a =', id(a))
# id of a = 140722730361808

b = a
print('id of b =', id(b))
# id of b = 140722730361808

c = 5.0
print('id of c =', id(c))
# id of c = 2376214753496

print(type(x))
# <class 'int'>
# If a single argument (object) is passed to type() built-in, it returns type of the given object.

print(type(z))
# <class 'str'>

print(type(3.14))
# <class 'float'>
