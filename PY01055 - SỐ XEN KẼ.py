def isOk(number: str):
    if number[0] == number[1]:
        return False
    if len(number) % 2 == 0:
        return False
    if len(set(digit for digit in number[::2])) !=  1:
        return False
    return True

for _ in range(int(input())):
    print("YES" if isOk(input()) else "NO")