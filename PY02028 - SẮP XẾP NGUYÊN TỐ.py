isPrime = [True] * 1000
isPrime[0] = isPrime[1] = False
p = 2
while p * p < 1000:
    if isPrime[p]:
        for i in range(p * p, 1000, p):
            isPrime[i] = False
    p += 1

n = input()
A, P = [], []

for x in map(int, input().split()):
    A.append(x)
    if isPrime[x]:
        P.append(x)

P.sort(reverse= True)
for i in A:
    print(P.pop() if isPrime[i] else i, end=" ")