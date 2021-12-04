import numpy as np

with open('./input04.txt') as f:
    rng = [int(x) for x in f.readline().split(',')]

    raw_boards=f.read().splitlines()[1:]
    raw_boards=list(filter(('').__ne__, raw_boards))

#print(rng)
#print(raw_boards)

boards=[]
for i in range(int(len(raw_boards)/5)):
    bd=[]
    for j in range(5):
        bd+=[[int(x) for x in raw_boards[5*i+j].split()]]
    boards += [bd]
#print(boards)

def check_win(wb):
    for j in range(len(boards)):
        bd = boards[j]
        for i in range(5):
            if bd[0][i] == bd[1][i] == bd[2][i] == bd[3][i] == bd[4][i]:
                print("WIN!!")
                print(bd)
                wb = bd
                return wb
            if bd[i][0] == bd[i][1] == bd[i][2] == bd[i][3] == bd[i][4]:
                print("WIN!!")
                print(bd)
                wb = bd
                return wb



j=0
print(rng)
winning_board=[]
for new_nb in rng:
    for bd in boards:
        for i in range(5):
            bd[i] = [-999 if x==new_nb else x for x in bd[i]]

    if j>=4:
        winning_board=check_win(winning_board)
        if winning_board :
            print(new_nb)
            print(winning_board)
            score = 0
            for i in range(5):
                score += sum([x if x != -999 else 0 for x in winning_board[i]])
            score *= new_nb
            print(score)
#            for bds in boards:
#                print(np.matrix(bds))
            exit(True)
    j+=1

exit(False)

