Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encry(text, key):
    encry = ''

    for i in text:
        ipos = Alpha.index(i)
        e = (ipos + key) % 26 
        encry = encry + Alpha[e]
    
    print("Your Encrypted Text: ", encry)

def decry(text, key):
    decry = ''

    for i in text:
        ipos = Alpha.index(i)
        d = (ipos - key) % 26
        decry = decry + Alpha[d]
    
    print("Your Decrypted Text: ", decry)

text = (input("Enter the Text: ")).upper()
key = int(input("Enter the Key: "))

encry(text, key)
