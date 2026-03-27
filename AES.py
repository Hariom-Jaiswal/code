from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'   # 16 bytes key
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
plaintext = input("Enter text: ").encode()
ciphertext = cipher.encrypt(pad(plaintext, 16))
print("Encrypted:", ciphertext)

# Decrypt
decrypted = unpad(cipher.decrypt(ciphertext), 16)
print("Decrypted:", decrypted.decode())