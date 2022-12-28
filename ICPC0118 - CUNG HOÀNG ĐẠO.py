for _ in range(int(input())):
    d, m = map(int, input().split())
    if m == 1:
        print("Ma Ket" if d < 20 else "Bao Binh")
    elif m == 2:
        print("Bao Binh" if d < 19 else "Song Ngu")
    elif m == 3:
        print("Song Ngu" if d < 21 else "Bach Duong")
    elif m == 4:
        print("Bach Duong" if d < 20 else "Kim Nguu")
    elif m == 5:
        print("Kim Nguu" if d < 21 else "Song Tu")
    elif m == 6:
        print("Song Tu" if d < 21 else "Cu Giai")
    elif m == 7:
        print("Cu Giai" if d < 23 else "Su Tu")
    elif m == 8:
        print("Su Tu" if d < 23  else "Xu Nu")
    elif m == 9:
        print("Xu Nu" if d < 23 else "Thien Binh")
    elif m == 10:
        print("Thien Binh" if d < 23 else "Thien Yet")
    elif m == 11:
        print("Thien Yet" if d < 23 else "Nhan Ma")
    elif m == 12:
        print("Nhan Ma" if d < 22 else "Ma Ket")