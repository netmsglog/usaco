"""
ID: yscript1
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')
n = int( fin.readline().strip())
heights = []
for i in range(n):
    heights.append( int(fin.readline().strip()))
heights.sort()

allgaps = [(i, i+17) for i in range(0,84)]
#print(allgaps)
# max height 100
mincost = n * 100 * 100

for gap in allgaps:
    cost = 0
    for h in heights:
        if h >= gap[0] and h <= gap[1]:
            cost = cost + 0
        if h < gap[0]:
            cost = cost + (gap[0]-h)*(gap[0]-h)
        if h > gap[1]:
            cost = cost + (h - gap[1])*(h - gap[1])
    if cost < mincost:
        mincost = cost

#print(n)
#print(heights)
#print(len(heights))
#ending = False
# cost = 0
# changes = []
# while True:
#     heights.sort()
#     lowest = heights[0]
#     highest = heights[-1]
#     print("L:",lowest, "H:", highest)
#     mid = (highest - lowest - 17) // 2
#     remain = (highest - lowest - 17) % 2
#     print("mid=",mid,"remain=",remain)
#     if mid < 0:
#         break
#     if mid == 0 and remain==0:
#         break
#     else:
#         #newlow = lowest + mid
#         #newhigh = highest - mid - remain
#         #print("newlow=",newlow, "newhigh=",newhigh)
#         #cost = cost + (newlow-lowest)*(newlow - lowest) +(newhigh - highest)*(newhigh - highest)
#         print("before:", heights)
#         # lows = 0
#         # while heights[0]==lowest:
#         #     #cost = cost + (newlow-lowest)*(newlow - lowest)
#         #     lows = lows + 1
#         #     heights.pop(0)
#         # highs = 0
#         # while heights[-1]==highest:
#         #     #cost = cost + (newhigh - highest)*(newhigh - highest)
#         #     highs = highs + 1
#         #     heights.pop(-1)
#         # print("lows=",lows,"highs=",highs, "mid=",mid, "remain=", remain)
#         # cost = cost + min(lows,highs)*(mid+remain)*(mid+remain) + max(lows,highs)*mid*mid
#         # #heights.pop(0)
#         #heights.pop(-1)
#         head = heights.pop(0)
#         tail = heights.pop(-1)
#         cost = cost + mid*mid +  (mid+remain)*(mid+remain)
#         print("cost=", cost)
#         changes.append(head + mid)
#         changes.append(tail - mid - remain)
#         print("changes=", changes)
#         print(heights)
#         if len(heights) < 2:
#             break
#         #heights[0] = newlow
#         #heights[-1] = newhigh
fout.write (str(mincost)+'\n')
fout.close()