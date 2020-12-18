"""
ID: yscript1
LANG: PYTHON3
TASK: milk3
"""
from copy import copy
from collections import namedtuple
NP = namedtuple('NP', ['node', 'right'])

class Node(object):
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def get_routes(node, route=None):
    route = route or []
    # If this node has children, clone the route, so we can process
    # both the right and left child separately.
    if node.right:
        right_route = copy(route)

    # Process the main (left) route.  Pass the route on to the left 
    # child, which may return multiple routes.
    route.append(NP(node, False))
    routes = get_routes(node.left, route) if node.left else [route]

    # If there is a right child, process that as well.  Add the route
    # results.  Note that NP.right is set to True, to indicate a right path.
    if node.right:
        right_route.append(NP(node, True))
        right_routes = get_routes(node.right, right_route)
        routes.extend(right_routes)
    
    # Pass the results back
    return routes


fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')
a,b,c = map(int, fin.readline().strip().split())

# initial_values
limits=[a,b,c]
buckets=[0,0,c]
left_node=[1,0,0]
right_node=[2,2,1]
names=['A','B','C']

# building pour trees
max_depth = 10
depth = 0
def building_tree(rt):
    global depth
    global max_depth
    depth = depth + 1
    if depth >= max_depth:
        return
    rt.left = Node( left_node[rt.name])
    rt.right = Node( right_node[rt.name])
    building_tree(rt.left)
    depth = depth - 1
    building_tree(rt.right)
    depth = depth - 1

root = Node(2)
building_tree(root)

#routes = get_routes(root)
# print all paths
# for route in routes:
#     path = []
#     for np in route:
#         path.append(names[np.node.name])
#     print(path)

# start from root:C 

possible_c = []
temp = []
def pour_bucket(buks):
    print("new pour:", buks)
    for i,p in enumerate(buks):
        for j,q in enumerate(buks):
            if i!=j:
                t=buks[:]
                if limits[j]-q >= p:
                    t[j]=q+p
                    t[i]=0
                else:
                    t[i]=p-(limits[j]-q)
                    t[j]=limits[j]
                print("Pour ",names[i],names[j],t)
                if not t[-1] in possible_c and not t in temp:
                    if t[0]==0:
                        possible_c.append(t[-1])
                    temp.append(t)
                    pour_bucket(t)

# def pour_bucket(f,t):
#     global buckets
#     global possible_c
#     print("Pour ",names[f],"=>", names[t], buckets)
#     if buckets[f] == 0:
#         # nothing to happen
#         print("nothing to pour")
#         return
    
#     total = buckets[t] + buckets[f]
#     if total >= limits[t]:
#         buckets[f] = total - limits[t]
#         buckets[t] = limits[t]
#     else:
#         buckets[f] = 0
#         buckets[t] = total
#     print("After Pour ",names[f],"=>", names[t], buckets)
#     if buckets[0] == 0:
#         print("A is 0, adding ", buckets[2])
#         possible_c.append(buckets[2])
    

# not working
# routes = get_routes(root)
# possible_c = []
# for route in routes:
#     start = route[0]
#     for i in range(1, len(route)):
#         # if buckets[start.node.name]==0:
#         #     if buckets[0]==0:  # A bucket is 0
#         #         possible_c.append(buckets[2])
#         #     break  # terminate the route
#         pour_bucket(start.node.name, route[i].node.name)
#         if buckets[0]==0:  # A bucket is 0
#                 possible_c.append(buckets[2])
#         start = route[i]

# print(possible_c)
# possible_c = set(possible_c)
# print(possible_c)

# depth = 0
# def traverse(start):
#     global buckets
#     global depth
#     left = left_node[start]
#     right = right_node[start]
#     print("traverse: ", names[start],"depth:", depth, "left:", names[left], "right:", names[right])
#     if buckets[start]==0 or depth > 3:
#         print("buckets[start]=",buckets[start],"depth:",depth)
#         return
    
#     backup = buckets[left]
#     pour_bucket(start, left)
#     depth = depth + 1
#     traverse(left)
#     depth = depth - 1
#     buckets[left] = backup
#     backup = buckets[right]
    
#     pour_bucket(start, right)
#     depth = depth + 1
#     traverse(right)
#     depth = depth - 1
#     buckets[right] = backup

#def traverse()
# times = 0
# def tranverse(start):
#     global buckets
#     global times
#     # print(names[start])
#     if buckets[start]==0:
#         return
#     if times > 10:
#         return
#     times = times + 1
#     left = left_node[start]
#     right = right_node[start]
#     backup = buckets.copy()
#     pour_bucket(start, left)
#     if buckets[0]==0:
#         return
#     tranverse(left)
#     buckets = backup.copy()
#     pour_bucket(start, right)
#     tranverse(right)
#     if buckets[0]==0:
#         return

#tranverse(2)
#traverse(2)
pour_bucket(buckets)
possible_c = sorted(set(possible_c))
fout.write(' '.join(map(str,possible_c)))
fout.write('\n')
fout.close()