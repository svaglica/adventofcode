fishes=[0]*9
with open('./input06.txt') as f:
    tmp = [int(x) for x in f.readline().split(',')]
    fishes = [tmp.count(y) for y in range(9)]

def reproduce():
    sixes=fishes[6]
    heights=fishes[8]
    for i in range(9):
        if i == 0:
            fishes[7]+=fishes[0]
            fishes[8]=fishes[0]
        elif i == 6:
            fishes[5]=sixes
        elif i == 8:
            fishes[7]=heights
        else:
            fishes[i-1]=fishes[i]

for i in range(256):
    reproduce()

print(sum(fishes))
