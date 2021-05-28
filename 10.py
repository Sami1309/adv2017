import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

myList = [i for i in range(256)]

skip = 0

lengths = list(map(int, lines[0].split(',')))

print(lengths)
