ds_Tram, CNT = {}, 0

class Tram:
    def __init__(self, ten, thoigian, luongmua):
        global CNT
        if ten == "Khoi tao":
            CNT += 1
        self.ten = ten
        self.ma = CNT
        self.thoigian = thoigian
        self.luongmua = luongmua
        self.trungBinh = 0

    def them(self, ten, giay, mm):
        self.ten = ten
        self.thoigian += giay
        self.luongmua += mm

    def tinhTrungBinh(self):
        self.trungBinh = self.luongmua / self.thoigian * 60

    def __str__(self):
        self.tinhTrungBinh()
        return f"T{self.ma:02} {self.ten} {self.trungBinh:.2f}"

def to_minute(hh_mm):
    hh, mm = map(int, hh_mm.split(":"))
    return hh * 60 + mm

def count_minut(time1, time2):
    start = to_minute(time1)
    end = to_minute(time2)
    return end - start

for _ in range(int(input())):
    ten, batdau, ketthuc = input(),  input(), input()
    thoigian = count_minut(batdau, ketthuc)
    luongmua = int(input())
    ds_Tram[ten] = ds_Tram.get(ten, Tram("Khoi tao", 0, 0))
    ds_Tram[ten].them(ten, thoigian, luongmua)

for ten_tram in ds_Tram:
    print(ds_Tram[ten_tram])