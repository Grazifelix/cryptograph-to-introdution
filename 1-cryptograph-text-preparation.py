# 01/07/22
# Graziela Felix

mensage = input('Insira sua mensagem: ')


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
                'V', 'W', 'X', 'Y', 'Z']
    for a in alphabet:
        if letra == a:
            return True
    return False


print(clean_text(mensage))
