while True:
    a = list(map(int, input().split()))

    if a == [0] * 4:
        break

    res = 0
    while len(set(a)) != 1:
        temp = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i+1])
        a[3] = abs(a[3] - temp)
        res += 1
    print(res)