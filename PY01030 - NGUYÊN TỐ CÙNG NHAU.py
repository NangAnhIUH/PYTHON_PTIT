from math import gcd

N, K = map(int, input().split())
cnt = 0
for i in range(10 ** (K-1), 10 ** K):
    if gcd(N, i) == 1:
        print(i, end=" ")
        cnt += 1
        if cnt % 10 == 0:
            print()