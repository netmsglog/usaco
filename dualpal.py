"""
ID: yscript1
LANG: PYTHON3
TASK: dualpal
"""

def is_palindromic(s):
    if s == s[::-1]:
        return True
    return False

BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

def is_dualpal(num):
    dual_cnt = 0
    for base in range(2, 11):
        if is_palindromic(to_base(num,base)):
            dual_cnt = dual_cnt + 1
            if dual_cnt >= 2:
                return True
    return False

fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')
n,s=map(int, fin.readline().strip().split())
cnt = 0
num = s + 1
while cnt < n:
    if is_dualpal(num):
        fout.write(str(num)+"\n")
        cnt = cnt + 1
    num = num + 1

fout.close()