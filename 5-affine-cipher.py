# Inicio: 06/07/22 - fim: 10/07/22
# Graziela Felix


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']


# remove especials and blank characters
def clean_text():
    mensage = input('Mensage: ')
    result = ''
    for letra in mensage:
        r = text_compare(letra.upper())
        if r is True:
            result = result + letra.lower()
    option(result)


def text_compare(letra):

    if letra == ' ':
        return False

    else:
        for a in alphabet:
            if letra == a:
                return True
        return False

# Selection between encryption or decryption
def option(msg):
    op = int(input("Select an option: \n 1 - Encryption \n 2 - Decryption \n"))
    if op == 1:
        affine_cipher_encryption(msg)
    elif op == 2:
        affine_cipher_decryption(msg)
    else:
        option(msg)


# Key 'a' Verification to the rule 1 ≤ a ≤ m, gcd(a, m) = 1
def key_a_verification():
    a = int(input("Chave a: "))
    m = len(alphabet)

    if a < m:
        dividend = a
        divisor = m
    else:
        dividend = m
        divisor = a

    # GCD verification
    while True:
        resto = dividend % divisor
        if resto != 0:
            dividend = divisor
            divisor = resto
        else:
            gdc = divisor
            if gdc == 1:
                return a
            else:
                print("This key is not valid, because not correspond to '1 ≤ a ≤ m, gcd(a, m)=1'")
                a = key_a_verification()
                return a


# Key 'b' verification to the rule 1 ≤ b ≤ m
def key_b_verfication():
    b = int(input("Chave b: "))
    if 1 <= b <= len(alphabet):
        return b
    else:
        print("The key B needs to be 1 ≤ b ≤ m")
        b = key_b_verfication()
        return b


# AFFINE CIPHER
def affine_cipher_encryption(acm):
    a = key_a_verification()
    b = key_b_verfication()
    result = ''
    for ac in acm:
        c = a*cont_number(ac.upper()) + b  # a*p+b
        c = c - len(alphabet)*int(c / len(alphabet))  # c mod m = c-m*c/m
        c = alphabet[c]
        result = result + c
    print(result.lower())


# The affine cipher decryption function
def affine_cipher_decryption(acdm):
    a = key_a_verification()
    a = a_inverse(a)
    b = key_b_verfication()
    result = ''
    for c in acdm:
        p = a*(cont_number(c.upper())-b)  # a^-1.(c-b)
        p = p - len(alphabet)*int(p / len(alphabet))  # p mod m = p-m * p/m
        p = alphabet[p]
        result = result + p
    print(result.lower())


# function to calculate the inverse of 'a' by the rule a.x = 1 mod m
def a_inverse(a):
    x = 0
    while True:
        r = int((a*x) % len(alphabet))  # a*x%m
        if r == 1:  # = 1 mod 1
            return x
        else:
            x += 1


# function to find the letter number in the alphabet list
def cont_number(n):
    cont = 0
    for a in alphabet:
        if n == a:
            return cont
        else:
            cont += 1


clean_text()
