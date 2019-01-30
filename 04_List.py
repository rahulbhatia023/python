nums = [25, 12, 36, 95, 14]

print(nums[0])
# 25

print(nums[4])
# 14

print(nums[2:])
# [36, 95, 14]

print(nums[-2:])
# [95, 14]

print(nums[-1])
# 14

print(nums[-5])
# 25

names = ['rahul', 'navin', 'john']

print(names[0])
# rahul

print(names[1])
# navin

values = [9.5, 'rahul', 2]

print(values)
# [9.5, 'rahul', 2]

mix = [nums, names]

print(mix)
# [[25, 12, 36, 95, 14], ['rahul', 'navin', 'john']]

nums.append(45)
print(nums)
# [25, 12, 36, 95, 14, 45]

nums.insert(2, 77)
print(nums)
# [25, 12, 77, 36, 95, 14, 45]

nums.remove(14)
print(nums)
# [25, 12, 77, 36, 95, 45]

nums.pop(1)
print(nums)
# [25, 77, 36, 95, 45]

nums.pop()
print(nums)
# [25, 77, 36, 95]

del nums[2:]
print(nums)
# [25, 77]

nums.extend([29, 12, 14, 36])
print(nums)
# [25, 77, 29, 12, 14, 36]

print(min(nums))
# 12

print(max(nums))
# 77

print(sum(nums))
# 193

nums.sort()
print(nums)
# [12, 14, 25, 29, 36, 77]
