with open('./input02-a.txt') as f:
    infile = f.read().splitlines()

valid = 0
for line in infile:
    [cond, letter, pwd] =  line.split(" ", 2)
    [min_cond, max_cond] = cond.split("-")
    letter = letter[0]
    min_cond = int(min_cond)
    max_cond = int(max_cond)

    if pwd.count(letter) <= max_cond and pwd.count(letter) >= min_cond:
        valid += 1


print(pwd.count(letter))
print(min_cond, max_cond, letter, pwd)
print(valid)
