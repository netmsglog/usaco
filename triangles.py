"""
ID: yscript1
LANG: PYTHON3
TASK: triangles
"""
from itertools import combinations

# judge if it is a valid tri with parallet to x-axis and y-axis
def is_valid_tri(tri):
    if tri[0][0] != tri[1][0] and tri[0][0] != tri[2][0] and  tri[1][0] != tri[2][0]:
        return False
    if tri[0][1] != tri[1][1] and tri[0][1] != tri[2][1] and  tri[1][1] != tri[2][1]:
        return False
    return True

def area_of_tri(tri):
    x1 = abs(tri[0][0] - tri[1][0])
    x2 = abs(tri[0][0] - tri[2][0])
    x = max(x1,x2)
    y1 = abs(tri[0][1] - tri[1][1])
    y2 = abs(tri[0][1] - tri[2][1])
    y = max(y1, y2)
    return x*y

fin = open ('triangles.in', 'r')
fout = open ('triangles.out', 'w')
n = int(fin.readline().strip())
points = []
for i in range(n):
    x, y = map(int, fin.readline().strip().split() )
    points.append((x,y))
#print(points)
tris = combinations(points, 3)
maxarea = 0
for tri in list(tris):
    #print(tri)
    if is_valid_tri(tri): #to judge if it is a right triangle
        area = area_of_tri(tri)
        if area >= maxarea:
            maxarea = area
#print(maxarea)
fout.write(str(maxarea)+'\n')
fout.close()