"""
ID: yscript1
LANG: PYTHON3
TASK: beads
"""
# return a broken string , start at pos
def get_broken_string(s, pos):
    return s[pos:] + s[:pos]

def max_head(s, l):
    cnt = 0
    pos = 0
    first = s[pos]
    while pos <= l:
        if first == 'w':
            if s[pos] != 'w':
                first = s[pos]
        if s[pos]==first or s[pos]=='w':
            cnt = cnt + 1
        else:
            break
        pos = pos + 1
    return cnt

def max_tail(s):
    l = len(s)
    cnt = 0
    pos = l - 1
    first = s[pos]
    while pos >= 0:
        if first == 'w':
            if s[pos] != 'w':
                first = s[pos]
        if s[pos]==first or s[pos]=='w':
            cnt = cnt + 1
        else:
            return cnt, pos
            #break
        pos = pos - 1
    return cnt, pos

# # only for testing
# s = 'wwwbbrwrbrbrrbrbrwrwwrbwrwrrb'
# ll = len(s)
# max = 0
# for i in range(ll):
#     bs = get_broken_string(s, i)
#     mh = max_head(bs)
#     mt = max_tail(bs)
#     if (mh+mt) > max:
#         print('mh:',mh, 'mt:',mt)
#         max = mh + mt

# print(max)

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
nums = int( fin.readline().strip())
beads = fin.readline().strip()
max_collected = 0
for i in range(nums):
    bs = get_broken_string(beads, i)
    mt, p = max_tail(bs)
    #print(mt,p)
    mh = max_head(bs, p)
    
    if (mh+mt) > max_collected:
        max_collected = mh + mt

fout.write (str(max_collected) + '\n')
fout.close()