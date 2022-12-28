n, k = map(int, input().split())
l = list(set(map(int, input().split())))
l.sort()
n = len(l)
a = []

def deQuy(idx):
    if len(a) == k:
        for i in a:
            print(i, end=' ')
        print()
    if idx == n:
        return
    for i in range(idx, len(l)):
        a.append(l[i])
        deQuy(i+1)
        a.pop()

deQuy(0)

# Solution 2
from itertools import *
for t in combinations(l, k):
    print(*t, sep=" ")