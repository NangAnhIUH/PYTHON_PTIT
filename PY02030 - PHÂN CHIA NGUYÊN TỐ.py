MAX = int(1e6)
isPrime = [True] * MAX
isPrime[0] = isPrime[1] = False
p = 2
while p * p < MAX:
    if isPrime[p]:
        for i in range(p * p, MAX, p):
            isPrime[i] = False
    p += 1

n = input()
D = {}
for x in map(int, input().split()):
    D[x] = D.get(x)
befor, after = 0, sum(D)
A = list(D)
i = 0
while i < len(D) - 1:
    befor += A[i]
    after -= A[i]
    if isPrime[after] and isPrime[befor]:
        print(i)
        break
    i += 1
if i == len(D) - 1:
    print("NOT FOUND")