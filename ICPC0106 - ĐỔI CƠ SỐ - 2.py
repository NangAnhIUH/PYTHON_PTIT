import math
c = ["A", "B", "C", "D", "E", "F"]
for _ in range(int(input())):
    n = int(input())
    s = input()
    b = int(math.log(n, 2))
    if n == 2:
        print(s)
        continue
    while len(s) % b != 0:
        s = "0" + s
    i = 0
    while i < len(s):
        temp = 0
        for j in range(i, i+b):
            temp += int(s[j]) * (2 ** (b - j + i - 1))
        if temp < 10:
            print(temp, end="")
        else:
            print(c[temp-10], end="")
        i += b
    print()