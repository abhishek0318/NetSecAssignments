import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kstest

from lcg import LCG
from bbs import BBS
from ansix917 import ANSIX917

if __name__ == "__main__":
    rnd_gen = LCG(m=31, a=13, c=0, x0=12)

    # rnd_gen = BBS(p=383, q=503, s=101355)

    # k1 = '0110110101101111011011100110000101110010011000110110100001111001'
    # k2 = '0100011010000111111011011010011001100101101001001100011011110100'
    # rnd_gen = ANSIX917(v0=1, k1=k1, k2=k2)

    x = []
    for i in range(1, 10001):
        x_n = rnd_gen.next()
        x.append(x_n) 
    x = np.array(x)

    rnge = x.max() - x.min()
    x = (x - x.min()) / rnge

    print(kstest(x, 'uniform'))

