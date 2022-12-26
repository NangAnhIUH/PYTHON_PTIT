def isPrime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i +  2) == 0:
            return False
        i += 6
    return True
for _ in range(int(input())):
    n = input()
    count = 0
    for c in n:
        if c in "2357":
            count += 1
    print("YES"  if isPrime(len(n)) and 2 * count > len(n) else "NO")