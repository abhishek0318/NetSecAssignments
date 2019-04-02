class LCG:
    def __init__(self, m, a, c, x0):
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0

    def next(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn


if __name__ == "__main__":
    rnd = LCG(a=7, c=0, m=32, x0=1)
    for i in range(1, 100):
        print(rnd.next(), end=' ')
        