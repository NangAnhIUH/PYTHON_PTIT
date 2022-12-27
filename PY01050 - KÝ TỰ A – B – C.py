def isOK(s, l, a, b, c)->str:
    if len(s) == l:
        if a <= b and b <= c and a > 0:
            print(s)
        return
    if len(s) < l:
        isOK(s + "A", l, a+1, b, c)
        isOK(s + "B", l, a, b+1, c)
        isOK(s + "C", l, a, b, c+1)

n = int(input())
for i in range(3, n+1):
    isOK("", i, 0, 0, 0)