MAX = int(1e6)
isPrime = [True] * (MAX + 1)
isPrime[0] = isPrime[1] = False
p = 2
while p * p <= MAX:
    if isPrime[p]:
        for i in range(p * p, MAX + 1, p):
            isPrime[i] = False
    p += 1


prime = [x for x in range(2, MAX + 1) if isPrime[x] == True]


def solve(n):
    d = dict()

    idx = 0
    while prime[idx] <= n:
        num = prime[idx]
        if n % num == 0:
            d[num] = d.get(num, 0) + 1
            n //= num
        else:
            idx += 1

    print(1, end="")
    for key, value in d.items():
        print(" * ", key, "^", value, sep="", end=" ")
    print()


for _ in range(int(input())):
   solve(int(input()))