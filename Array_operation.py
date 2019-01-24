import numpy
def Create_list(n,m):
    listoflists = []
    a_list = []
    for i in range(0,10):
        a_list.append(i)
        if len(a_list)>3:
            a_list.remove(a_list[0])
            listoflists.append(list(a_list), a_list[0])
    return listoflists

N, M = map(int, input().split())

A = (Create_list(N,M))
print(A)
#B = numpy.array(Create_list(N,M))
