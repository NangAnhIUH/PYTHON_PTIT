Panlin = [0]

def Cal(s):
    sum, so = 0, 1
    s = s[::-1]
    for i in s:
        if i == '1':
            sum = sum + so
        so = so * 2
    return sum

def Pre(s):
    if len(s) > 21:
        return
    if s and s[0] != '0':
        Panlin.append(Cal(s))
    Pre('0' + s + '0')
    Pre('1' + s + '1')

def binSearch(l, r, x):
    while l <= r:
        mid = (l+r)//2
        if Panlin[mid] == x:
            return mid
        if Panlin[mid] < x:
            l = mid+1
        else:
            r = mid - 1
            res = mid
    return res

l, r, n = map(int, input().split())
res = 0
if n == 3:
    if l == 0:
        res += 1
    if l <= 1 <= r:
        res += 1
    if l <= 6643 <= r:
        res += 1
    if l <= 1422773 <= r:
        res += 1
    print(res)
elif n > 3:
    if l == 0:
        res += 1
    if l <= 1 <= r:
        res += 1
    print(res)
elif n == 2:
    Pre('')
    Pre('1')
    Pre('0')
    Panlin.sort()
    it1 = binSearch(0, len(Panlin) - 1, l)
    it2 = binSearch(0, len(Panlin) - 1, r)
    if Panlin[it2] != r:
        it2 -= 1
    print(it2 - it1 + 1)