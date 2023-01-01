class Rectangle:
    def __init__(self, a: int, b: int, c: str):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return 2 * (self.a + self.b)
    def area(self):
        return self.a * self.b
    def color(self):
        return self.c.capitalize()


arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
