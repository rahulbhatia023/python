def add(x, y):
    c = x + y
    return c


sum = add(5, 4)
print('Sum is:', sum)


def add_sub(x, y):
    sum = x + y
    diff = x - y
    return sum, diff


sum, diff = add_sub(5, 4)
print('Sum is:', sum)
print('Difference is:', diff)
