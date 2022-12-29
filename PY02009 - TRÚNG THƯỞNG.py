for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        x = int(input())
        d[x] = d.get(x, 0) + 1
    res = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    print(res[0][0])