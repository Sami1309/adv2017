import collections
import math

filepath = "input.in"
ins = [int(l.rstrip('\n')) for l in open(filepath).read().split('\n')]


pointer = 0
steps = 0
while pointer in range(len(ins)):
    currentIns = ins[pointer]
    temp = currentIns
    if temp >= 3:
        ins[pointer] = ins[pointer] - 1
    else:
        ins[pointer] = ins[pointer] + 1
    pointer += temp
    steps += 1

print(steps)

    