import numpy as np
import time

from des import *

class TripleDES:
    def __init__(self, k1, k2):
        """Initialises object.
        
        Args:
            k1: string with binary digits of length 64
            k2: string with binary digits of length 64
        """

        self.k1 = k1
        self.k2 = k2
        self.des = DES()
    
    def encrypt(self, data):
        """Encrypts.
        
        Args:
            data: of type np.uint64

        Returns:
            output: of type np.uint64
        """

        data = '{:064b}'.format(data)
        output = self.des.run(self.k1, data, ENCRYPT)
        output = self.des.run(self.k2, output, DECRYPT)
        output = self.des.run(self.k1, output, ENCRYPT)
        return np.uint64(int(output, 2))
        
class ANSIX917:
    def __init__(self, v0, k1, k2):
        self.vi = np.uint64(v0) 
        self.k1 = k1
        self.k2 = k2
        self.tdes = TripleDES(self.k1, self.k2)

    def next(self):
        self.dti = np.float64(time.time())
        dti_string = self.dti.view(np.int64).item()
        self.ri = self.tdes.encrypt(self.vi ^ self.tdes.encrypt(dti_string))
        self.vi = self.tdes.encrypt(self.ri ^ self.tdes.encrypt(dti_string))
        return self.ri

if __name__ == "__main__":
    k1 = '0110110101101111011011100110000101110010011000110110100001111001'
    k2 = '0100011010000111111011011010011001100101101001001100011011110100'
    rnd = ANSIX917(v0=1, k1=k1, k2=k2)
    for i in range(1, 100):
        print(rnd.next(), end=' ')