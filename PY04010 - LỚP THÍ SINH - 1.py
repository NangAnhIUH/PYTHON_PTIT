class Student:
    def __init__(self, ten, ngaysinh, mon1, mon2, mon3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.mon1 = float(mon1)
        self.mon2 = float(mon2)
        self.mon3 = float(mon3)
        self.tong = self.mon1 + self.mon2 + self.mon3

    def __str__(self):
        return f'{self.ten} {self.ngaysinh} {self.tong}'

ten, ngaysinh, mon1, mon2, mon3 = input(), input(), input(), input(), input()
print(Student(ten, ngaysinh, mon1, mon2, mon3))