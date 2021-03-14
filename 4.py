import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

def def_val():
    return 0

sum = 0

for line in lines:

    words = line.split()

    hasDupes = False
    wordList = collections.defaultdict(def_val)
    for word in words:
        testString = ''
        for j in sorted(word):
            testString += j
        if wordList[testString]:
            hasDupes = True
        else:
            wordList[testString] = 1

    if not hasDupes:
        sum += 1

print(sum)