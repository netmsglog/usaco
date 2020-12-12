y=open("breedflip.in", 'r')
n=int(y.readline())
strA=y.readline().strip()
strB=y.readline().strip()

print(strA)
print(strB)
pos=0
cnt=0
diff=False
while pos<n:
  if strA[pos] != strB[pos]:
    if not diff:
      print(pos)
      cnt=cnt+1
      diff=True
  else:
    diff=False
    print(-1)
  pos = pos+1

print(cnt)

