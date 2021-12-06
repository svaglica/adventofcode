import numpy as np
vents=np.zeros(1000000)

lines=[]
with open('./input05.txt') as f:
    for elem in f.read().splitlines():
        line = elem.split(' -> ')
        print(line)
        lines += [[[int(x) for x in line[0].split(',')], [int(x) for x in line[1].split(',')]]]

print(lines)

for line in lines:
    if line[0][0] == line[1][0]:
        # same row
        maxi = max(line[0][1], line[1][1])
        mini = min(line[0][1], line[1][1])
        for col in range(maxi - mini +1):
            vents[line[0][0] * 1000 + (mini + col)] += 1

    elif line[0][1] == line[1][1]:
        # same collumn
        maxi = max(line[0][0], line[1][0])
        mini = min(line[0][0], line[1][0])
        for row in range(maxi - mini +1):
            vents[(mini + row) * 1000 + line[0][1]] += 1

print(vents)
nb=0
for i in range(len(vents)):
    nb += int(vents[i] >= 2)

print(nb)
