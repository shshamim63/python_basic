import numpy
def Create_list(n,m):
    listoflists = []
    a_list = []
    for i in range(0,n):
        for j in range(0,m):
            a_list.append(int(input()))
        listoflists.append(list(a_list))
        a_list.clear()
    return listoflists

N, M = map(int, input().split())
A = numpy.array(Create_list(N,M))
B = numpy.array(Create_list(N,M))

print (A + B)
print (A - B)
print (A * B)
print (A // B)
print (A % B)
print (A ** B)