for i in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    print(a[-1] - a[0] - len(a) + 1)
'''
2
5
4 5 3 8 6
3
2 1 3
'''