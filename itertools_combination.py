from itertools import combinations
S,K=input().split()
S=sorted(S)
print(*[''.join(res) for i in range(1,int(K)+1) for res in combinations(S,i)],sep='\n')