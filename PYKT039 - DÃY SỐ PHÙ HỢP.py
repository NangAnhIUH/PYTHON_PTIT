for _ in range(int(input())):
    n = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    flag = True
    for i in range(n):
        if A[i] > B[i]:
            flag = False
    print("YES" if flag else "NO")