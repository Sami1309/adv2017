import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

sum = 0

forward = len(lines[0])/2
first = lines[0][int(forward)]
count = 1
for l in lines[0]:
    if l == first:
        sum += int(l)
    first = lines[0][(int(forward) + count)%len(lines[0])]
    count += 1
print(sum)
