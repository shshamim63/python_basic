import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    print(s)