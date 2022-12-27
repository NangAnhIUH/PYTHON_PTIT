def isOk(number: str):
    sum = 0
    for digit in number:
        sum += int(digit)
    return not sum % 3

for _ in range(int(input())):
    print("YES" if isOk(input()) else "NO")