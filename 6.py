import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


banks = list(map(int, lines[0].split('\t')))

print(banks)


seens = set()
seens2 = set()
# part 1 2:44

cycles = 0
cycles2 = 0

firstEnc = False

while 1:
    if firstEnc and tuple(banks) in seens2:
        print(cycles2)
        print(banks)
        break
    if tuple(banks) in seens and not firstEnc:
        print(cycles)
        firstEnc = True
        cycles2 = 0
        seens2.add(tuple(banks))
        print(banks)

    if not firstEnc:
        seens.add(tuple(banks))
    else:
        seens2.add(tuple(banks))
    max = -float('inf')
    max_in = 0

    for i in range(len(banks)):
        if banks[i] > max:
            max = banks[i]
            max_in = i

    banks[max_in] = 0

    cur = max_in + 1
    for i in range(max):
        banks[cur % len(banks)] += 1
        cur += 1
    cycles += 1
    cycles2 += 1
