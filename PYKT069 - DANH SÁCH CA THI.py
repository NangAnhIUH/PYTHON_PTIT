L, A = [], []
with open("CATHI.in") as data:
    A.extend(data.read().split())

class CaThi:
    def __init__(self, ngay: str, gio: str, phong, ma: int):
        self.dd, self.mm, self.yy = map(int, ngay.split("/"))
        self.hh, self.min = map(int, gio.split(":"))
        self.phong = phong
        self.ma = ma

    def cmp(self)->tuple:
        return self.yy, self.mm, self.dd, self.hh, self.mm, self.ma

    def __str__(self):
        return f"C{self.ma:03d} {self.dd:02}/{self.mm:02}/{self.yy} {self.hh:02}:{self.min:02} {self.phong}"

for i in range(int(A[0])):
    idx = i * 3
    L.append(CaThi(A[idx + 1], A[idx + 2], A[idx + 3], i + 1))
L.sort(key=lambda x: x.cmp())
print(*L, sep="\n")