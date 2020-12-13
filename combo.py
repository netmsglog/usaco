"""
ID: yscript1
LANG: PYTHON3
TASK: combo
"""

# return all near numbers with 2 positions
def near_number(num, n):
    options = []
    g1 = (num + 1) % n
    if g1 == 0:
        g1 = n
    g2 = (num + 2) % n
    if g2 == 0:
        g2 = n
    l1 = (num - 1) % n
    if l1 == 0:
        l1 = n
    l2 = (num - 2) % n
    if l2 == 0:
        l2 = n
    options.extend([l2, l1, num, g1, g2])
    
    return options

fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
n = int(fin.readline().strip())
john = list(map(int, fin.readline().strip().split()))
master = list(map(int, fin.readline().strip().split()))
#print(n, john, master)
oj = [near_number(i,n) for i in john]
om = [near_number(i,n) for i in master]
#print(oj)
#print(om)
combinations_table = {}
for a in oj[0]:
    for b in oj[1]:
        for c in oj[2]:
            key = str([a,b,c])
            if key not in combinations_table:
                combinations_table[key] = 1

for a in om[0]:
    for b in om[1]:
        for c in om[2]:
            key = str([a,b,c])
            if key not in combinations_table:
                combinations_table[key] = 1

cnts = len(combinations_table)
fout.write (str(cnts) + '\n')
fout.close()