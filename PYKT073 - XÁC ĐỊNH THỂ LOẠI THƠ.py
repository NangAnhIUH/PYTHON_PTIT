n = int(input())
res = ""
for i in range(n):
    if len(input().split()) in [6, 8]:
        res += "1"
    else:
        res += "2"
while '11' in res:
    res = res.replace('11', '1')
res = res.replace('2222', '2')
print(len(res))
print('\n'.join(res))