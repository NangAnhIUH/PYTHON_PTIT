from math import gcd
class Fraction:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        GCD = gcd(self.tu, self.mau)
        self.tu //= GCD
        self.mau //= GCD
        return self

    def congPhanSo(self, B):
        self = self.rutGon()
        B = B.rutGon()
        mau = self.mau * B.mau // gcd(self.mau, B.mau)
        tu_a = self.tu * (mau // self.mau)
        tu_b = B.tu * (mau // B.mau)
        tong = tu_a + tu_b
        return Fraction(tong, mau).rutGon()

a, b, c, d = map(int, input().split())
A = Fraction(a, b)
B = Fraction(c, d)
C = A.congPhanSo(B)
print(C.tu, '/', C.mau, sep="")