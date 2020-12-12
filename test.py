"""
ID: yscript1
LANG: PYTHON3
TASK: test
"""
fin = open ('test.in', 'r')
fout = open ('test.out', 'w')
x = list(map(int, fin.readline().split()))
total = sum(x)
fout.write (str(total) + '\n')
fout.close()