def isvalid(i):
    res = [int(x) for x in str(i)]
    for j in range(len(res) -1 ):
        if res[j] > res[j+1]:
            return False

    i = str(i)
    tmp_double = False
    double = False
    for j in range(1,len(i) -1 ):
        tmp_double = False
        if i.count("{}".format(i[j])) == 2 :
            tmp_double = True
            break
    double = tmp_double or double
    return double

count = 0
for i in range(265275, 781584):
    if isvalid(i):
        count = count +  1

print count

print isvalid(112232)
print isvalid(112233)
print isvalid(123444)
print isvalid(111122)
