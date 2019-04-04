from des import *

from itertools import zip_longest

import numpy
import matplotlib.pyplot as plt
from skimage import img_as_bool, img_as_ubyte
from skimage.io import imread

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def xor(string1, string2):
    output = []
    for bit1, bit2 in zip(string1, string2):
        output.append((int(bit1) + int(bit2)) % 2)
    return ''.join([str(bit) for bit in output])

def ECB(data, key):
    """Implements ECB mode of operation.
    
    Args:
        data: numpy array of binary digits
        key: string of length 64
    
    Returns:
        encrypted data: numpy array of binary digits
    """
    outputs = []
    cipher = DES()
    data = ''.join(map(lambda x: str(int(x)), data))
    for block in grouper(data, 64):
        output = cipher.encrypt(key, ''.join(block))
        outputs.append(output)
    return numpy.array(outputs).flatten()

def CBC(data, key, iv):
    """Implements CBC mode of operation.
    
    Args:
        data: numpy array of binary digits
        key: string of length 64
        iv: string of length 64
    
    Returns:
        encrypted data: numpy array of binary digits
    """
    outputs = []
    cipher = DES()
    output = iv
    data = ''.join(map(lambda x: str(int(x)), data))
    for block in grouper(data, 64):
        output = cipher.encrypt(key, xor(output, block))
        outputs.append(output)
        output = ''.join([str(bit) for bit in output])
    return numpy.array(outputs).flatten()

if __name__ == "__main__":
    img = imread('newton.jpg', as_grey=True)
    img = img_as_bool(img)

    plt.imshow(img_as_ubyte(img), cmap='gray')
    plt.show()

    output = ECB(img.flatten(), key='0110110101101111011011100110000101110010011000110110100001111001')

    plt.imshow(img_as_ubyte(output.reshape(256, 256)), cmap='gray')
    plt.show()

    output = CBC(img.flatten(), key='0110110101101111011011100110000101110010011000110110100001111001',
                iv='0110010101101111111001100110000101111010011000110110100001111001')

    plt.imshow(img_as_ubyte(output.reshape(256, 256)), cmap='gray')
    plt.show()

