def update(x):
    print('id of x before update:', id(x))
    x = 8
    print('id of x after update:', id(x))


a = 10
print('Value of a before update: ', a)
print('id of a:', id(a))
update(a)
print('Value of a after update: ', a)

# Python is neither pass by value nor pass by reference
