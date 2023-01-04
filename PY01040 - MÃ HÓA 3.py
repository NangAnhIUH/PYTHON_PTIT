BASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getValue(c: str):
    return ord(c) - ord("A")

def cypher(c: str, n: int):
    i = (getValue(c) + n) % 26
    return BASE[i]

def rotate(s: str):
    res = ""
    n = sum(getValue(c) for c in s)
    for c in s:
        res += cypher(c, n)
    return res

def merge(s1: str, s2: str):
    res = ""
    for i in range(len(s1)):
        res += cypher(s1[i], getValue(s2[i]))
    return res

for _ in range(int(input())):
    s = input()
    devide = len(s) // 2
    s1, s2 = s[:devide], s[devide:]
    s1, s2 = rotate(s1), rotate(s2)
    print(merge(s1, s2))