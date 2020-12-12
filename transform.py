"""
ID: yscript1
LANG: PYTHON3
TASK: transform
"""
def clockwise_90(l):
    size = len(l[0])
    ll = []
    for i in range(size):
        nstr = ''
        for j in range(size):
            nstr = nstr + l[size - j -1][i]
        ll.append(nstr)
    return ll

def clockwise_180(l):
    return clockwise_90( clockwise_90(l) )

def clockwise_270(l):
    return clockwise_90( clockwise_180(l) )

# reflection around a vertical line in the middle of pattern
def reflect(l):
    size = len(l[0])
    middle = size // 2
    ll = []
    for i in range(size):
        # as python string is immutable, we use list to let it mutable
        nstr = list(l[i])
        # swap around vertical line
        for j in range(middle):
            c = nstr[j] 
            nstr[j] = nstr[size - j - 1]
            nstr[size - j - 1] = c
        ll.append(''.join(nstr))
    return ll


# test clockwise_90
# print( clockwise_90(['@-@','---','@@-']))
# print( clockwise_90(['ABC','CBA','ACD']))
# print( clockwise_180(['ABC','CBA','ACD']))
# print( clockwise_270(['ABC','CBA','ACD']))
# print( reflect(['ABC','CBA','ACD']))
# print( reflect(['ABCD','CBAE','ACDF','CDEB']))

def which_transform(origin, dest):
    if clockwise_90(origin) == dest:
        return 1
    if clockwise_180(origin) == dest:
        return 2
    if clockwise_270(origin) == dest:
        return 3
    reflected = reflect(origin)
    if reflected == dest:
        return 4
    if clockwise_90(reflected) == dest or clockwise_180(reflected) == dest or clockwise_270(reflected) == dest:
        return 5
    if origin == dest:
        return 6
    return 7

fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
n = int( fin.readline().strip() )
origin = []
dest = []
for i in range(n):
    origin.append(fin.readline().strip())
for i in range(n):
    dest.append(fin.readline().strip())
#print(origin, dest)
result = which_transform(origin, dest)

fout.write (str(result)+'\n')
fout.close()