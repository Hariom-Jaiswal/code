alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def keyMatrix(key):
    key = key.replace("J", "I")
    used = ''
    matrix = []

    for i in key:
        if i not in used:
            used = used + i

    for i in alpha:
        if i not in used:
            used = used + i

    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))
    
    return matrix



def textPair(text):
    text = text.replace('J', 'I')
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]

        if i+1 < len(text):
            b = text[i+1]

            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1

        pairs.append((a, b))

    return pairs

def pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i,j
            


def encry(text, key):
    matrix = keyMatrix(key)  
    pairs = textPair(text)

    result = ''

    for a,b in pairs:
        r1, c1 = pos(matrix, a)
        r2, c2 = pos(matrix, b)

        if r1 == r2:
            result = result + matrix[r1][(c1+1)%5]
            result = result + matrix[r2][(c2+1)%5]

        elif c1 == c2:
            result = result + matrix[(r1+1)%5][c1]
            result = result + matrix[(r2+1)%5][c2]

        else:
            result = result + matrix[r1][c2]
            result = result + matrix[r2][c1]

    print("Encrypted Text:", result)



text = input("Enter the Text: ").upper()
key = input("Enter the Key: ").upper()

encry(text, key)