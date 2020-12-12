"""
ID: yscript1
LANG: PYTHON3
TASK: ride
"""
import sys
def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

def prod(l):
    result = 1
    for c in l:
        result = result * ( ord(c) - ord('A') + 1)
    return result

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
comet = fin.readline().strip()
group = fin.readline().strip()
if prod(comet) % 47  == prod(group) % 47:
    fout.write('GO\n')
else:
    fout.write('STAY\n')

fout.close()