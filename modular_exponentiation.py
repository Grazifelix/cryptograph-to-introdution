# Graziela Maria
# 01 de setembro de 2022


# function A^B mod C

def modular_exponentiation(base, exponent, modulo):
    result = 1

    # # change the exponent to a binary number
    binary = bin(exponent)
    binary = binary[2:]
    binary = binary[::-1]

    # Converting the binary number in base-2 numeral system
    base_two_numeral_list = []
    exponent_count = 0
    for i in binary:
        if i == '1':
            base_two_numeral_list.append(2**exponent_count)
            exponent_count += 1
        elif i == '0':
            exponent_count += 1

    # use the results of base-2 exponentiation as an exponent of A
    # Calculate the (mod C) of each base A exponentiation
    for j in base_two_numeral_list:
        result = result * ((base**j) % modulo)
    result = result % modulo

    return result


def main():
    base = int(input("Insert the base value: "))
    exponent = int(input("Insert the exponent value : "))
    modulo = int(input("Insert the module value: "))
    result = modular_exponentiation(base, exponent, modulo)
    print(result)


if __name__ == "__main__":
    main()
