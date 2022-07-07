# Inicio: 06/07/22 - fim: 07/07/22
# Graziela Felix

mensage = input('Mensage: ')
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

# remove especials and blank characters
def clean_text(m):
    result = ''
    for letra in m:
        r = text_compare(letra.upper())
        if r is True:
            result = result + letra.lower()

    return result


def text_compare(letra):

    if letra == ' ':
        return False

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False


mensage_clean = clean_text(mensage)

# Key 'a' Verification to the rule 1 ≤ a ≤ m, gcd(a, m) = 1

def key_a_verification():
    a = int(input("Chave a: "))
    divisor = 0
    dividendo = 0
    m = len(alphabet)

    if (a < m):
        dividendo = a
        divisor = m
    else:
        dividendo = m
        divisor = a

    # GCD verification
    while True:
        resto = dividendo % divisor
        if (resto != 0):
            dividendo = divisor
            divisor = resto
        else:
            mdc = divisor
            if (mdc == 1):
                return a
            else:
                print("This key is not valid, because not correspond to '1 ≤ a ≤ m, gcd(a, m)=1'")
                a = key_a_verification()
                return a


a = key_a_verification()

# Key 'b' verification to the rule 1 ≤ b ≤ m
def key_b_verfication():
    b = int(input("Chave b: "))
    if (b >= 1 and b <= len(alphabet)):
        return b
    else:
        print("The key B needs to be 1 ≤ b ≤ m")
        b = key_b_verfication()
        return b

b = key_b_verfication()


# AFFINE CIPHER
def affine_cipher(acm, a, b):
    result = ''
    for ac in acm:
        d = a*cont_number(ac.upper()) + b
        n = d / len(alphabet)
        c = d - len(alphabet)*int(n)
        c = alphabet[c]
        result = result + c
    return result.lower()


def cont_number(n):

    cont = 0
    for a in alphabet:
        if n == a:
            return cont
        else:
            cont += 1


print(affine_cipher(mensage_clean, a, b))