import sys
import six
print(sys.maxsize)
print(six.MAXSIZE)

with open('day22.txt') as f:
    shuffles = f.read().splitlines()

deck_size = 119315717514047

deck = list(range(deck_size))

times = 0
while times < 101741582076661:
    times += 1
    print(times)
    for line in shuffles:
        if 'cut' in line:
            size = int(line[3:])
            if size > 0:
                for i in range(size):
                    deck.append(deck.pop(0))
            elif size < 0:
                for i in range(abs(size)):
                    deck.insert(0, deck.pop(deck_size -1 ))
        elif 'increment' in line:
            n = int(line[19:])
#            new_stack = [0] * deck_size
#            for i in range(deck_size):
#                new_stack[(i*n) % deck_size] = deck[i]
#            deck = new_stack
        elif 'stack' in line:
            deck.reverse()

print(deck[2020])
