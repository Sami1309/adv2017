import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


def def_val():
    return 0


derivs = set()

starts = {}

sets = {}

base_starts = set()

for line in lines:
    programs = line.split(' -> ')
    firsts = programs[0].split(' ')
    parent = firsts[0]
    weight = int(firsts[1][1:-1])
    children = []
    chil = []
    if len(programs) > 1:
        children = programs[1].split(', ')
        # print(children)
        for c in children:
            chil.append(c)
            derivs.add(c)
    base_starts.add(parent)

    sets[parent] = chil
    starts[parent] = weight


# print(starts)
# print(derivs)
for s in sets:
    if len(sets[s]) > 0:
        # print(sets[s])
        pass


base = ''

for s in base_starts:
    if s not in derivs:
        # print(s)
        base = s

#base = 'lnpuarm'
print(starts['lnpuarm'])
starts['lnpuarm'] -= 8
print(starts['lnpuarm'])
sum = 0
stack = []
stack.append(base)

prime_children = list(sets[base])
print(prime_children)
while len(stack) > 0:
    cur = stack.pop()
    if cur in prime_children:
        print(sum)
        sum = 0
    # print(cur)
    sum += starts[cur]
    children = sets[cur]
    for c in children:
        stack.append(c)
print(sum)
