a = 10


def doSomething():
    a = 5
    print('local =', a)
    # 5


doSomething()

print('global =', a)
# 10

################################################

a = 10


def doSomething():
    global a
    a = 5

    print('local =', a)
    # 5


doSomething()

print('global =', a)
# 5

################################################

a = 10


def doSomething():
    a = 5

    globals()['a'] = 15

    print('local =', a)
    # 5


doSomething()

print('global =', a)
# 5
