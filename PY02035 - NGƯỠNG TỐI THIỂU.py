s, k = input(), int(input())
D, L = {}, []
for i in range(0, len(s) - 1, 2):
    val = s[i:i+2]
    D[val] = D.get(val, 0) + 1
for key, val in D.items():
    if val >= k:
        L.append((key,val))
if L:
    L.sort()
    for i in L:
        print(*i)
else:
    print("NOT FOUND")