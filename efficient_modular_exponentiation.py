# Graziela Maria
# 12 de setembro de 2022

# function A^B mod C
def efficient_modular_exponentiation(base, exponent, modulo):
    result = 1

    base = base % modulo

    if base == 0:
        return 0

    while exponent > 0:

        # If y is odd, multiply
        # x with result
        if (exponent & 1) == 1:
            result = (result * base) % modulo

        # y must be even now
        exponent = exponent >> 1  # y = y/2
        base = (base * base) % modulo

    return result


def main():
    base = int(input("Insert the base value: "))
    exponent = int(input("Insert the exponent value : "))
    modulo = int(input("Insert the module value: "))
    result = efficient_modular_exponentiation(base, exponent, modulo)
    print(result)


if __name__ == "__main__":
    main()