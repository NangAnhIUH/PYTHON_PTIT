class ChuyenCan:
    def __init__(self, ma, ten, lop, diemdanh=""):
        self.ma = ma
        self.ten = ten
        self.lop = lop
        self.diem = 10
        self.ghiChu = ""

    def __str__(self):
        return f'{self.ma} {self.ten} {self.lop} {self.diem} {self.ghiChu}'

    def tinhDiem(self, diemdanh):
        diem = 10
        for c in diemdanh:
            if c == "v":
                diem -= 2
            elif c == "m":
                diem -= 1
        if diem <= 0:
            self.ghiChu = "KDDK"
            self.diem = 0
        else:
            self.diem = diem

L = dict()
t = int(input())
for i in range(t):
    ma = input()
    ten = input()
    lop = input()
    L[ma] = L.get(ten, ChuyenCan(ma, ten, lop))

for i in range(t):
    ma, diemdanh = input().split()
    L[ma].tinhDiem(diemdanh)
for i in L:
    print(L[i])