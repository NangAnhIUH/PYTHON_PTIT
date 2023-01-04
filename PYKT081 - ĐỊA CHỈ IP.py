for _ in range(int(input())):
    s = input().split(".")
    for c in s:
        if not c.isdigit():
            print("NO")
            break
    else:
        a = list(map(int, s))
        if len(a) != 4 or any(x < 0 or x > 255 for x in a):
            print("NO")
        else:
            print("YES")