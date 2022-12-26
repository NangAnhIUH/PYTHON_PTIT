def solve(n):
    if len(n) < 3:
        return False
    i = 0
    while n[i] < n[i+1]:
        i += 1
    while i < len(n) - 1:
        if n[i] <= n[i+1]:
            return False
        i += 1
    return True

for i in range(int(input())):
    print("YES" if solve(input()) else "NO")