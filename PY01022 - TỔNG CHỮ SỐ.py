n, cnt = input(), 0

if n[0] == "-":
    n = sum(map(int, n[1:])) - 3
    cnt += 1
while len(str(n)) > 1:
    n = sum(map(int, str(n)))
    cnt += 1

print(cnt)