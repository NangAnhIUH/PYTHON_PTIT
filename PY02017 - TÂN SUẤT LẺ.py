for _ in range(int(input())):
    n = input()
    D = {}
    for i in map(int, input().split()):
        D[i] = D.get(i, 0) + 1
    for num, f in D.items():
        if f % 2:
            print(num)
            break
