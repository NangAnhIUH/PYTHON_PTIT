a = dict()
test = 10
while test > 0:
    base = list(map(int, input().split()))
    test -= len(base)
    for x in base:
        temp = x % 42
        a[temp] = a.get(temp, 1)
print(len(a))
