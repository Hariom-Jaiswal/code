def encry(text, key):
    encry = ''

    for c in range(len(text)):
        e = ord(text[c]) ^ ord(key[c])
        encry = encry + chr(e)

    print("Your Encrypted Text: ", encry)
    print("Encrypted (ASCII):", [ord(i) for i in encry])  # visible output
    return encry

def decry(cipher, key):
    decry = ''

    for c in range(len(cipher)):
        d = ord(cipher[c]) ^ ord(key[c])
        decry = decry + chr(d)

    print("Your Decrypted Text: ", decry)


text = ''
key = ' '
while len(text) != len(key):
    print("\n#Key and PlainText should be of same Length")
    text = input("Enter the Text: ")
    key = input("Enter the Key: ")

decry(encry(text, key),key)
    
