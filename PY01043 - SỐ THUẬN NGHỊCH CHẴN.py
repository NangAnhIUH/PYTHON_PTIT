a = []


def check(n):
    for i in n:
        if int(i) % 2 == 1:
            return False
    return True

i = 2
while i <= 888:
    if check(str(i)):
        temp = str(i)
        a.append(int(temp + temp[::-1]))
    i += 2

for _ in range(int(input())):
    n = int(input())
    for i in a:
        if i >= n:
            break
        print(i, end=" ")
    print()