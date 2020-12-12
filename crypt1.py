"""
ID: yscript1
LANG: PYTHON3
TASK: crypt1
"""
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
n = int(fin.readline().strip())
digits = list(map(int, fin.readline().strip().split()))
digits = sorted(digits)
digits_str = str(digits)

def is_valid(num):
    nstr = str(num)
    for c in nstr:
        if c not in digits_str:
            return False
    return True

#print(digits)
valid_abc = []
for i in range(digits[0]*111, digits[-1]*111 + 1):
    if is_valid(i):
        valid_abc.append(i)

valid_de = []
for i in range(digits[0]*11, digits[-1]*11 + 1):
    if is_valid(i):
        valid_de.append(i)       

#print(valid_abc)
#print(valid_de)
solutions = 0
for i in valid_abc:
    for j in valid_de:
        d = j // 10 % 10
        e = j % 10
        di = d * i
        if di > 999:
            continue
        if not is_valid(di):
            continue
        ei = e * i
        if ei > 999:
            continue
        if not is_valid(ei):
            continue
        sum = di*10 + ei
        if sum > 9999:
            continue
        if is_valid(di*10 + ei):
            #print(i, '*', j, '=',di*10 + ei, di, ei )
            solutions = solutions + 1

#print(solutions)
fout.write (str(solutions) + '\n')
fout.close()