# 10/07/22
# Graziela Felix

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# clean_text
def clean_text(m):
    result = ''
    for letra in m:
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


# ROT13 Cipher
def rot13_cipher():
    key_13 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C',
              'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    mensage = input("Mensage: ")
    mensage = clean_text(mensage)
    result = ''
    for m in mensage:
        if m == ' ':
            result = result + ' '
        else:
            m = cont_number(m.upper())
            m = key_13[m]
            result = result + m
    print(result)


def cont_number(n):
    cont = 0
    for a in alphabet:
        if n == a:
            return cont
        cont += 1

rot13_cipher()
