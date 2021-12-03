from numpy import sum

with open('./input01-a.txt') as f:
    depths = [int(x) for x in f.readlines()]

win_size=3
incr=0

for i in range(len(depths)-3):
    sum1= sum(depths[i:i+win_size])
    sum2= sum(depths[i+1:i+1+win_size])
    print(sum1,sum2)
    if (sum1 < sum2):
        incr += 1

print(incr)
