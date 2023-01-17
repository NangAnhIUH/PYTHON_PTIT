from math import comb

def countC(A: list):
    for a in A:
        cnt = a.count("C")
        D[cnt] = D.get(cnt, 0) + 1

n = int(input())
A = list(input() for i in range(n))
AT, D, res = [], {}, 0
for i in range(n):
    temp = ''
    for a in A:
        temp += a[i]
    AT.append(temp)

countC(A)
countC(AT)

for key, value in D.items():
    res += value * comb(key, 2)
print(res)