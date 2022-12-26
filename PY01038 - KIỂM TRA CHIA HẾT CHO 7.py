def solve(n):
    loop = 1
    while loop != 1000:
        if not n % 7:
            return n
        else:
            n += int(str(n)[::-1])
        loop += 1
    return -1


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
