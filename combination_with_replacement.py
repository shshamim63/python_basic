from itertools import combinations_with_replacement
S,K=input().split()
S=sorted(S)
print(*[''.join(res) for res in combinations_with_replacement(S,int(K))],sep='\n')