from collections import namedtuple
n = int(input())
a = input()
Student=namedtuple('Student',a)
sum=0
for _ in range(n):
    student=Student(*input().split())
    sum+=int(student.MARKS)
print('{:0.2f}'.format(sum/n))