with open('./input02-a.txt') as f:
    infile = f.read().splitlines()

valid = 0
for line in infile:
    [cond, letter, pwd] =  line.split(" ", 2)
    [min_pos, max_pos] = cond.split("-")
    letter = letter[0]
    min_pos = int(min_pos) -1
    max_pos = int(max_pos) -1

    if (not (pwd[min_pos] == letter and pwd[max_pos] == letter)) and (pwd[min_pos] == letter or pwd[max_pos] == letter):
        valid += 1


print(pwd.count(letter))
print(min_pos, max_pos, letter, pwd)
print(valid)
