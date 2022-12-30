for i in range(int(input())):
    s = input().split()
    tmp = 0
    for i in s:
        if tmp + len(i) <= 100:
            tmp += len(i) + 1
            print(i, end=" ")
        else:
            break
    print()