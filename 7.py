import collections
import math

filepath = "input.in"
lines = [l.rstrip('\n') for l in open(filepath).read().split('\n')]

def def_val():
    return 0
notBottoms = []

bottomProgram = "azqje"

for line in lines:
    if "->" in line:
        notBottoms.append(line.split()[0])


for bottom in notBottoms:
    canBe = True
    for line in lines:
        if bottom in line and line.split()[0] != bottom:
           canBe = False
        
    if(canBe):
        print(bottom, "is bottom program")


lastWeight = 0

programAddress = collections.defaultdict(def_val)

for line in lines:
    programAddress[line.split()[0]] = int(line.split()[1][1:-1])

print(programAddress)

# def findWeightChildren(program):
#     for