for _ in range(int(input())):
    n = int(input())
    d = dict()

    for i in map(int, input().split()):
        d[i] = d.get(i, 0) + 1

    flag = 0
    for i in d:
        if d[i] > (n // 2):
           print(i)
           flag = 1
           break
            
    if flag == 0:
        print("NO")