from datetime import datetime

t = int(input())

for i in range(t):
    time_1 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    time_2 = datetime.strptime(input(), "%a %d %b %Y %X %z")
    result = abs(int((time_1 - time_2).total_seconds()))
    print(result)