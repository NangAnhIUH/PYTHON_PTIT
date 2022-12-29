n = int(input())
a = []
b = list(map(int, input().split()))

def di(k):
    l = 0
    r = len(a)-1
    while l <= r:
        mid = (l + r) // 2
        if k >= a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    a.insert(l, k)
    return l

dem = 0
for i in b:
    dem += di(i)
print(dem)

