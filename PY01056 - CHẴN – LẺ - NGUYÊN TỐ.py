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

def isOK(num: str):

    chan = set(int(x) for x in num[0::2])
    for c in chan:
        if c % 2 == 1:
            return False

    le = set(int(x) for x in num[1::2])
    for l in le:
        if l % 2 == 0:
            return False

    tong = sum([int(x) for x in num])
    return isPrime(tong)

for _ in range(int(input())):
    print("YES" if isOK(input()) else "NO")
