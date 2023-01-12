def getScore(n: int):
    if 0 < n < 3:
        return 1
    elif 2 < n < 5:
        return 2.5
    elif n < 7:
        return 3
    elif n < 10:
        return 3.5
    elif n < 13:
        return 4
    elif n < 16:
        return 4.5
    elif n < 20:
        return 5
    elif n < 23:
        return 5.5
    elif n < 27:
        return 6
    elif n < 30:
        return 6.5
    elif n < 33:
        return 7
    elif n < 35:
        return 7.5
    elif n < 37:
        return 8
    elif n < 39:
        return 8.5
    elif n < 41:
        return 9

for _ in range(int(input())):
    n = input().split()
    res = (getScore(int(n[0])) + getScore(int(n[1])) + float(n[2]) + float(n[3])) / 4
    if res % 1 >= 0.75:
        res = int(res) + 1
    elif res % 1 >= 0.25:
        res = int(res) + 0.5
    else:
        res = int(res)
    print(f"{res:.1f}")