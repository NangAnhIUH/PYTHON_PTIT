for _ in range(int(input())):
    n, m = map(int, input().split())
    A, A_T = [], []

    for i in range(n):
        A.append(list(map(int, input().split())))

    for j in range(m):
        row = []
        for a in A:
            row.append(a[j])
        A_T.append(row)

    for i in range(n):
        for j in range(n):
            s = 0
            for z in range(m):
                s += A[i][z] * A_T[z][j]
            print(s, end=" ")
        print()