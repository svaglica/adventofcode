with open('./input03-a.txt') as f:
    slope = f.read().splitlines()

down = 1
right = 3


heigh = len(slope)
width = len(slope[0])
pos = (0,0) # left - / right +, up - / down +

trees_hit = 0
while(pos[1] < heigh):
    print(slope[pos[1]][pos[0]])
    if(slope[pos[1]][pos[0]] == "#"):
        trees_hit += 1
    pos = ((pos[0] + right) % width, pos[1] + down)
    print(pos)


print(trees_hit)

