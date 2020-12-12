"""
ID: yscript1
LANG: PYTHON3
TASK: breedflip
"""
import sys
def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

fin = open ('breedflip.in', 'r')
fout = open ('breedflip.out', 'w')
n = int(fin.readline().strip())
stra = fin.readline().strip()
strb = fin.readline().strip()

# just find how many successive substrings are not different
pos = 0
diff = False
diff_cnt = 0
while pos < n:
    if stra[pos] != strb[pos]:
        if not diff:
            diff_cnt = diff_cnt + 1
            diff = True
    else:
        diff = False
    pos = pos + 1

fout.write(str(diff_cnt)+'\n')
fout.close()