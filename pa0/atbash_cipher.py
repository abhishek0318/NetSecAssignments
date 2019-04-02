class AtbashCipher:
    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            ciphertext += chr(ord('z') - (ord(char) - ord('a')))
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            plaintext += chr(ord('z') - (ord(char) - ord('a')))
        return plaintext

if __name__ == "__main__":
    cipher = AtbashCipher()
    print(cipher.encrypt("security"))
    #print(cipher.decrypt("abc"))