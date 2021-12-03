from numpy import digitize
with open('./input03.txt') as f:
    repport = [x for x in f.readlines()]

ones=[0]*12
zeros=[0]*12
gamma=''
eps=''

for line in repport:
    for bit in range(12):
        if int(line[bit])==0:
            zeros[bit]+=1
        else:
            ones[bit]+=1

for i in range(len(ones)):
    if ones[i] > zeros[i]:
        gamma+='1'
        eps+='0'
    else:
        gamma+='0'
        eps+='1'

print(gamma)
print(eps)
print(int(gamma, 2))
print(int(eps, 2))


print(int(gamma,2 ) * int(eps, 2))
