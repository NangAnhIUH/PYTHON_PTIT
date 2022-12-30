class contact:
    def __init__(self, date, hoVaTen, soDienThoai):
        dd, mm, yy = map(int, date.split("/"))
        self.dd = dd
        self.mm = mm
        self.yy = yy
        self.hoVaTen = hoVaTen
        l = hoVaTen.split()
        self.ten = l[-1]
        self.hoDem = ""
        for i in range(len(l) - 1):
            self.hoDem += l[i] + " "
        self.soDienThoai = soDienThoai

    def toString(self):
        return f"{self.hoVaTen}: {self.soDienThoai} {self.dd}/{self.mm}/{self.yy}"

l = []

def repairString(s):
    s = s.replace("\n", "")
    s = s.replace("Ngay ", "")
    return s

with open("SOTAY.txt", "r") as sotay:
    with open("DIENTHOAI.txt", "w") as danhba:
        d = [repairString(x) for x in sotay.readlines() if len(x) != 0]
        idx = 0
        while idx < len(d):
            if "/" in d[idx]:
                date = d[idx]
                idx += 1
            else:
                l.append(contact(date, d[idx], d[idx+1]))
                idx += 2
        l.sort(key=lambda x: (x.ten, x.hoDem))
        for contact in l:
            danhba.write(contact.toString()+"\n")