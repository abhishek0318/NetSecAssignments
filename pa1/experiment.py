import matplotlib.pyplot as plt

from caeser_cipher import CaeserCipher
from vigenere_cipher import VigenereCipher
from playfair_cipher import PlayfairCipher
from des import DES 

with open('crypto.txt', 'r') as file:
    text = file.read()
    
text = ''.join([char for char in text.lower() if char in 'abcdefghijklmnopqrstuvwxyz'])

def build_freq(text):
    freq = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}
    for char in text:
        if char in freq:
            freq[char] += 1
    return freq

def plot(text, max_freq_plaintext, label, marker):
    freq = build_freq(text)
    rel_freq = {char: freq[char]/max_freq_plaintext for char in freq}
    plt.plot(sorted(rel_freq.values(), reverse=True), label=label, marker=marker)

ccipher = CaeserCipher()
vcipher = VigenereCipher("cryptography")
pcipher = PlayfairCipher("cryptography")
dcipher = DES()

max_freq_plaintext = max(build_freq(text).values())
plot(text, max_freq_plaintext, 'Plaintext', '>')
plot(ccipher.encrypt(text), max_freq_plaintext, 'Caeser Cipher', '<')
plot(vcipher.encrypt(text), max_freq_plaintext, 'Vigenere Cipher', '+')
plot(pcipher.encrypt(text), max_freq_plaintext, 'Playfair Cipher', 'x')
plot(dcipher.encrypt("monarchy", text), max_freq_plaintext, 'DES', 'o')
plt.xlabel('Frequency ranked letters')
plt.ylabel('Relative frequency')
plt.title("Simmon's Experiment")
plt.legend()
plt.show()