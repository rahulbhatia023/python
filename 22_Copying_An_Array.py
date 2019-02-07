from numpy import *

arr1 = array([1, 2, 3, 4, 5])

arr2 = arr1

print(arr1)
# [1 2 3 4 5]

print(arr2)
# [1 2 3 4 5]

print(id(arr1))
# 154306344

print(id(arr2))
# 154306344

########################################################

arr1 = array([1, 2, 3, 4, 5])

arr2 = arr1.view()

print(arr1)
# [1 2 3 4 5]

print(arr2)
# [1 2 3 4 5]

print(id(arr1))
# 146637192

print(id(arr2))
# 142023280

arr1[1] = 7

print(arr1)
# [1 7 3 4 5]

print(arr2)
# [1 7 3 4 5]

# This is an example of Shallow copy

########################################################

arr1 = array([1, 2, 3, 4, 5])

arr2 = arr1.copy()

print(arr1)
# [1 2 3 4 5]

print(arr2)
# [1 2 3 4 5]

print(id(arr1))
# 155289744

print(id(arr2))
# 155320912

arr1[1] = 7

print(arr1)
# [1 7 3 4 5]

print(arr2)
# [1 2 3 4 5]

# This is an example of Deep copy
