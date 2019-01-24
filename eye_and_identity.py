import numpy
N, M = map(int, input().split())
Ans=str(numpy.eye(N,M,k=0)).replace("0", " 0").replace("1"," 1")
print(Ans)