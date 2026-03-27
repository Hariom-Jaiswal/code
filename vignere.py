alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(text, key):
    encry = ''

    for c in range(len(text)):
        tpos = alpha.index(text[c])
        kpos = alpha.index(key[c])
        e = (tpos + kpos) % 26

        encry = encry + alpha[e]

    print("Your Encrypted Text: ", encry)
    return encry

def decry(text, key):
    decry = ''

    for c in range(len(text)):
        tpos = alpha.index(text[c])
        kpos = alpha.index(key[c])
        d = (tpos - kpos) % 26

        decry = decry + alpha[d]

    print("Your Decrypted Text: ", decry)


text = input("Enter the Text: ").upper()
key = input("Enter the key: ").upper()

while len(text) > len(key):
    flag = 'f'
    for i in key:
        if flag=='f':
            key = key + i
            if len(key) == len(text):
                flag = 't'

decry(encry(text, key), key)