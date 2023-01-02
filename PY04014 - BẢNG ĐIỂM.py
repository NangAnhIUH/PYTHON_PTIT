L = []

class SinhVien:
    def __init__(self, ten, diem):
        self.ma = len(L) + 1
        self.ten = ten
        self.diem = diem
        self.trungBinh = self.tinhTrungBinh()
        self.xepHang = self.Rank()

    def tinhTrungBinh(self):
        tong = 0
        for i in range(10):
            if i <= 1:
                tong += self.diem[i] * 2
            else:
                tong += self.diem[i]
        return round(tong / 10 / 1.2, 1)

    def Rank(self):
        tmp = self.trungBinh
        if tmp >= 9:
            return "XUAT SAC"
        elif tmp >= 8:
            return "GIOI"
        elif tmp >= 7:
            return "KHA"
        elif tmp >= 5:
            return "TB"
        return "YEU"

    def __str__(self):
        return f"HS{self.ma:02d} {self.ten} {self.trungBinh:.1f} {self.xepHang}"

for i in range(int(input())):
    ten = input()
    diem = [float(x) for x in input().split()]
    L.append(SinhVien(ten, diem))

L.sort(key=lambda x: -x.trungBinh)
for student in L:
    print(student)