from functools import reduce
nums = list(range(0, 11))

print(nums)

i = list(filter(lambda x: x % 2 == 0, nums))

l = list(map(lambda num: num * 2, i))

reduce1 = reduce(lambda x, y: x + y, nums)

print(reduce1)