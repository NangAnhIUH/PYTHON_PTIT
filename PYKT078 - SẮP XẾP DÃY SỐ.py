for _ in range(int(input())):
    n, m = map(int, input().split())
    a, b, A = [], [], list(map(int, input().split()))
    for x in A:
        if x < 0:
            a.append(x)
        else:
            b.append(x)
    A = a + b
    A.insert(A.index(max(A)), m)
    print(*A, sep=" ")
