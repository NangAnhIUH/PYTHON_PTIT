def isOk(n: int, a: list, b: list):
    a.sort()
    b.sort()
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

for _ in range(int(input())):
    print("YES" if isOk(int(input()),
                        list( map(int, input().split())),
                        list(map(int, input().split())))
          else "NO")