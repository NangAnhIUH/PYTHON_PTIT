N, X = map(int, input().split())
MAX = int(8e3)
isPrime = [True] * (MAX + 1)
isPrime[0] = isPrime[1] = False
p = 2

while p * p < MAX:
    if isPrime[p]:
        for i in range(p*p, MAX + 1, p):
            isPrime[i] = False
    p += 1
prime = [x for x in range(MAX) if isPrime[x]]

print(X, end=" ")
for i in range(N):
    print(X+prime[i], end=" ")
    X += prime[i]