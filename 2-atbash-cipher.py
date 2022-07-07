# 06/07/22

mensage = input('Mensagem: ')

# Limpeza
def clean_text(m):
    result = ''
    for letra in m:
        r = comparacao(letra.upper())
        if r is True:
            result = result + letra.lower()

    return result


def comparacao(letra):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ê', 'Ô', 'Ã', 'Õ']

    if letra == ' ':
        return True

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False

# Atashi cipher

mensage_clean = clean_text(mensage)

def atashiCipher(mc):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    result = ''
    for mcl in mc:
        i = contNumber(mcl.upper())
        if i is None:
            result = result + ' '
        else:
            i = alphabet[26-i]
            result = result + i
    return result


def contNumber(n):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    cont = 0
    for a in alphabet:
        cont += 1
        if n == a:
            return cont

print(atashiCipher(mensage_clean))