D = {}

for _ in range(int(input())):
    s = input()
    w = ""
    for c in s.lower() + " ":
        if c.isalpha():
            w += c
        else:
            if w != "":
                D[w] = D.get(w, 0) + 1
            w = ""

m = sorted(D.items(), key=lambda x: (-x[1], x[0]))
for i in m:
    print(i[0], i[1])