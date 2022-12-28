p = ('2', '3', '5', '7')

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

def isOk(number: str):
    return isPrime(len(number)) and 2 * sum([1 for x in number if x in p]) > len(number)

for _ in range(int(input())):
    print("YES" if isOk(input()) else "NO")
'''
3
1234567
22334455667
23400300489898989
'''