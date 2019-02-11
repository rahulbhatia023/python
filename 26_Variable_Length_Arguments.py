def add(*b):
    sum = 0
    for num in b:
        sum = sum + num

    print(sum)


add(10, 20)
# 30

add(10, 20, 30, 40)
# 100
