n = int(input())
A, C, L = [], [], []
while len(A) < n:
    A.extend(x for x in list(map(int, input().split())))
for i in A:
    if i % 2:
        L.append(i)
    else:
        C.append(i)
C.sort(reverse=True)
L.sort()
for i in A:
    print(L.pop() if i % 2 else C.pop(), end=" ")