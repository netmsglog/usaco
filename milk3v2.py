"""
ID: yscript1
LANG: PYTHON3
TASK: milk3
"""
fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')
a,b,c = map(int, fin.readline().strip().split())

# initial_values
limits=[a,b,c]
buckets=[0,0,c]
names=['A','B','C']
possible_c=[]
visited={}

def pour_bucket(buks,f,t):
    global limits
    print(buks, f, t, names[f], "=>", names[t])
    total = buks[t] + buks[f]
    if total >= limits[t]:
        buks[f] = total - limits[t]
        buks[t] = limits[t]
    else:
        buks[f] = 0
        buks[t] = total
    #return buks.copy()

def traverse(buks):
    global possible_c
    global visited
    print("traverse:", buks)
    if str(buks) in visited:
        print("already has state:",buks, "visited=",visited)
        return
    visited[str(buks)] =  1
    if buks[0]==0:
        print("possible C:", buks[2])
        possible_c.append(buks[2])
    
    for i in range(3):
        for j in range(3):
            if i!=j:
                pour_bucket(buks, i, j)
                t=buks[:]
                print("t=", t)
                traverse(t)

traverse(buckets)
possible_c = sorted(set(possible_c))
fout.write(' '.join(map(str,possible_c)))
fout.write('\n')
fout.close()