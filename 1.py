import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

num_str = lines[0]
length = int(len(num_str) / 2)

print(sum([int(num_str[i]) if num_str[i] == num_str[(i + 1) % len(num_str)]
      else 0 for i in range(0, len(num_str))]))  # part 1 solution

print(sum([int(num_str[i]) if num_str[i] == num_str[(i + length) % len(num_str)]
      else 0 for i in range(0, len(num_str))]))  # part 2 solution
