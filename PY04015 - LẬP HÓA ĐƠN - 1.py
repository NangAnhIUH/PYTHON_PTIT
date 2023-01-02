L = []

class KhachHang:
    def __init__(self, ten, old, new):
        self.ma = len(L) + 1
        self.ten = ten
        self.old = old
        self.new = new
        self.tongTien = self.tinhTongTien()

    def __str__(self):
        return f"KH{self.ma:02} {self.ten} {int(self.tongTien)}"

    def tinhTongTien(self):
        tieudung = self.new - self.old
        if tieudung <= 50:
            return round(tieudung * 100 * 1.02)
        elif tieudung <= 100:
            return round((50 * 100 + (tieudung - 50) * 150) * 1.03)
        else:
            return round((50 * 250 + (tieudung - 100) * 200) * 1.05)

for _ in range(int(input())):
    ten = input()
    cu = int(input())
    moi = int(input())
    L.append(KhachHang(ten, cu, moi))

L.sort(key=lambda x: -x.tongTien)
for kh in L:
    print(kh)