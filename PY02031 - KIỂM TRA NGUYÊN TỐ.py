n = 1000
isPrime = [True] * (n+1)
isPrime[0] = isPrime[1] = False
i = 2
while i * i <= n:
    if isPrime[i]:
        for j in range(i * i, n+1, i):
            isPrime[j] = False
    i += 1
n, m = map(int, input().split())
for _ in range(n):
    row = list(map(int, input().split()))
    for ai in row:
        print("1" if isPrime[ai] else "0" , end=" ")
    print()