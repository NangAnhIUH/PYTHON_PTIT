while True:
    n = int(input())
    if n == 0:
        break
    A = []
    for i in range(n):
        A.append(int(input()))
    maxx, minn = max(A), min(A)
    print("BANG NHAU" if maxx == minn else f"{minn} {maxx}")
