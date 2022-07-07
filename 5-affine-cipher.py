# 06/07/22


mensage = input('Mensagem: ')


# remove especials and blank characters
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
        return False

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False


print(clean_text(mensage))

# affine cipher
mensage_clean = clean_text(mensage)
# p = input().split('')
a = int(input("Chave a: ")) # need verification to the rule i ≤ b ≤ m
b = int(input("Chave b: "))

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

def affineCipher(acm, al):
    result = ''
    for ac in acm:
        d = a*contNumber(ac.upper(), al) + b
        n = d / len(al)
        c = d - len(al)*int(n)
        c = al[c]
        result = result + c
    return result.lower()

def contNumber(n, al):

    cont = 0
    for a in al:
        if n == a:
            return cont
        else:
            cont += 1

print(affineCipher(mensage_clean, alphabet))