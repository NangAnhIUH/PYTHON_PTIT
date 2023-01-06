isPrime = [True] * 1000
isPrime[0] = isPrime[1] = False
p = 2
while p * p < 1000:
    if isPrime[p]:
        for i in range(p * p, 1000, p):
            isPrime[i] = False
    p += 1

A, res = [], 0
n, m = map(int, input().split())

for i in range(n):
    A.extend(list(map(int, input().split())))
for i in A:
    if isPrime[i] and i > res:
        res = i

if res:
    print(res)
    for i, n in enumerate(A):
        if n == res:
            print(f"Vi tri [{i // m}][{i % m}]")
else:
    print("NOT FOUND")