from collections import defaultdict
n,m=map(int,input().split())
d=defaultdict(list)
l=list()
for i in range(0,n):
    d[input()].append(i+1)
for i in range(0,m):
    l.append(input())
for val in l:
    if val in d:
        print(' '.join(map(str,d[val])))
    else:
        print(-1)