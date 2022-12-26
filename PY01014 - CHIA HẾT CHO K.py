dList = list(map(int, input().split()))
b = []

a, K, N = dList

i = K - (a % K)

N -= a

while i <= N:
    b.append(i)
    i += K
if b:
    for x in b:
        print(x, end=" ")
else:
    print(-1)