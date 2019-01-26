import numpy
N,M=map(int,input().split())
my_array=numpy.array([list(map(int,input().split())) for i in range(N)]) 
print(numpy.transpose(my_array))
print(my_array.flatten())