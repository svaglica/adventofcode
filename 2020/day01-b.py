with open('./input01-a.txt') as f:
    costs = f.read().splitlines()

print(costs)
for i in range(len(costs) - 2 ):
#    print(range(i, len(costs)))
    for j in range(i+1, len(costs) - 1):
        for k in range (j+1, len(costs)):
            total = int(costs[i]) + int(costs[j]) + int(costs[k])
            print(total)
            if (total == 2020):
                print(int(costs[i]) * int(costs[j]) * int(costs[k]))
                exit(0)

print("not found")
exit(0)
