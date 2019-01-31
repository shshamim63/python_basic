from collections import Counter
X=int(input())
shoes=Counter(map(int,input().split()))
N=int(input())
income=0
for i in range(0,N):
    size,price=map(int,input().split())
    if shoes[size]:
        income+=price
        shoes[size]-=1
print(income)