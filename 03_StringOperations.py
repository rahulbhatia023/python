print('rahul')
# rahul

print("rahul's laptop")
# rahul's laptop

print('rahul "laptop"')
# rahul "laptop"

print('rahul\'s "laptop"')
# rahul's "laptop"

print('rahul' + 'rahul')
# rahulrahul

print(3 * 'rahul')  # Print 'rahul' 3 times
# rahulrahulrahul

print('c:\docs\navin')
# c:\docs
# avin

print(r'c:\docs\navin')  # r means the string will be treated as raw string. Won't consider \n as new line
# c:\docs\navin

z = 'rahul'

print(z[0])
# r

print(z[4])
# l

print(z[-1])  # Negative index is used in python to index starting from the last element of the list, tuple or any other
# container class which supports indexing. -1 refers to the last index, -2 refers to the second last index and so on
# l

print(z[-5])
# r

print(z[0:4])  # Print the characters starting from 0 until 3
# rahu

print(z[2:4])  # Print the characters starting from 2 until 3
# hu

print(z[2:])  # Print the characters starting from 2 until end of the string
# hul

print(z[:2])  # Print the characters starting from start until 1
# ra

print(z[2:80])  # Print the characters starting from 2 until end of the string even if end index provided is more than
# the length of the string
# hul
