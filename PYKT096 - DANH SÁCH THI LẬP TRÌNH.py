class Competitor:
    def __init__(self, ten, team):
        self.ten = ten
        self.ma = len(L) + 1
        self.team = a[int(team[5])-1]

    def __str__(self):
        return f"C{self.ma:03d} {self.ten} {self.team}"

a = {}
for i in range(int(input())):
    ten_team = input()
    ten_truong = input()
    a[i] = f'{ten_team} {ten_truong}'

L = []
for i in range(int(input())):
    ten_thi_sinh = input()
    ma_team = input()
    L.append(Competitor(ten_thi_sinh, ma_team))

L.sort(key=lambda x: x.ten)
for i in L:
    print(i)