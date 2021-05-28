import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


ins = list(map(int, lines))

print(ins)

curPos = 0
steps = 0
while curPos >= 0 and curPos < len(ins):
    instruct = ins[curPos]
    nextStep = curPos + instruct
    if instruct >= 3:
        ins[curPos] -= 1
    else:
        ins[curPos] += 1
    curPos = nextStep
    steps += 1

print(steps)
