"""
ID: yscript1
LANG: PYTHON3
TASK: barn1
"""
# aborted version, not necessary
# def merge_list_by(l, gap):
#     ll = []
#     pos = 0
#     last = l[0]
#     tl = []
#     while pos < len(l):
#         if l[pos] - last <= gap:
#             tl.append( l[pos] )
#         else:
#             if len(tl) > 0:
#                 ll.append(tl)
#             tl = [ l[pos] ]
#         last = l[pos]
#         pos = pos + 1
#     if len(tl) > 0:
#         ll.append(tl)
#     return ll

# l is a list of list , when reach limit, return immediately
def merge_listlist_by(l, gap, limit):
    ll = []
    pos = 1
    last = l[0][-1] 
    tl = l[0]
    while pos < len(l):
        if l[pos][0] - last <= gap:
            tl.extend( l[pos] ) 
            #print("tl=", tl)
            #print("len(ll)=",len(ll), "len(l)-pos=", len(l)-pos)
            if len(ll) + len(l) - pos == limit :  #find the answer
                ll.append(tl)
                for i in range(pos+1, len(l)):
                    ll.append(l[i])
                return ll 
            last = tl[-1]
        else:
            if len(tl) > 0:
                ll.append(tl)
            tl = l[pos]
            last = tl[-1]
        pos = pos + 1
    if len(tl) > 0:
        ll.append(tl)
    return ll

def sum_gaps(l):
    gap = 0
    for item in l:
        gap = gap + ( item[-1] - item[0] + 1)
    return gap

fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')
m,s,c = map(int, fin.readline().strip().split())
occupied_stalls = []
for i in range(c):
    occupied_stalls.append(int(fin.readline().strip()))

merged = [ [el] for el in sorted(occupied_stalls)]
step = 1
while len(merged)  > m:
    merged = merge_listlist_by(merged, step, m)
    step = step + 1

print(merged)
#print(sum_gaps(merged))
gaps = sum_gaps(merged)
fout.write (str(gaps)+'\n')
fout.close()