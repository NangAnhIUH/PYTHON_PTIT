MAX= int(1e6)
isPrime = [True] * (MAX + 1)
isPrime[0], isPrime[1] = [False] * 2
p = 2
while p * p <= MAX:
    if isPrime[p]:
        for i in range(p * p, MAX - 1, p):
            isPrime[i] = False
    p += 1

# Prime = []
# for i in range(2, MAX):
#     if isPrime[i]:
#         Prime.append(i)

for _ in range(int(input())):
    n = int(input())
    res = 0

    # idx = 0
    # while Prime[idx] < n - 6:
    #     num = Prime[idx]
    #     if isPrime[num + 6] and (isPrime[num + 2] or isPrime[num + 4]):
    #         res += 1
    #     idx += 1

    for i in range(2, n-6):
        if isPrime[i] and (isPrime[i+2] or isPrime[i+4]) and isPrime[i+6]:
            res += 1
    print(res)