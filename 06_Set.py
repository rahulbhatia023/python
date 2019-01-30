# A set is an unordered collection with no duplicate elements.

set1 = {22, 25, 14, 21, 5}
print(set1)
# {5, 14, 21, 22, 25}

set2 = {25, 14, 98, 63, 75, 98}
print(set2)
# {98, 75, 14, 25, 63} --> show that duplicates have been removed

print(14 in set1)
# True --> fast membership testing

print(50 in set2)
# False

set3 = set('abracadabra')
print(set3)
# {'r', 'd', 'c', 'b', 'a'}

set4 = set('alacazam')
print(set4)
# {'l', 'm', 'c', 'a', 'z'}

print(set3 - set4)
# {'b', 'd', 'r'} --> letters in set3 but not in set4

print(set3 | set4)
# {'c', 'm', 'z', 'r', 'a', 'd', 'l', 'b'} --> letters in set3 or set4 or both

print(set3 & set4)
# {'c', 'a'} --> letters in both set3 and set4

print(set3 ^ set4)
# {'b', 'm', 'd', 'z', 'l', 'r'} --> letters in set3 or set4 but not both
