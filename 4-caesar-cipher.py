#  10/07/22
# Graziela Felix
3
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# Selection between encryption or decryption
def option():
    op = int(input("Select an option: \n 1 - Encryption \n 2 - Decryption \n"))
    if op == 1 or op == 2:
        caesar_cipher(op)
    else:
        option()


# clean_text
def clean_text():
    mensage = input('Mensage: ')
    result = ''
    for letra in mensage:
        r = comparison(letra.upper())
        if r is True:
            result = result + letra.lower()

    return result


def comparison(letra):
    if letra == ' ':
        return True

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False


def caesar_cipher(op):
    mensage = clean_text()
    key = int(input("Key: "))
    result = ''
    for x in mensage:
        if x == ' ':
            result = result + ' '
        else:
            x = cont_number(x.upper())
            # e(x) = x + k (mod m) -> encryption
            if op == 1:
                x = x + key
            else:
                # e(x) = x + k (mod m) -> decryption
                x = x - key
            x = x - len(alphabet)*int(x / len(alphabet))  # x mod m
            x = alphabet[x]
            result = result + x
    print(result)


def cont_number(n):
    cont = 0
    for a in alphabet:
        if n == a:
            return cont
        cont += 1


option()
