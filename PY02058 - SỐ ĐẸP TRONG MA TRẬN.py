n, m = map(int, input().split())
A, res = [], ''
for i in range(n):
    A.extend(list(map(int, input().split())))
num = max(A) - min(A)
for i in range(len(A)):
    if A[i] == num:
        res += f'Vi tri [{i // m}][{i % m}]\n'
if res:
    print(num)
    print(res)
else:
    print("NOT FOUND")