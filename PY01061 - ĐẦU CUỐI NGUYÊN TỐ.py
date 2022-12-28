def isPrime(num: int):
    if num < 2:
        return False
    if num <4:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

for i in range(int(input())):
    n = input()
    print("YES" if isPrime(int(n[:3])) and isPrime(int(n[-3:])) else "NO")
'''

'''