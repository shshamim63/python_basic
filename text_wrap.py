import math
string=input()
num_substring=int(input())
for i in range(int(math.ceil(len(string)/num_substring))):
    if (((i*num_substring)+num_substring) >= len(string)):
        print(string[(i*num_substring):])
        break
    else:
        print(string[(i*num_substring):(i*num_substring)+num_substring])