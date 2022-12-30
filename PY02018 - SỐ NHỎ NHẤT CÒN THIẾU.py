n = int(input())
a = list(map(int, input().split()))

a.sort()

res = 1
for x in a:
    if x > res:
        break
    elif x == res:
        res += 1
print(res)