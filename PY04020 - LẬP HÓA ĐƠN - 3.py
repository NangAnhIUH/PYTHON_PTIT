class DonHang:
    def __init__(self, ma, ten, soluong, dongia, chietkhau):
        self.ma = ma
        self.ten = ten
        self.soLuong = soluong
        self.donGia = dongia
        self.chietKhau = chietkhau
        self.tong = self.soLuong * self.donGia - self.chietKhau

    def __str__(self):
        return f'{self.ma} {self.ten} {self.soLuong} {self.donGia} {self.chietKhau} {self.tong}'

L = []
for i in range(int(input())):
    ma = input()
    ten = input()
    soluong = int(input())
    dongia = int(input())
    chietkhau = int(input())
    L.append(DonHang(ma, ten, soluong, dongia, chietkhau))

L.sort(key=lambda x: -x.tong)
for hang in L:
    print(hang)