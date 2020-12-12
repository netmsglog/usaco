"""
ID: yscript1
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
n,m = map(int, fin.readline().split())
farmers = []
for i in range(m):
    p, a = map(int, fin.readline().split())
    farmers.append({'price':p,'amount':a})

nf = sorted(farmers, key = lambda i:i['price'])

#print(nf)
remain = n
cost = 0
for farmer in nf:
    if farmer['amount'] >= remain:
        cost = cost + remain * farmer['price']
        break
    else:
        cost = cost + farmer['amount'] * farmer['price']
        remain = remain - farmer['amount']

#print(cost)
fout.write (str(cost) + '\n')
fout.close()