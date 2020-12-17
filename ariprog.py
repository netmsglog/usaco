"""
ID: yscript1
LANG: PYTHON3
TASK: ariprog
"""

# warning: this problem should be resolved in C/C++/java
# the python version will run out of the 5 seconds time limitation

fin = open ('ariprog.in', 'r')
fout = open ('ariprog.out', 'w')
# N (3 <= N <= 25), the length of progressions for which to search
n = int(fin.readline().strip())
# M (1 <= M <= 250), an upper bound to limit the search to the bisquares with 0 <= p,q <= M.
m = int(fin.readline().strip())
bisqs = []
for p in range(0,m+1):
    for q in range(0,m+1):
        bisqs.append(p*p + q*q)

bisqs = list(set(bisqs))
bisqs.sort()
#print(bisqs)
maxpq = max(bisqs)
maxa = maxpq - (n-1)
maxb = maxpq // (n-1) + 1

bistable =[0 for i in range(125001)]
#bistable = {}
for item in bisqs:
    bistable[item] = 1
#print(len(bistable), maxpq, maxa, maxb)
seqs = []
for start in range(0, len(bisqs)-n+1):
    for item in range(start+1, len(bisqs)-n+2):
        gap = bisqs[item] - bisqs[start]
        #if gap > maxb:
        #    continue
        #print("item=",item,"gap=",gap)
        next = 2
        valid = True
        while next < n:
            num = bisqs[start] + next*gap
            #print(num)
            if num > 125000 or bistable[num]==0: # num not in bistable:
                valid = False
                break
            next = next + 1
        if valid:
            seqs.append((bisqs[start], gap))

# iters = len(bisqs) - n
# for i in range(iters):
#     print(i)
#     #try_list(bisqs, n)
#     bisqs.pop(0)

# bistable = {}
# for item in bisqs:
#     bistable[item] = 1

# print("len of bisqs", len(bisqs))
# maxpq = max(bisqs)
# maxa = maxpq - (n-1)
# maxb = maxpq // (n-1) + 1
# print(maxpq, maxa, maxb)
# possible = 0
# for a in range(0, maxa+1):
#     for b in range(1, maxb+1):
#         if a + (n-1)*b in bistable:
#             possible = possible + 1
# print(possible)

# old time-consuming solution , not pass test #1 with 21, 200
# max possible a or b
# maxpq = max(bisqs)
# # a + (n-1)b <= maxpq, maxa when b=1
# maxa = maxpq - (n-1)
# # maxb when a = 0
# maxb = maxpq // (n-1) + 1
# print("maxpq",maxpq,"maxa=",maxa,"maxb=",maxb)
# seqs = []
# for b in range(1, maxb+1):
#     na = maxpq-(n-1)*b
#     print("b=",b, "na=", na)
#     for a in range(0,na):
#     #nb = (maxpq - a) // (n-1) + 1
#     #print("a=",a, "nb=",nb)
#     #for b in range(1,nb+1):
#         #if a + (n-1)*b > maxpq:
#         #    continue
#         findseq = True
#         for i in range(n):
#             if (a + i*b) not in bistable:
#                 findseq = False
#                 break
#         if findseq:
#             seqs.append((a, b))
#         #print(a,b)


if len(seqs) > 0:
    seqs.sort(key=lambda x:x[1])
    for s in seqs:
        fout.write(str(s[0])+' '+str(s[1])+'\n')
else:
    fout.write('NONE\n')
fout.close()