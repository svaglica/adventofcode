Number = list()

with open('./pic.txt') as f:
    while True:
        c = f.read(1)
        if '\n' == c:
            break
        Number.append(int(c))

layers = list()
zeros = 0
ones = 0
twos = 0
min_zeros = 9999999
min_mul = 0

width = 25
height = 6
nb_layers = len(Number) // (width * height)
layer_size = width * height


for i in range(nb_layers):
    zeros = 0
    ones = 0
    twos = 0
    for j in range(layer_size):
        if Number[i * layer_size + j] == 0:
            zeros +=1

        elif Number[i * layer_size + j] == 1:
            ones +=1
        elif Number[i * layer_size + j] == 2:
            twos +=1

    layers.append((zeros,ones,twos))
    if zeros < min_zeros:
        min_zeros = zeros
        min_mul = ones * twos

final_pic = list()
color = 2

for i in range(layer_size):
    color = 2
    for j in range(nb_layers):
        if color == 2:
            color = Number[j * layer_size + i]
        else:
            break

    final_pic.append(int(color))

print(final_pic)

matrix = []
for i in range(6):
#    print(final_pic[nb_layers * 25 : nb_layers * 26])
    matrix.append(final_pic[i * 25 : (i+1) * 25])

for e in matrix:
    print(e)









