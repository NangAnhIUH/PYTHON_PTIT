n = int(input())
A = list(map(int, input().split()))
step, num = sum(abs(ai - A[0]) for ai in A), A[0]

for i in range(n):
    if A[i] != num:
        tmp = sum(abs(ai - A[i]) for ai in A)
        if tmp < step:
            step = tmp
            num = A[i]

print(step, num)