"""
ID: yscript1
LANG: PYTHON3
TASK: gift1
"""
import sys
def print_err(*args):
    sys.stderr.write(' '.join(map(str,args)) + '\n')

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
np = int(fin.readline().strip())
members = {}
for i in range(np):  # read np members' name
    name = fin.readline().strip()
    members[name] = 0
for i in range(np):  # read np groups of giving
    name = fin.readline().strip()  # person sending
    amount_of_money, num_of_receiver = map(int,  fin.readline().strip().split())
    if num_of_receiver > 0:
        to_send = amount_of_money // num_of_receiver
        to_remain = amount_of_money % num_of_receiver
        for j in range(num_of_receiver):
            r_name = fin.readline().strip()
            members[r_name] += to_send  # receiver get money
            members[name] -= to_send # sender reduce money
        #members[name] += to_remain  # sender get remain
    else:
        members[name] += amount_of_money
    for name in members:
        print_err(name, members[name])
    print_err('-------------')

for name in members:
    fout.write(name + ' ' + str(members[name]) + '\n')

fout.close()