for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    low, low[0] = [0] * n, L[0]
    high, high[-1]= [int(1e9)] * n, L[-1]
    for i in range(1, n):
        low[i] = max(L[i], low[i - 1])
    for i in range(n - 2, -1, -1):
        high[i] = min(L[i], high[i + 1])
    dem = 0
    for i in range(1, n-1):
        if low[i - 1] <= L[i] < high[i + 1]:
            dem += 1
    if L[0] < high[1]:
        dem += 1
    if L[-1] >= low[n-2]:
        dem += 1
    print(dem)