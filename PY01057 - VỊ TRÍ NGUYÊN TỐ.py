def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def check(n):
    for i in range(len(n)):
        temp = int(n[i])
        if isPrime(i) and not isPrime(temp):
            return False
        if isPrime(temp) and not isPrime(i):
            return False
    return True

for _ in range(int(input())):
    print("YES" if check(input()) else "NO")