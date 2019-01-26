from collections import Counter

x = sorted(input())

c = Counter(x).most_common(3)

for k,v in c:
    print(k,v) 