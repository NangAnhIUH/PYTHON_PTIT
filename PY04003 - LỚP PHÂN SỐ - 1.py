from math import gcd
class Fraction:
    def __init__(self, a, b):
        self.gcd = gcd(a, b)
        self.a = a
        self.b = b
    def rutGon(self):
        self.a //= self.gcd
        self.b //= self.gcd
        return f'{self.a}/{self.b}'

a, b = map(int, input().split())
P = Fraction(a, b)
print(P.rutGon())