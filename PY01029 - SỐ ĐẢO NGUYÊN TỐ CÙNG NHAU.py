from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = int(str(n)[::-1])
    print("YES" if gcd(n, a) == 1 else "NO")