import collections
import math
import re


filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]


# ev inc -11 if d <= -963

regs = collections.Counter()
top = 0
for line in lines:
    reg, dr, num, left, comp, right = re.match(
        r"(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (\S+)", line).groups()
    if eval(f'{regs[left]} {comp} {right}'):
        num = int(num)
        if dr == 'dec':
            num *= -1
        regs[reg] += num
        top = max(top, regs[reg])
print(max(regs.values()))  # part 1
print(top)  # part 2


print(eval('8 >= 3'))
