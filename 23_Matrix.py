from numpy import *

arr = array([[1, 2, 3],
             [4, 5, 6]])

print(arr)
# [[1 2 3]
#  [4 5 6]]

print(arr.dtype)
# int32

print(arr.ndim)
# 2

print(arr.size)
# 6

#########################################################

# Convert a 2-D array to 1-D array

arr_1d = arr.flatten()

print(arr_1d)
# [1 2 3 4 5 6]

#########################################################

# Convert a 1-D array to 2-D array

arr_2d = arr_1d.reshape(3, 2)  # (rows, columns)

print(arr_2d)
# [[1 2]
#  [3 4]
#  [5 6]]

#########################################################

# Convert a 1-D array to 3-D array

arr_1d = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr_3d = arr_1d.reshape(2, 2, 3)

print(arr_3d)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]

#########################################################

# Create a matrix from a 2-D array

m = matrix(arr)

print(m)
# [[1 2 3]
#  [4 5 6]]

#########################################################

# Create a matrix

m = matrix('1,2,3 ; 4,5,6 ; 7,8,9')

print(m)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(diagonal(m))
# [1 5 9]

print(m.max())
# 9

#########################################################

# Multiply two matrix

m1 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')
m2 = matrix('1,2,3 ; 4,5,6 ; 7,8,9')

m = m1 * m2

print(m)
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]
