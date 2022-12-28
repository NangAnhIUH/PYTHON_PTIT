import sys
import array as arr
# dung arr va sys de giam Memory va tang inputTime

MAX = int(2e6)+1
c = arr.array('i', [0]*MAX)
i = 2
while i * i < MAX:
    if c[i] == 0:
        c[i] = i
        for j in range(i * i, MAX, i):
            c[j] = i
    i += 1
for i in range(4, MAX):
    c[i] += c[i//c[i]] if c[i] else i

res = 0
for _ in range(int(sys.stdin.readline())):
    res += c[int(sys.stdin.readline())]
print(res)