n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
n_remove = abs(n - m)
if n > m:
    for i in range(n):
        if n_remove != 0 and i % 2 == 0:
            n_remove -= 1
            continue
        else:
            print(*A[i])
else:
    for a in A:
        cnt = 0
        for i in range(m):
            if cnt != n_remove and i % 2:
                cnt += 1
                continue
            print(a[i], end=" ")
        print()