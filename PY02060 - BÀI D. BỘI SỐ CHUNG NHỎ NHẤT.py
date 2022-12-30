from sys import stdin

N, mod = 10 ** 6, 10 ** 9 + 7
Prime = [True] * (N + 1)
Prime[0] = Prime[1] = False
p = 2
while p * p <= N:
    if Prime[p]:
        for i in range(p * p, N + 1, p):
            Prime[i] = False
    p += 1


def pw(x, y):
    res = 1
    while y != 0:
        if y % 2:
            res = (res * x) % mod
        y //= 2
        x = (x * x) % mod
    return res


def mu(x, n):
    dem, i = 0, x
    while i <= n:
        dem += n // i
        i *= x
    return dem


for i in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    ans = 1
    dem = 0
    for i in range(2, b // 2 + 1):
        if Prime[i]:
            ans = (ans * ((mu(i, b) - mu(i, a - 1)) * 2 + 1)) % mod
    for i in range(b // 2 + 1, b + 1):
        if Prime[i]:
            dem += 1
    ans = (ans * pw(3, dem)) % mod
    print(ans)