class BBS:
    def __init__(self, p, q, s):
        self.p = p
        self.q = q
        self.n = p * q
        self.s = s
        self.xi = (s ** 2) % self.n 

    def next(self):
        self.xi = (self.xi ** 2) % self.n
        return self.xi % 2


if __name__ == "__main__":
    rnd = BBS(p=383, q=503, s=101355)
    for i in range(1, 100):
        print(rnd.next(), end=' ')
        