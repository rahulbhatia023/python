tup1 = (21, 36, 14, 25)

print(tup1[1])
# 36

tup2 = tup1, (1, 2, 3, 4, 5)
print(tup2)
# ((21, 36, 14, 25), (1, 2, 3, 4, 5))

# Tuples are immutable
# tup1[0] = 40 --> This will not work