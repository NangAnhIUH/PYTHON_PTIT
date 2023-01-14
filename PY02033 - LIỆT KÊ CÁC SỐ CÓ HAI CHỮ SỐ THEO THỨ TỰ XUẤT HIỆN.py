D, s = {}, input()
for i in range(0, len(s)-1, 2):
    n = s[i:i+2]
    D[n] = D.get(n, 0) + 1
for i in D:
    print(i, end=" ")