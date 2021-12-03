import sys
import itertools

def get_val(a, pos, mode, rel=None):
    if mode == 0:
        return a[a[pos]]
    elif mode == 1:
        return a[pos]
    elif mode ==2:
        return a[a[pos] + rel]

def set_val(a, pos, mode, val, rel=None):
    if mode == 0:
       a[a[pos]] = val
    elif mode == 1:
       a[pos] = val
    if mode == 2:
       a[a[pos] + rel] = val

def get_x_ball(screen):
    screen[2::3].count(2)

def get_x_paddle(screen):

def intcode_v3(a=None, init=None):
    i = 0
    rel_base = 0
    output = list()
    while a[i]!=99:
        if a[i] % 100 == 1:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10
            t = a[i] // 10000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            set_val(a, i+3, t, val=f + s, rel=rel_base)
            i = i+4
        elif a[i] % 100 == 2:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10
            t = a[i] // 10000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            set_val(a, i+3, t, f * s, rel=rel_base)

            i = i+4

        elif a[i] % 100 == 3:
            t = a[i] // 100 % 10
            set_val(a, i+1, t, val=init.pop(0), rel=rel_base)
            i += 2

        elif a[i] % 100 == 4:
            t = a[i] // 100 % 10
            output.append(get_val(a, i+1, t, rel_base))
            i = i+2

        elif a[i] % 100 == 5:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            if f != 0:
                i = s
            else:
                i = i+3

        elif a[i] % 100 == 6:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            if f == 0:
                i = s
            else:
                i = i+3

        elif a[i] % 100 == 7:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10
            t = a[i] // 10000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            if f < s:
               # a[a[i+3] + offset_t] = 1
                set_val(a, i+3, t, 1, rel=rel_base)
            else:
                #a[a[i+3] + offset_t] = 0
                set_val(a, i+3, t, 0, rel=rel_base)
            i += 4
        elif a[i] % 100 == 8:
            f = a[i] // 100 % 10
            s = a[i] // 1000 % 10
            t = a[i] // 10000 % 10

            f = get_val(a, i+1, f, rel_base)
            s = get_val(a, i+2, s, rel_base)

            if f == s:
#                a[a[i+3] + offset_t] = 1
                set_val(a, i+3, t, 1, rel=rel_base)
            else:
#               a[a[i+3] + offset_t] = 0
                set_val(a, i+3, t, 0, rel=rel_base)
            i += 4

        elif a[i] % 100 == 9:
            f = a[i] // 100 % 10
            f = get_val(a, i+1, f, rel_base)

            rel_base += f
            i += 2
    return output


b=[2,380,379,385,1008,2119,899068,381,1005,381,12,99,109,2120,1101,0,0,383,1101,0,0,382,20101,0,382,1,20101,0,383,2,21101,37,0,0,1105,1,578,4,382,4,383,204,1,1001,382,1,382,1007,382,37,381,1005,381,22,1001,383,1,383,1007,383,20,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,35,381,1006,381,161,1101,0,1,384,20102,1,392,1,21102,1,18,2,21102,0,1,3,21101,0,138,0,1105,1,549,1,392,384,392,20102,1,392,1,21101,18,0,2,21101,0,3,3,21102,1,161,0,1105,1,549,1102,0,1,384,20001,388,390,1,20102,1,389,2,21101,0,180,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21002,389,1,2,21101,205,0,0,1105,1,393,1002,390,-1,390,1102,1,1,384,21002,388,1,1,20001,389,391,2,21102,1,228,0,1106,0,578,1206,1,261,1208,1,2,381,1006,381,253,20102,1,388,1,20001,389,391,2,21102,1,253,0,1106,0,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21102,279,1,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,1,304,0,1106,0,393,1002,390,-1,390,1002,391,-1,391,1102,1,1,384,1005,384,161,20101,0,388,1,20102,1,389,2,21101,0,0,3,21102,338,1,0,1106,0,549,1,388,390,388,1,389,391,389,21002,388,1,1,20101,0,389,2,21102,4,1,3,21102,1,365,0,1105,1,549,1007,389,19,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,251,16,15,1,1,18,109,3,22102,1,-2,1,21202,-1,1,2,21102,1,0,3,21101,0,414,0,1106,0,549,21201,-2,0,1,22102,1,-1,2,21102,1,429,0,1105,1,601,2102,1,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22101,0,-3,-7,109,-8,2105,1,0,109,4,1202,-2,37,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2105,1,0,109,3,1202,-1,37,593,201,-2,593,593,101,639,593,593,21001,0,0,-2,109,-3,2105,1,0,109,3,22102,20,-2,1,22201,1,-1,1,21101,373,0,2,21102,698,1,3,21101,740,0,4,21101,630,0,0,1106,0,456,21201,1,1379,-2,109,-3,2106,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,2,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,0,0,2,0,0,2,2,0,2,0,2,2,2,0,1,1,0,2,2,2,0,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,0,2,0,2,2,2,2,2,2,0,2,0,0,0,0,1,1,0,0,0,0,2,2,2,2,0,2,0,0,2,2,0,0,2,2,2,0,2,2,2,0,2,2,0,2,0,2,0,2,0,2,0,1,1,0,2,2,2,2,0,2,2,2,2,2,2,0,2,2,2,2,2,2,2,0,2,2,0,0,2,2,2,0,0,0,2,2,2,0,1,1,0,0,2,2,2,2,2,2,2,2,0,2,0,2,2,0,0,2,2,2,0,2,2,0,2,2,2,0,2,0,0,0,0,2,0,1,1,0,2,2,0,2,0,0,2,2,0,2,2,0,2,2,0,2,2,2,2,2,2,2,2,0,0,0,2,2,2,0,2,2,0,0,1,1,0,2,2,2,0,0,2,2,2,2,0,2,2,0,0,2,2,2,2,0,2,0,2,2,2,2,2,2,2,2,0,2,0,0,0,1,1,0,0,0,2,2,2,2,0,2,2,2,0,2,2,0,2,2,0,2,2,2,0,2,2,0,0,0,2,2,0,2,2,0,0,0,1,1,0,0,2,0,2,0,0,0,2,2,0,2,0,0,0,2,0,0,2,2,0,2,2,2,0,2,2,2,0,2,0,2,2,0,0,1,1,0,2,2,2,2,2,0,0,2,0,2,2,0,2,2,2,0,0,0,2,2,2,0,0,2,2,0,2,2,2,0,2,2,0,0,1,1,0,0,2,2,2,2,0,0,2,0,0,2,2,2,2,0,2,2,2,0,0,0,2,0,0,0,2,2,0,2,0,2,2,2,0,1,1,0,2,2,0,0,0,2,2,2,0,0,2,0,0,0,0,2,2,2,2,0,2,0,2,2,0,0,2,0,0,2,2,2,2,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,7,6,62,46,97,31,39,45,95,95,98,48,29,84,17,69,15,63,97,49,94,40,66,35,55,30,26,68,72,37,25,72,98,71,57,16,63,47,30,4,9,59,42,34,51,23,13,79,75,82,84,39,54,12,3,73,15,28,7,59,29,93,5,36,1,53,52,40,32,60,96,1,35,3,79,92,40,97,77,29,86,62,31,66,46,29,45,96,18,38,8,65,28,74,37,96,59,46,7,41,47,11,94,49,74,67,5,64,14,75,50,61,42,93,61,4,75,42,56,36,38,49,24,58,81,2,25,62,68,27,94,81,65,54,8,36,56,5,97,27,78,78,94,33,75,11,1,1,41,52,92,8,26,66,58,10,85,33,34,87,41,81,24,4,5,11,18,97,65,25,47,39,36,61,59,21,75,5,29,93,81,33,17,96,58,3,22,67,87,87,4,96,37,11,74,21,55,51,67,47,40,29,96,49,89,72,96,64,31,88,47,49,51,91,46,42,37,27,58,40,73,49,3,36,98,19,65,14,78,96,97,70,58,45,66,67,43,66,65,44,84,40,85,39,87,57,90,72,77,38,59,90,91,67,19,14,63,1,89,21,53,40,53,16,62,20,74,62,72,45,29,87,48,81,39,89,21,14,49,56,53,76,58,75,40,96,11,12,60,41,13,53,53,77,3,66,6,16,7,64,75,22,21,29,22,78,63,15,2,66,53,19,2,1,83,11,61,34,53,53,40,66,88,78,40,59,46,49,21,38,69,54,52,20,89,27,82,54,2,69,27,35,65,37,13,27,84,69,64,49,95,36,88,58,16,86,74,82,45,33,27,81,16,10,3,33,62,80,37,40,24,60,27,27,72,53,89,45,48,42,80,96,27,81,22,25,39,70,31,29,50,38,96,30,7,66,93,20,83,57,57,98,10,16,58,63,8,26,72,94,67,55,1,98,4,50,51,88,97,95,97,40,58,97,97,36,72,58,76,64,48,11,94,1,97,34,30,13,36,8,14,6,70,86,91,18,41,66,37,59,71,38,86,74,89,96,19,69,85,26,68,86,59,31,90,76,82,11,74,83,29,34,74,37,25,31,6,85,60,44,43,11,73,24,6,91,7,96,3,41,58,9,29,3,89,36,19,66,66,12,35,46,14,24,56,87,71,16,94,27,88,7,18,22,30,52,90,42,18,39,45,68,54,50,74,27,42,1,24,30,5,60,24,20,91,33,57,55,60,6,58,52,27,13,85,98,27,8,67,66,33,16,33,15,88,73,75,51,90,90,27,88,32,60,20,34,86,67,38,83,76,19,67,36,63,50,56,41,37,40,37,34,75,52,82,60,25,57,62,82,34,53,82,1,49,9,24,35,22,86,60,14,75,63,14,5,37,75,96,21,64,39,74,7,59,8,42,96,7,14,43,76,62,70,16,30,3,36,62,77,68,95,60,19,45,7,62,14,24,30,91,91,26,11,73,2,74,8,60,17,96,74,5,88,72,85,41,57,47,22,42,4,52,42,48,73,52,43,87,49,29,49,24,97,76,30,34,75,24,58,23,54,4,73,56,84,11,77,60,59,78,5,5,79,45,94,47,49,84,38,54,48,86,76,27,23,42,73,42,2,64,33,63,70,1,86,5,1,77,43,16,34,61,44,28,76,34,76,16,89,56,72,12,28,37,38,5,23,13,49,899068]
for i in range(100000):
    b.append(0)
screen = intcode_v3(b, [2])
print(screen[2::3].count(2))
print('done')

