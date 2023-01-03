D = {}

for _ in range(int(input())):
    ma = input()
    ten = input()
    hinhthuc = input()
    D[ma] = f"{ten} {hinhthuc}"

id_list = sorted(D.keys())
for ma in id_list:
    print(ma, D[ma])