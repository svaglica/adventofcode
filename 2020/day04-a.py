with open('./input04-a.txt') as f:

    #passports = f.read().splitlines()
    passports = list()
    passports.append("")
    passports_number = 0
    for line in f:
        if line == "\n":
            passports_number += 1
            passports.append("")
        else:
            passports[passports_number] += line.replace("\n", " ")

fields = ("byr",
          "iyr",
          "eyr",
          "hgt",
          "hcl",
          "ecl",
          "pid",
          "cid")

valid_passports = 0
for passport in passports:
    found = True
    for field in fields[:-1]: # last one not necessary
        if field not in passport:
            found = False

    if found:
        valid_passports +=1

print(valid_passports)
