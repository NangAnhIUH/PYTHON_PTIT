from datetime import datetime
GIA = [25, 34, 50, 80]

class HoaDon:
    def __init__(self, ma, ten, phong, nhan, tra, phi):
        self.ma = ma
        self.ten = ten
        self.phong = phong
        self.ngayNhan = nhan
        self.ngayTra = tra
        self.phi = phi

        self.soNgay = str(datetime.strptime(self.ngayTra, '%d/%m/%Y') - datetime.strptime(self.ngayNhan, '%d/%m/%Y')).split()[0]
        if self.soNgay == '0:00:00':
            self.soNgay = 1
        else:
            self.soNgay = int(self.soNgay) + 1

        self.thanhTien = GIA[int(self.phong[0])-1] * self.soNgay + self.phi

    def __str__(self):
        return f"KH{self.ma:02d} {self.ten} {self.phong} {self.soNgay} {self.thanhTien}"

L = []
for i in range(0, int(input())):
    ma = i + 1
    ten = input().strip()
    phong = input().strip()
    nhan = input().strip()
    tra = input().strip()
    dvu = int(input())
    L.append(HoaDon(ma, ten, phong, nhan, tra, dvu))

L.sort(key=lambda x: -x.thanhTien)
for i in L:
    print(i)

