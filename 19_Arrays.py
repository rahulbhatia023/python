# An array is a collection of elements of the same type.
# We can treat lists as arrays. However, we cannot constrain the type of elements stored in a list.

from array import *

# we need to import array module to create arrays

vals = array('i', [1, 2, 3, 4, 5])
# Here, we created an array of int type. The letter 'i' is a type code. This determines the type of the array during
# creation.

# Type code	    C Type	        Python Type	        Minimum size in bytes
# 'b'	        signed char	    int	                1
# 'B'	        unsigned char	int	                1
# 'u'	        Py_UNICODE	    Unicode character	2
# 'h'	        signed short	int	                2
# 'H'	        unsigned short	int	                2
# 'i'	        signed int	    int	                2
# 'I'	        unsigned int	int	                2
# 'l'	        signed long	    int	                4
# 'L'	        unsigned long	int	                4
# 'f'	        float	        float	            4
# 'd'	        double	        float	            8

print(vals)
# array('i', [1, 2, 3, 4, 5])

print(vals.buffer_info())
# Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to
# hold array’s contents.
# (89244448, 5)

print(vals.typecode)
# Returns the typecode character used to create the array.
# i

print(vals.reverse())
# Reverse the order of the items in the array.

print(vals[0])
# We use indices to access elements of an array
# 5

for i in vals:
    print(i)

for i in range(len(vals)):
    print(vals[i])

vals = array('u', ['a', 'e', 'i', 'o', 'u'])

for i in vals:
    print(i)

newVals = array(vals.typecode, (a for a in vals))
# Copy the values from vals array to newVals array

for i in newVals:
    print(i)
