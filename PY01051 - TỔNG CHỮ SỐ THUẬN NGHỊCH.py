def isOk(number):
    sum = 0
    for digit in number:
        sum += int(digit)
    return len(str(sum)) > 1 and str(sum) == str(sum)[::-1]

for _ in range(int(input())):
    print("YES" if isOk(input()) else "NO")