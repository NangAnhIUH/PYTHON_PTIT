N, M = map(int, input().split())
L = [0] * (M + 1)

for vote in map(int, input().split()):
    L[vote] += 1
maxx = max(L)

for i in range(1, M+1):
    if L[i] == maxx:
        L[i] = 0
res = max(L)
print(L.index(res) if res else "NONE")