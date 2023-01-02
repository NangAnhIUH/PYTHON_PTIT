def to_min(hh_mm: str):
    hh, mm = map(int, hh_mm.split(":"))
    return hh*60 + mm

def count_min(start, end):
    return abs(to_min(end) - to_min(start))

class Gamer:
    def __init__(self, ma, ten, giovao, giora):
        self.ma = ma
        self.ten = ten
        self.thoigian = count_min(giovao, giora)
        self.gio = self.thoigian // 60
        self.phut = self.thoigian % 60
    def __str__(self):
        return f"{self.ma} {self.ten} {self.gio} gio {self.phut} phut"

L = []
for _ in range(int(input())):
    ma = input()
    ten = input()
    giovao = input()
    giora = input()
    L.append(Gamer(ma, ten, giovao, giora))

L.sort(key=lambda x: -x.thoigian)
for gamer in L:
    print(gamer)