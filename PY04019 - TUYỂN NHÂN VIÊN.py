class NhanVien:
    def __init__(self, ten, lythuyet, thuchanh, id):
        self.ma = "TS0"+str(id)
        self.ten = ten
        if lythuyet > 10:
            lythuyet /= 10
        if thuchanh > 10:
            thuchanh /= 10
        self.lyThuyet = lythuyet
        self.thucHanh = thuchanh
        self.trungBinh = (lythuyet + thuchanh) / 2
        self.xepLoai = self.danhGia()

    def __str__(self):
        return f"{self.ma} {self.ten} {self.trungBinh:.2f} {self.xepLoai}"

    def danhGia(self):
        tmp = self.trungBinh
        if tmp < 5:
            return "TRUOT"
        elif tmp < 8:
            return "CAN NHAC"
        elif tmp < 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

L = []
for i in range(int(input())):
    ten = input()
    thuchanh = float(input())
    lythuyet = float(input())
    L.append(NhanVien(ten,thuchanh, lythuyet, i+1))
L.sort(key=lambda x: -x.trungBinh)
for nhanvien in L:
    print(nhanvien)