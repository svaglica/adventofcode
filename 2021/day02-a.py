with open('./input02-a.txt') as f:
    depths = [x.split(' ') for x in f.read().splitlines()]

f=0
d=0

for step in depths:
    if step[0] == 'forward':
        f += int(step[1])
    if step[0] == 'up':
        d -= int(step[1])
    if step[0] == 'down':
        d += int(step[1])

print(f*d)
