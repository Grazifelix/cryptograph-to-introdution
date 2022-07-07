# 06/07/22

mensage = input('Mensage: ')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']

# cleaning
def clean_text(m):
    result = ''
    for letra in m:
        r = comparacao(letra.upper())
        if r is True:
            result = result + letra.lower()

    return result


def comparacao(letra):
    if letra == ' ':
        return True

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False

# Atbash Cipher

mensage_clean = clean_text(mensage)


def atbash_cipher(mc):

    result = ''
    for mcl in mc:
        i = cont_number(mcl.upper())
        if i is None:
            result = result + ' '
        else:
            i = alphabet[26-i]
            result = result + i
    return result


def cont_number(n):
    cont = 0
    for a in alphabet:
        cont += 1
        if n == a:
            return cont

print(atbash_cipher(mensage_clean))