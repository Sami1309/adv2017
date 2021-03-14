import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

turnEnd = 30000000



def lastCheck(lastNum, spoken, place):
    return lastPlace[lastNum]

def def_val():
    return -1

lastPlace = collections.defaultdict(def_val)

spoken = [None]*turnEnd
spoken[0] = 0
spoken[1] = 14
spoken[2] = 6
spoken[3] = 20
spoken[4] = 1
spoken[5] = 4

lastPlace[0] = 0
lastPlace[14] = 1
lastPlace[6] = 2
lastPlace[20] = 3
lastPlace[1] = 4
lastPlace[4] = 5
#spoken = [2,1,3]

start = 6
while start < turnEnd:
    lastNum = spoken[start - 1]

    lastSpoken = lastCheck(lastNum, spoken, start-1)
    if lastSpoken == -1:
        spoken[start] = 0
        lastPlace[lastNum] = start-1
    else:
        spoken[start] = start - lastSpoken-1
        lastPlace[lastNum] = start-1
    
    start += 1


print(spoken[-1])