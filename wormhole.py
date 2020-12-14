"""
ID: yscript1
LANG: PYTHON3
TASK: wormhole
"""
from itertools import combinations 

fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
n = int(fin.readline().strip())
points = []
for i in range(n):
    x,y = map(int, fin.readline().strip().split())
    points.append((x,y))

def get_pairs(l):
    if len(l) == 2:
        return [[ (l[0], l[1]) ]]
    else:
        start = l[0]
        pairs = []
        for i in range(1, len(l) ):
            ll = l.copy()
            ll.remove( start )
            ll.remove( l[i] )
            #print(ll)
            for p in get_pairs(ll):
                #print("p=",p)
                tl = [ (start, l[i])]
                tl.extend(p)
                pairs.append( tl)
                #print("pairs=", pairs)
        return pairs

def sort_pair(p):
    pp = []
    for item in p:
        p1 = item[0]
        p2 = item[1]
        if p1[0] > p2[0]:
            pp.append((p2, p1))
        else:
            pp.append((p1, p2))
    return pp

#if two oblique lines are crossover
# def is_cross(l1, l2):
#     a = l1[0]
#     b = l1[1]
#     c = l2[0]
#     d = l2[1]
#     if a[0] != b[0] and a[1] != b[1]:
#         if c[0] != d[0] and c[1] != d[1]:
#             if a[1] == d[1] and c[1] == b[1]:
#                 return True
#     return False

# def is_cyclic(p):
#     ps = sort_pair(p)
#     for s in ps:  #s:  (a,b), (c,d)
#         if s[1][1] == s[0][1]: # y coordinates equal
#             # no point in the middle of s[0] and s[1]
#             no_middle = True
#             for pn in points:
#                 if pn[1] == s[0][1] and pn[0] > s[0][0] and pn[0] < s[1][0]:
#                     no_middle = False
#                     break
#             if no_middle:
#                 return True
#     # any cross line ?
#     all2lines = combinations(ps, 2)
#     for lines  in list(all2lines):
#         if is_cross( lines[0], lines[1]):
#             return True
#     return False

def find_testpath(ps):
    ally = set([ i[1] for i in ps])
    paths = {}
    for y in ally:
        for p in ps:
            if p[1] == y:
                if str(y) in paths:
                    paths[str(y)].append((p[0], p[1]))
                else:
                    paths[str(y)] = [(p[0], p[1]) ]
    for pa in paths:
        paths[pa].sort(key = lambda x: x[0])
    return paths

def get_pairpoint(p, pt):
    for item in p:
        if item[0] == pt:
            return item[1]
        if item[1] == pt:
            return item[0]

# ap is all testing path
def get_nextpoint_in_path(ap, pt):
    for idx in ap:
        p = ap[idx]
        for i in range(len(p)):
            if p[i]==pt:
                if i+1 < len(p):
                    return p[i+1]
    return None

# testing p
def worm_move(path, pairs, ap):
    #print("Moving", path, " with ", pairs)
    if len(path) < 2:
        return False
    for i in range(len(path)):
        visited = {}
        start = path[i]
        #print("start:", start)
        visited[str(start)] = True

        ending = False
        cyclic = False
        while not ending:
            pair_start = get_pairpoint(pairs, start)
            #print("pair_start:", pair_start)
            np = get_nextpoint_in_path(ap, pair_start)
            #print("np:", np)
            if np is None:
                ending = True
                break
            else:
                if str(np) in visited:
                    #print("cyclic:", np, "visited:", visited)
                    ending = True
                    cyclic = True
                else:
                    visited[str(np)] = True
                    start = np
        if cyclic:
            return True
    # after testing all points in a path, no cyclic
    return False

allp = get_pairs(points)
testing = find_testpath(points)

#print(allp)
#print(testing)

nums = 0
for pair in allp:
    pair_cyclic = False
    for t in testing:
        if worm_move(testing[t], pair, testing):
            pair_cyclic = True
            break
    if pair_cyclic:
        nums = nums + 1
        
fout.write (str(nums) + '\n')
fout.close()
