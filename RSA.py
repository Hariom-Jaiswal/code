import math

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d


p = int(input("Enter p Prime number: "))
q = int(input("Enter q Prime number: "))

n = p * q
phi = (p-1) * (q-1)

e = int(input("Enter e: "))

if math.gcd(e, phi) != 1:
    print("Invalid e")
    exit()

d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

#Encrypt
M = int(input("Enter Message: "))
C = (M**e) % n
print("Encrypted: ", C)

#Decrypt
M = int(input("Enter Message: "))
C = (M**d) % n
print("Decrypted: ", C)
