n = int(input())
a = list(map(int, input().split()))
res = []

for i in a:
    if len(res) == 0:
        res.append(i)
    elif (res[-1] + i) % 2 == 0:
        res.pop()
    else:
        res.append(i)

print(len(res))