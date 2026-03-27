# Diffie-Hellman Key Exchange

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Private keys
a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("Alice Public Key:", A)
print("Bob Public Key:", B)

# Shared secret
K1 = pow(B, a, p)
K2 = pow(A, b, p)

print("Shared Key (Alice):", K1)
print("Shared Key (Bob):", K2)