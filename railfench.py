def encrypt(text, rails):
    rail = ['' for _ in range(rails)]
    
    row = 0
    direction = 1   # 1 = down, -1 = up

    for ch in text:
        rail[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(rail)


text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

cipher = encrypt(text, rails)
print("Encrypted:", cipher)




def decrypt(cipher, rails):
    pattern = [['\n' for _ in range(len(cipher))] for _ in range(rails)]

    row, direction = 0, 1

    # Mark positions
    for col in range(len(cipher)):
        pattern[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    # Fill letters
    index = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if pattern[i][j] == '*' and index < len(cipher):
                pattern[i][j] = cipher[index]
                index += 1

    # Read zig-zag
    result = ''
    row, direction = 0, 1

    for col in range(len(cipher)):
        result += pattern[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return result


cipher = input("Enter cipher: ")
rails = int(input("Enter number of rails: "))

print("Decrypted:", decrypt(cipher, rails))