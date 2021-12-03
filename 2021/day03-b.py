from numpy import digitize
with open('./input03.txt') as f:
    repport_original= [x for x in f.read().splitlines()]

ox_repport = repport_original.copy()
co2_repport = repport_original.copy()

def most_common(repport, i):
    ones=sum([int(x[i]) for x in repport])
    zeros=len(repport) - ones
    return int(ones >= zeros)

def least_common(repport, i):
    ones=sum([int(x[i]) for x in repport])
    zeros=len(repport) - ones
    return int(zeros > ones)

end=True
ox_end=True
co2_end=True
while(end):
    for i in range(12):
        if ox_end:
            if len(ox_repport) <= 1:
                ox_end=False
                ox_rating=ox_repport[0]
            else:
                val = most_common(ox_repport, i)
                ox_repport = [x for x in ox_repport if int(x[i])==val]

        if co2_end:
            if len(co2_repport) <= 1:
                co2_end=False
                co2_rating=co2_repport[0]
            else:
                val = least_common(co2_repport, i)
                co2_repport = [x for x in co2_repport if int(x[i])==val]
    end=(ox_end )


print(ox_rating)
print(co2_rating)

print(int(ox_rating, 2) * int(co2_rating, 2))
