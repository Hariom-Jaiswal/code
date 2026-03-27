def encrypt(text, key):
    col = len(key)
    row = len(text) // col
    if len(text) % col != 0:
        row += 1

    # Fill matrix
    matrix = [['X' for _ in range(col)] for _ in range(row)]
    k = 0

    for i in range(row):
        for j in range(col):
            if k < len(text):
                matrix[i][j] = text[k]
                k += 1

    # Sort key
    key_order = sorted(list(key))
    
    cipher = ''

    for ch in key_order:
        col_index = key.index(ch)
        for i in range(row):
            cipher += matrix[i][col_index]

    return cipher


text = input("Enter text: ").upper().replace(" ", "")
key = input("Enter key: ").upper()

print("Encrypted:", encrypt(text, key))











def decrypt(cipher, key):
    col = len(key)
    row = len(cipher) // col

    matrix = [['' for _ in range(col)] for _ in range(row)]

    key_order = sorted(list(key))
    k = 0

    for ch in key_order:
        col_index = key.index(ch)
        for i in range(row):
            matrix[i][col_index] = cipher[k]
            k += 1

    text = ''
    for i in range(row):
        for j in range(col):
            text += matrix[i][j]

    return text


cipher = input("Enter cipher: ")
key = input("Enter key: ").upper()

print("Decrypted:", decrypt(cipher, key))