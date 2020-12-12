"""
ID: yscript1
LANG: PYTHON3
TASK: palsquare
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

fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')
base = int(fin.readline().strip())
for n in range(300):
    num = (n + 1) * (n + 1)
    num_normal = to_base(num, base)
    if is_palindromic(num_normal):
        fout.write(to_base(n+1, base))
        fout.write(" ")
        fout.write(num_normal)
        fout.write("\n")

fout.close()
#print(to_base(333,17))
# print(is_palindromic('1'))
# print(is_palindromic('40804'))
# print(is_palindromic('69696'))
# print(is_palindromic('323'))
# print(is_palindromic('4313'))