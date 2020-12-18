"""
ID: yscript1
LANG: PYTHON3
TASK: swap
"""
fin = open ('swap.in', 'r')
fout = open ('swap.out', 'w')
n,k = map(int, fin.readline().strip().split())
a1,a2 = map(int, fin.readline().strip().split())
b1,b2 = map(int, fin.readline().strip().split())
cows = [i for i in range(1,n+1)]
print(cows)
def reverse(cows, start, end):
    t = cows[0:start]
    t.extend(cows[start:end+1][::-1])
    t.extend(cows[(end+1):])
    return t

t = cows[:]
for i in range(k):
    t = reverse(t, a1-1,a2-1)
    t = reverse(t, b1-1,b2-1)
    #print(i, t)
print(t)
fout.write('\n')
fout.close()