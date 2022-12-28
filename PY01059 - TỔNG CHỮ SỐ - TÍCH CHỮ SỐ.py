def Tong(number: str):
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum

def Tich(number: str):
    s = set()
    tich = 1
    for digit in number:
        s.add(digit)
        tmp = int(digit)
        if tmp:
            tich *= tmp
    if s == {'0'}:
        return 0
    return tich

for _ in range(int(input())):
    n = input()
    print(Tong(n[::2]), Tich(n[1::2]))
'''
3
12345678
20000
22334455667788
'''
