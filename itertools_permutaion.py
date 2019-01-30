from itertools import permutations
S,K=input().split()
print(*[''.join(res) for res in permutations(sorted(S),int(K))],sep='\n')
