for _ in range(int(input())):
    N, d = map(int, input().split())
    a = list(map(int, input().split()))
    for ai in a[d:]+a[:d]:
        print(ai, end=" ")
    print()
