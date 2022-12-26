n = int(input())
a, top, bot = [], 0, 0

for _ in range(n):
    a.append(list(map(int, input().split())))
    for i in range(n-_-1):
        top += a[_][i]
    for j in range(n-_, n):
        bot += a[_][j]

k = int(input())

val = top - bot
print("YES" if -k <= val <= k else "NO")
print(val if val > 0 else -val)

'''
5
2 8 10 6 7
6 3 2 6 9
10 2 6 2 8
9 9 7 9 8
9 6 5 6 9
5
'''