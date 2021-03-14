import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

total = 0
garbageCount = 0
for line in lines:
    groupLevel = 0
    groups = []
    isGarbage = False
    a = 0
    
    while a < len(line):

        if isGarbage:
            garbageCount += 1

        if line[a] == "!":
            a += 1
            garbageCount -= 1
        elif line[a] == "<":
            isGarbage = True
        elif line[a] == ">":
            isGarbage = False
            garbageCount -= 1
        elif line[a] == "{" and not isGarbage:
            groupLevel += 1
        elif line[a] == "}" and not isGarbage:
            groups.append(groupLevel)
            groupLevel -= 1


        a += 1
    total += sum(groups)

print(garbageCount)
