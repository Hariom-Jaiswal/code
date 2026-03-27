import hashlib

text = input("Enter text: ")

# SHA-256
hash_value = hashlib.sha256(text.encode()).hexdigest()

print("Hash:", hash_value)