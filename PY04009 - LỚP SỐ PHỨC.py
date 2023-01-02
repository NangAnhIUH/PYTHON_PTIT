class Complex:
    def __init__(self, a, bi):
        self.a = a
        self.bi = bi

    def cong(self, z2):
        a = self.a + z2.a
        bi = self.bi + z2.bi
        return Complex(a, bi)

    def nhan(self, z2):
        a = self.a * z2.a - self.bi * z2.bi
        bi = self.a * z2.bi + self.bi * z2.a
        return Complex(a, bi)

    def __str__(self):
        if self.bi >= 0:
            return f"{self.a} + {abs(self.bi)}i"
        else:
            return f"{self.a} - {abs(self.bi)}i"

for _ in range(int(input())):
    a, bi, c, di = map(int, input().split())
    A = Complex(a, bi)
    B = Complex(c, di)
    C = A.cong(B).nhan(A)
    D = A.cong(B).nhan(A.cong(B))
    print(C, D, sep=', ')