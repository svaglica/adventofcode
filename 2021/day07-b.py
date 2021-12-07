with open('./input07.txt') as f:
    crabs = [int(x) for x in f.readline().split(',')]

crabs.sort()

def compute_fuel(pos):
    fuel=0
    for i in crabs:
        fuel += sum(range(1, abs(i-pos)+1))
    return fuel

print(min([compute_fuel(x) for x in range(len(crabs))]))
