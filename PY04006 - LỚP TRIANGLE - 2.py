import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        x0 = self.x  - point.x
        y0 = self.y - point.y
        return math.sqrt(x0 * x0 + y0 * y0)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def cnt(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if max(a, b, c) * 2 >= a + b + c:
            print("INVALID")
        else:
            p = (a + b + c)
            heron = math.sqrt(p * (p - 2 * c) * (p - 2 * a) * (p - 2 * b)) * 1 / 4
            print(f"{heron:.2f}")

l = []
i = 0
for _ in range(int(input())):
    l += list(map(float, input().split()))
    A = Point(l[i], l[i + 1])
    B = Point(l[i + 2], l[i + 3])
    C = Point(l[i + 4], l[i + 5])
    tri = Triangle(A, B, C)
    tri.cnt()
    i += 6