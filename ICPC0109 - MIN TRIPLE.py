big = int(1e9)
for _ in range(int(input())):
    n = input()
    s = input()
    x, y, z = big, big, big
    n = len(s)//3
    while s[n] != " ": n -= 1
    a = s[:n]
    s = s[n:]
    for i in map(int, a.split()):
        if i >= z: continue
        elif i <= x: x, y, z = i, x, y
        elif i <= y: y, z = i, y
        else: z = i
    n = len(s) // 2
    while s[n] != " ": n -= 1
    for i in map(int, s[:n].split()):
        if i >= z: continue
        elif i <= x: x,y,z = i, x, y
        elif i <= y: y, z = i, y
        else: z = i
    for i in map(int, s[n:].split()):
        if i >= z: continue
        elif i <= x: x,y,z = i, x, y
        elif i <= y: y, z = i, y
        else: z = i
    print(x+y+z)