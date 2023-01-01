ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for _ in range(int(input())):
    d, cnt, s = {}, 0, input()
    for c in s:
        if c.isalpha():
            d[c] = d.get(c, 0) + 1
        else:
            cnt += int(c)
    for a in ALPHA:
        print(a*d.get(a, 0), end="")
    print(cnt)