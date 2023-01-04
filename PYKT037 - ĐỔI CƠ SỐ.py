BASE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
    num_10, base = map(int, input().split())
    res = []
    while num_10 != 0:
        remainder = num_10 % base
        res.append(BASE[remainder])
        num_10 //= base
    print(*res[::-1], sep="")