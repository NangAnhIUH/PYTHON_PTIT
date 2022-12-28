def dis(n:str):
    for i in range(1, len(n)):
        if abs(int(n[i-1]) - int(n[i])) != 2:
            return False
    return True
for _ in range(int(input())):
    n = input()
    print("YES" if sum(int(x) for x in n) % 10 == 0 and dis(n) else "NO")