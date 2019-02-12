import sys

print(sys.getrecursionlimit())
# 1000

sys.setrecursionlimit(2000)

counter = 1


def greet():
    global counter
    print("Hello:", counter)
    counter = counter + 1
    greet()


greet()
