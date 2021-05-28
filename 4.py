import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


def def_val():
    return 0


valids = 0

for line in lines:

    passes = line.split(' ')
    for i in range(len(passes)):
        passes[i] = ''.join(sorted(passes[i]))
    print(passes)
    setPass = set(passes)
    if len(setPass) == len(passes):
        valids += 1

print(valids)
