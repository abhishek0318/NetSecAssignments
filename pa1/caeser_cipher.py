class CaeserCipher:
    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
                ciphertext += chr(ord('a') + (ord(char) - ord('a') + 3) % 26)
        return ciphertext

if __name__ == "__main__":
    cipher = CaeserCipher()
    print(cipher.encrypt("xyzabc"))
