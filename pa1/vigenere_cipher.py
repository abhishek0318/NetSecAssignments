class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        i = 0
        ciphertext = ''
        for char in plaintext:
            ciphertext += chr(ord('a') + (ord(char) + ord(self.key[i]) - 2 * ord('a')) % 26)
            i = (i + 1) % len(self.key)
        return ciphertext

if __name__ == "__main__":
    cipher = VigenereCipher("attist")
    print(cipher.encrypt("simple"))
