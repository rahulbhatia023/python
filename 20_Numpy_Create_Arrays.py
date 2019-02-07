# NumPy is the fundamental package for scientific computing with Python. It contains among other things:
#
# a powerful N-dimensional array object
# sophisticated (broadcasting) functions
# tools for integrating C/C++ and Fortran code
# useful linear algebra, Fourier transform, and random number capabilities

from numpy import *

# Different ways of creating arrays through numpy

# 1. array()
arr = array([1, 2, 3, 4, 5])
print(arr)
# [1 2 3 4 5]

print(arr.dtype)
# int32

arr = array([1, 2, 3, 4, 5.0])
print(arr.dtype)
# float64

arr = array([1, 2, 3, 4, 5], float)
print(arr)
print(arr.dtype)
# [1. 2. 3. 4. 5.]
# float64

#########################################################

# 2. arange()

# arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval.
# The interval mentioned is half opened i.e. [Start, Stop)
# Parameters :
#
# start : [optional] start of interval range. By default start = 0
# stop  : end of interval range
# step  : [optional] step size of interval. By default step size = 1,
# For any output out, this is the distance between two adjacent values, out[i+1] - out[i].
# dtype : type of output array

# Return:
#
# Array of evenly spaced values.
# Length of array being generated  = Ceil((Stop - Start) / Step)

print(arange(3))
# [0 1 2]

print(arange(3.0))
# [0. 1. 2.]

print(arange(3, 7))
# [3 4 5 6]

print(arange(3, 7, 2))
# [3 5]

#########################################################

# 3. ones()

print(ones(5))
# [1. 1. 1. 1. 1.]

print(ones(5, int))
# [1 1 1 1 1]

#########################################################

# 4. zeros()

print(zeros(5))
# [0. 0. 0. 0. 0.]

print(zeros(5, int))
# [0 0 0 0 0]
