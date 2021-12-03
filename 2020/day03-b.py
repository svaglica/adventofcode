with open('./input03-a.txt') as f:
    montain = f.read().splitlines()

# right, down
slopes = ((1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2))
heigh = len(montain)
width = len(montain[0])

factor_trees = 1

for slope in slopes:

    trees_hit = 0
    pos = (0,0) # left - / right +, up - / down +

    while(pos[1] < heigh):
        if(montain[pos[1]][pos[0]] == "#"):
            trees_hit += 1
        pos = ((pos[0] + slope[0]) % width, pos[1] + slope[1])

    factor_trees *= trees_hit

print(factor_trees)

