def isPrime(n: int):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 and n % (i + 2) == 0:
            return False
        i += 6
    return True

def isOK(number: str):
    sum = 0
    for digit in number:
        sum += int(digit)
    return isPrime(sum)

for _ in range(int(input())):
    print("YES" if isOK(input()) else "NO")