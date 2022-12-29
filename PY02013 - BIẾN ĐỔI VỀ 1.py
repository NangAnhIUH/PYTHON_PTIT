def res(n: int):
    cnt = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        cnt += 1
    return cnt

while True:
    n = int(input())
    if n == 0:
        break
    print(res(n))