def isPrime(num: int):
    if num < 2:
        return False
    if num < 4:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

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
    if isPrime(after) and isPrime(befor):
        print(i)
        break
    i += 1
if i == len(D) - 1:
    print("NOT FOUND")