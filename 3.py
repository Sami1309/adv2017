import collections
import math

#filepath = "input.in"
#lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


input = 361527

orient = [(0, 1), (1, 0), (0, -1), (-1, 0)]
positions = set()
positions.add((0, 0))
positions.add((1, 0))
cur_pos = (1, 0)
direction = 0
for i in range(2, input):
    newPos = (cur_pos[0] + orient[(direction-1) % 4][0],
              cur_pos[1] + orient[(direction-1) % 4][1])
    if newPos in positions:
        x = orient[direction][0]
        y = orient[direction][1]
        nextPos = (cur_pos[0] + x, cur_pos[1] + y)
        positions.add(nextPos)
        cur_pos = nextPos
        # move forward
    else:
        # move left
        direction = (direction-1) % 4
        positions.add(newPos)
        cur_pos = newPos

print(abs(cur_pos[0]) + abs(cur_pos[1]))  # part 1 solution

positions2 = set()
positions2.add((0, 0))
positions2.add((1, 0))
cur_pos = (1, 0)
direction = 0
cur_val = 1

vd = {}

vd[(0, 0)] = 1
vd[(1, 0)] = 1


for i in range(2, input):
    newPos = (cur_pos[0] + orient[(direction-1) % 4][0],
              cur_pos[1] + orient[(direction-1) % 4][1])
    if newPos in positions2:
        x = orient[direction][0]
        y = orient[direction][1]
        nextPos = (cur_pos[0] + x, cur_pos[1] + y)
        positions2.add(nextPos)
        cur_pos = nextPos
        # move forward
    else:
        # move left
        direction = (direction-1) % 4
        positions2.add(newPos)
        cur_pos = newPos
    curSum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if not (x == 0 and y == 0):
                if vd.get((cur_pos[0] + x, cur_pos[1] + y)):
                    curSum += vd[(cur_pos[0] + x, cur_pos[1] + y)]
    vd[cur_pos] = curSum
    if curSum > input:
        print(curSum)
        break

print(cur_pos)
print(vd[cur_pos])
