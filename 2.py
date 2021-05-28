import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

dif_total = 0
for line in lines:
    nums = list(map(int, line.split('\t')))
    dif_total += max(nums) - min(nums)
print(dif_total)  # part 1 answer

total = 0
for line in lines:
    nums = list(map(int, line.split('\t')))

    for a in nums:
        for b in nums:
            if a != b and ((a/b).is_integer() or (b/a).is_integer()):
                if (a/b).is_integer():
                    total += a/b
                else:
                    total += b/a


print(int(total/2))  # part 2 answer
