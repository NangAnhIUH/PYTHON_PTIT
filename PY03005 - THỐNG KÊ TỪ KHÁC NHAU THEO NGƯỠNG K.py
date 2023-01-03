D = {}
t, k = map(int, input().split())
for _ in range(t):
    s = input()
    w = ""
    for c in s.lower() + " ":
        if c.isalnum():
            w += c
        else:
            if w != "":
                D[w] = D.get(w, 0) + 1
            w = ""

m = sorted(D.items(), key=lambda x: (-x[1], x[0]))
for i in m:
    if i[1] < k:
        break
    print(i[0], i[1])