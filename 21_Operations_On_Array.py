from numpy import *

arr = array([1, 2, 3, 4, 5])

arr = arr + 5

print(arr)
# [ 6  7  8  9 10]

arr1 = array([1, 3, 5, 7, 9])
arr2 = array([2, 4, 6, 8, 10])

arr = arr1 + arr2

print(arr)
# [ 3  7 11 15 19]

arr = array([1, 2, 3, 4, 5])

print(log(arr))
# [0.         0.69314718 1.09861229 1.38629436 1.60943791]

print(square(arr))
# [ 1  4  9 16 25]

print(concatenate([arr1, arr2]))
# [ 1  3  5  7  9  2  4  6  8 10]
