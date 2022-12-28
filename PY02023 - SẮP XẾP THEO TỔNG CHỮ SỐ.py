def solve(n: int):
    tong = 0
    while n > 0:
        tong += n % 10
        n //= 10
    return tong

for i in range(int(input())):
    n, a = input(),list(map(int, input().split()))
    a.sort(key=lambda x: (solve(x), x))
    print(*a, sep=" ")