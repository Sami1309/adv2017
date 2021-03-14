import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

def reverse(l, curPos, numbers):
    reversible = numbers[curPos:l]
    reversible.reverse()
    returnList = numbers[0:curPos]
    returnList.append(reversible)
    returnList.append(numbers[curPos+l:])
    return returnList

numbers = [n for n in range(256)]

curPos = 0

skipSize = 0




lengths = lines[0].split(',')

for l in lengths:
    numbers = reverse(l, curPos, numbers)

    curPos += l + skipSize
    skipSize += 1