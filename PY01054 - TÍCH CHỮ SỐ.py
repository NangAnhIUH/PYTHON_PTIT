def Tich(number: str):
    res = 1
    for digit in number:
        res *= int(digit) if int(digit) != 0 else 1
    return res

for _ in range(int(input())):
    print(Tich((input())))