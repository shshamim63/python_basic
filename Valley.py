import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    l=list()
    valley=0
    position=0
    for i in range(n):
        if (s[i]=='U'):
            position =position+1
            l.append(int(position))
        else:
            position =position-1
            l.append(int(position))
    for i in range(len(l)-1):
        if ((l[i]== -1) and (l[i+1]==0)):
            valley=valley+1
    return valley

n = int(input())

s = input()

result = countingValleys(n, s)

print(result)
