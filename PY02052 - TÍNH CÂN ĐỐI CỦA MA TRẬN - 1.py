n, A, top, bot = int(input()), [], 0, 0

for i in range(n):
    A.append(list(map(int, input().split())))

k = int(input())

for i in range(n):
    for j in range(i+1, n):
        top += A[i][j]
    for q in range(i):
        bot += A[i][q]

res = abs(top - bot)
print("YES" if res <= k else "NO")
print(res)