A = []
n, m = map(int, input().split())

for i in range(n):
    A.extend(list(map(int, input().split())))

res = 0
for i in A:
    if i > 9 and str(i) == str(i)[::-1] and i > res:
        res = i

if res:
    print(res)
    for i, n in enumerate(A):
        if n == res:
            print(f"Vi tri [{i // m}][{i % m}]")
else:
    print("NOT FOUND")