Alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Sub =   "QWERTYUIOPASDFGHJKLZXCVBNM"

def encry(text):
    encry = ''

    for i in text:
        if i in Alpha:
            ipos = Alpha.index(i)
            encry = encry + Sub[ipos]
        else:
            encry = encry + i   # handle space/symbols

    print("Your Encrypted Text: ", encry)

def decry(text):
    decry = ''

    for i in text:
        ipos = Sub.index(i)
        decry = decry + Alpha[ipos]

    print("Your Decrypted Text: ", decry)


text = (input("Enter the Text: ")).upper()
decry(text)