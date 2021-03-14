import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


total = 0
for line in lines:
    nums = line.split()
    vals = []
    for num in nums:
        vals.append(int(num))
    for a in vals:
        for b in vals:
            if a != b and ((a/b).is_integer() or (b/a).is_integer()):
                if (a/b).is_integer():
                    total += a/b
                else:
                    total += b/a
                    

print(total/2)
